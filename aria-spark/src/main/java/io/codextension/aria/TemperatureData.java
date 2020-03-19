package io.codextension.aria;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.functions;
import org.apache.spark.sql.streaming.StreamingQuery;
import org.apache.spark.sql.types.*;

import java.util.Map;

public class TemperatureData extends SensorData {

    private final StructType tempSchema;
    private Dataset<Row> ds;

    public TemperatureData(Dataset<Row> ds, Map<String, String> variables) {
        super(variables,"temperature");
        this.ds = ds;
        StructField[] fields = new StructField[3];
        fields[0] = new StructField("temperature", DataTypes.DoubleType, true, Metadata.empty());
        fields[1] = new StructField("humidity", DataTypes.DoubleType, true, Metadata.empty());
        fields[2] = new StructField("timestamp", DataTypes.DoubleType, true, Metadata.empty());
        this.tempSchema = new StructType(fields);
    }

    @Override
    public StreamingQuery startWorking() {
        Dataset<Row> sensor = this.ds.filter("topic == 'temperature'");
        sensor = sensor.select(functions.from_json(sensor.col("value"), this.tempSchema).alias("data")).select("data.*");
        sensor = sensor.withColumn("timestamp", sensor.col("timestamp").cast(DataTypes.TimestampType));

        return sensor.writeStream().foreachBatch(this::writeJDBC).start();
    }
}
