from pyspark.sql.types import *
from pyspark.sql.functions import *
import os

class TemperatureData():

    def __init__(self, df, db):
        self.df = df
        self.db = db
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
        # df = df.withColumn(
        #     "id", monotonically_increasing_id()
        # )  # adding a db identifier
        df.write.format("jdbc").mode("append").options(
            url=self.db["url"],
            dbtable="temperature",
            driver="org.postgresql.Driver",
            user=self.db["user"],
            password=self.db["pwd"],
        ).save()
        df.unpersist()

    def start_working(self):
        sensor = self.df.filter("topic == 'temperature'")
        sensor = sensor.select(from_json(sensor.value, self.temp_schema).alias("data")).select(
            "data.*"
        )

        # converting timestamp column to Timestamp type, somehow the conversion doesn't work from the start.
        sensor = sensor.withColumn("timestamp", sensor["timestamp"].cast(TimestampType(
        )))

        ds = sensor.writeStream.foreachBatch(self.write_jdbc).start()
        return ds
