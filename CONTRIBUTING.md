🤝 **Contributing to Realtime Anomaly Detection**

Thank you for your interest in contributing to Realtime Anomaly Detection! 🚀
This project aims to provide a scalable and efficient anomaly detection framework for streaming data, powered by Kafka, Spark, and Python.

We welcome contributions of all kinds — bug reports, documentation improvements, feature requests, or code contributions.

**🛠️ Getting Started**
1. Fork and Clone the Repository
git clone https://github.com/ShyaamSundar04/Realtime-Anomaly-detection-in-Cloud-Infrastructure.git
cd realtime-anomaly-detection

2. Start Required Services

Navigate to the deployment directory and spin up the core services using Docker Compose:

cd deployment

# Start Apache Spark
docker compose up -d spark

# Start Zookeeper & Kafka
docker compose up -d zookeeper kafka

# Start Dashboard service
docker compose up -d dashboard

3. Run Kafka Producer

From the project root directory, start the Kafka producer:

cd kafka
python producer.py

4. Monitor Kafka Logs

To check real-time Kafka logs:

cd deployment
docker compose logs -f kafka

**Reporting Issues**

If you find a bug or have a feature request, please open an Issue on GitHub with:

Clear title and description

Steps to reproduce (if it’s a bug)

Logs, screenshots, or error messages (if applicable)

**📄 License**

By contributing, you agree that your contributions will be licensed under the same terms as this project: MIT License.
