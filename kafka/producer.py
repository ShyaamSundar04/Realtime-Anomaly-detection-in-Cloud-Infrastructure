import time
import json
import random
from kafka import KafkaProducer

def generate_cloud_metrics():
    """
    Simulate cloud infrastructure metrics data.
    """
    metrics = {
        "cpu_usage": round(random.uniform(0, 100), 2),
        "memory_usage": round(random.uniform(0, 100), 2),
        "disk_usage": round(random.uniform(0, 100), 2),
        "network_in": round(random.uniform(0, 1000), 2),
        "network_out": round(random.uniform(0, 1000), 2),
        "api_request_rate": random.randint(0, 1000),
        "timestamp": int(time.time())
    }
    return metrics

def main():
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    topic = 'cloud_metrics'

    print("Starting Kafka producer to send cloud metrics...")
    try:
        while True:
            metrics = generate_cloud_metrics()
            producer.send(topic, metrics)
            print(f"Sent metrics: {metrics}")
            time.sleep(1)  # Send data every second
    except KeyboardInterrupt:
        print("Kafka producer stopped.")
    finally:
        producer.close()

if __name__ == "__main__":
    main()
