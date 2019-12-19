import findspark
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split
from pyspark.sql.types import *
from pyspark.sql.functions import *
from smarthome_utils import read_configuration


class TemperatureData():

    def __init__(self, spark, df):
        self.spark = spark
        self.df = df
        self.config = read_configuration()
        self.temp_schema = StructType(
            [
                StructField("temperature", DoubleType(), True),
                StructField("humidity", DoubleType(), True),
                StructField("timestamp", DoubleType(), True)
            ]
        )

    def write_jdbc(self, df, epoch_id):
        # Transform and write batchDF
        df.persist()
        df.write.format("jdbc").mode("append").options(
            url=self.config["db"]["url"],
            dbtable="temperature",
            driver=self.config["db"]["driver"],
            user=self.config["db"]["username"],
            password=self.config["db"]["password"],
        ).save()
        df.unpersist()

    def start_working(self):
        sensor = self.df.filter("topic == 'temperature'")
        sensor = sensor.select(from_json(sensor.value, self.temp_schema).alias("data")).select(
            "data.*"
        )

        # converting timestamp column to Timestamp type, somehow the conversion doesn't work from the start.
        sensor = sensor.withColumn("timestamp", sensor["timestamp"].cast(TimestampType(
        ))).withColumn("id", monotonically_increasing_id())  # adding a db identifier

        ds = sensor.writeStream.foreachBatch(self.write_jdbc).start()
        return ds
