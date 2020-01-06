import os
import threading
import json
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
from dust_data import DustData
from temperature_data import TemperatureData

# Initialising pyspark (the spark runner)
packages = [
    "org.postgresql:postgresql:42.2.9",
    "com.h2database:h2:1.4.200",
    "com.alibaba:fastjson:1.2.62",
    "org.apache.spark:spark-streaming-kafka_2.11:1.6.3",
    "org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.4",
    "org.apache.logging.log4j:log4j-api:2.7",
    "org.apache.logging.log4j:log4j-core:2.7",
    "org.apache.spark:spark-core_2.11:2.4.4",
    "org.apache.spark:spark-sql_2.11:2.4.4",
]

os.environ[
    "PYSPARK_SUBMIT_ARGS"
] = f"--master local[*] --packages {','.join(packages)}  pyspark-shell"

'''
os.environ["CX_KAFKA_URL"]="192.168.178.63:9092"
os.environ["CX_DB_URL"]="jdbc:postgresql://localhost:5432/pi"
os.environ["CX_DB_DRIVER"]="org.postgresql.Driver"
os.environ["CX_DB_USER"]="sa"
os.environ["CX_DB_PWD"]="sa"
'''

class SparkInit:
    def __init__(self):
        self.spark = (
            SparkSession.builder.config("spark.streaming.concurrentJobs", "3")
            .config("spark.scheduler.mode", "FAIR")
            .appName("smarthome")
            .getOrCreate()
        )

        self.df = (
            self.spark.readStream.format("kafka")
            .option("kafka.bootstrap.servers", os.getenv("CX_KAFKA_URL"))
            .option("subscribe", "dust,temperature")
            .option("startingOffsets", "latest")  # latest/earliest
            .load()
        )
        self.df = self.df.withColumn("value", self.df.value.astype("string"))
        self.dust_data = DustData(self.df)
        self.temperature_data = TemperatureData(self.df)

    def start(self):
        self.temperature_data.start_working()
        self.dust_data.start_working()

        self.spark.streams.awaitAnyTermination()


spark_init = SparkInit()
spark_init.start()
