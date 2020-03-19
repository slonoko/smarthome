package io.codextension.aria;


import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.streaming.StreamingQueryException;
import org.apache.spark.sql.types.DataTypes;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class App {
    public static void main(String[] args) throws StreamingQueryException {
        String KAFKA_URL = System.getenv("CX_KAFKA_URL");

        Map<String, String> dbInfo = new HashMap<>();
        dbInfo.put("url", "jdbc:postgresql://aria-storage:5432/" + System.getenv("CX_DB_NAME"));
        dbInfo.put("user", System.getenv("CX_DB_USER"));
        dbInfo.put("pwd", System.getenv("CX_DB_PWD"));

        SparkSession spark = SparkSession.builder().appName("aria-spark").getOrCreate();

        Dataset<Row> ds = spark.readStream().format("kafka")
                .option("kafka.bootstrap.servers", KAFKA_URL)
                .option("subscribe", "dust,temperature")
                .option("startingOffsets", "latest").load();
        ds = ds.withColumn("value", ds.col("value").cast(DataTypes.StringType));

        List<SensorData> sensors = new ArrayList<>();
        sensors.add(new DustData(ds, dbInfo));
        sensors.add(new TemperatureData(ds, dbInfo));

        for (SensorData sensorData : sensors) {
            sensorData.startWorking();
        }

        spark.streams().awaitAnyTermination();
    }
}
