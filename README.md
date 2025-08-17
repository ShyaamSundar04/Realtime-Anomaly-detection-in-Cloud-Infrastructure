# Realtime-Anomaly-detection-in-Cloud-Infrastructure

# 📌 Overview

This project focuses on building a real-time anomaly detection system designed for cloud infrastructure environments.  

It leverages machine learning (Isolation Forest) for anomaly detection and runs in a containerized environment using Docker Compose.

# 🔹 Key Features:

Real-time streaming with Apache Kafka & Spark

Isolation Forest ML model for anomaly detection

Containerized architecture using Docker Compose

Scalable & cloud-ready design

Interactive Dashboard for anomaly visualization

# ⚙️ Architecture

            ┌──────────────┐
            │   Producer    │
            │ (Kafka Input) │
            └───────▲──────┘
                    │
            ┌───────┴───────┐
            │   Apache Kafka │
            └───────▲───────┘
                    │
            ┌───────┴──────────┐
            │   Apache Spark    │
            │ (Anomaly Model)   │
            └───────▲──────────┘
                    │
            ┌───────┴──────────┐
            │    Dashboard      │
            │  (Visualization)  │
            └───────────────────┘

# 🛠️ Tech Stack

Programming: Python 3.9+

Machine Learning: Isolation Forest (Scikit-learn)

Streaming: Apache Kafka + Zookeeper

Processing: Apache Spark

Containerization: Docker Compose

Visualization: Dashboard (Web UI)

# 📊 Dashboard

The dashboard provides real-time anomaly detection insights including:

Stream health  

Anomaly alerts  

System metrics

# 📜 License

This project is licensed under the MIT License – see the LICENSE file for details.

# 🌍 Project Status

✅ Public & Open Source  

✅ Ready for cloud infrastructure deployment  

🚧 Contributions for scaling, testing & visualization improvements are welcome
