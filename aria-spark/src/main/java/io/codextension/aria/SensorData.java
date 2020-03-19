package io.codextension.aria;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.streaming.StreamingQuery;

import java.util.HashMap;
import java.util.Map;

public abstract class SensorData {
    private String tableName;
    private Map<String, String> variables;

    public SensorData(Map<String, String> variables, String tableName) {
        this.variables = variables;
        this.tableName = tableName;
    }

    public abstract StreamingQuery startWorking();

    protected void writeJDBC(Dataset<Row> ds, Long epochId) {
        ds.persist();
        Map<String, String> options = new HashMap<>();
        options.put("url", this.variables.get("url"));
        options.put("dbtable", this.tableName);
        options.put("driver", "org.postgresql.Driver");
        options.put("user", this.variables.get("user"));
        options.put("password", this.variables.get("pwd"));
        ds.write().format("jdbc").mode("append").options(options).save();
        ds.unpersist();
    }
}
