from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, DoubleType, IntegerType, LongType
import numpy as np
import json
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'model'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'alerts'))
from anomaly_detector import AnomalyDetector
from slack_alerts import send_slack_alert

def main():
    spark = SparkSession.builder \
        .appName("CloudMetricsAnomalyDetection") \
        .getOrCreate()

    # Define schema for incoming JSON data
    schema = StructType([
        StructField("cpu_usage", DoubleType(), True),
        StructField("memory_usage", DoubleType(), True),
        StructField("disk_usage", DoubleType(), True),
        StructField("network_in", DoubleType(), True),
        StructField("network_out", DoubleType(), True),
        StructField("api_request_rate", IntegerType(), True),
        StructField("timestamp", LongType(), True)
    ])

    # Read from Kafka topic 'cloud_metrics'
    df = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "cloud_metrics") \
        .option("startingOffsets", "latest") \
        .load()

    # Extract the value as string and parse JSON
    json_df = df.selectExpr("CAST(value AS STRING) as json_str") \
        .select(from_json(col("json_str"), schema).alias("data")) \
        .select("data.*")

    # Initialize anomaly detector
    detector = AnomalyDetector()

    def detect_anomaly(batch_df, batch_id):
        # Collect batch data to driver
        data = batch_df.select("cpu_usage", "memory_usage", "disk_usage", "network_in", "network_out", "api_request_rate").collect()
        if not data:
            return
        X = np.array([[
            row['cpu_usage'],
            row['memory_usage'],
            row['disk_usage'],
            row['network_in'],
            row['network_out'],
            row['api_request_rate']
        ] for row in data])

        # Predict anomalies
        preds = detector.predict(X)

        for i, pred in enumerate(preds):
            if pred == -1:
                anomaly_info = f"Anomaly detected: {data[i]}"
                print(anomaly_info)
                send_slack_alert(anomaly_info)

    query = json_df.writeStream \
        .foreachBatch(detect_anomaly) \
        .start()

    query.awaitTermination()

if __name__ == "__main__":
    main()
