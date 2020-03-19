package io.codextension.aria;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.functions;
import org.apache.spark.sql.streaming.StreamingQuery;
import org.apache.spark.sql.types.*;

import java.util.Map;

public class DustData extends SensorData {

    private StructType dustSchema;
    private Dataset<Row> ds;

    public DustData(Dataset<Row> ds, Map<String, String> variables) {
        super(variables, "dust");
        this.ds = ds;
        StructField[] fields = new StructField[4];
        fields[0] = new StructField("value", DataTypes.IntegerType, true, null);
        fields[1] = new StructField("voltage", DataTypes.FloatType, true, null);
        fields[2] = new StructField("density", DataTypes.DoubleType, true, null);
        fields[3] = new StructField("timestamp", DataTypes.DoubleType, true, null);
        this.dustSchema = new StructType(fields);
    }

    @Override
    public StreamingQuery startWorking() {
        Dataset<Row> sensor = this.ds.filter("topic == 'dust'");
        sensor = sensor.select(functions.from_json(sensor.col("value"), this.dustSchema).alias("data")).select("data.*");

        sensor = sensor.withColumn("timestamp", sensor.col("timestamp").cast(DataTypes.TimestampType));
        sensor = (
                sensor.withWatermark("timestamp", "5 minutes")
                        .groupBy(functions.window(functions.column("timestamp"), "1 minutes"))
                        .avg()
        );
        sensor = (
                sensor.withColumn("startdate", sensor.col("window").getField("start"))
                        .withColumn("window", sensor.col("window").getField("end"))
                        .withColumnRenamed("window", "enddate")
                        .withColumnRenamed("avg(value)", "value")
                        .withColumnRenamed("avg(voltage)", "voltage")
                        .withColumnRenamed("avg(density)", "density")
        );

        return sensor.writeStream().foreachBatch(this::writeJDBC).start();
    }
}
