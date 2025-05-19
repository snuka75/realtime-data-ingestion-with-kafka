# 🛡️ Real-Time Intrusion Detection System using Kafka, Spark, and Random Forest

This project implements a **real-time intrusion detection system (IDS)** using Apache Kafka and Apache Spark Streaming. A trained Random Forest model detects potential cyber-attacks from live network traffic data. The system is scalable and modular for integration into larger cybersecurity pipelines.

---

## 📁 Project Structure

```
.
├── kafka_producer.py            # Sends simulated network traffic to Kafka
├── spark_stream.py              # Spark job to consume data and predict attacks
├── train_model.py               # Trains Random Forest model on UNSW-NB15 dataset
├── UNSW_NB15_training-set.csv   # Training dataset
├── UNSW_NB15_testing-set.csv    # Testing dataset
├── zk-single-kafka-single.yml   # Kafka + Zookeeper Docker Compose setup
├── rf_model.pkl                 # Trained machine learning model
└── README.md                    # Project documentation

```
---

## ⚙️ Components Overview

### ✅ Kafka Producer
- Simulates real-time network logs by reading CSV rows and sending them to a Kafka topic (`network-logs`).

### ✅ Model Training
- Trains a Random Forest classifier using the UNSW-NB15 dataset.
- Outputs a serialized model file (`rf_model.pkl`) used in Spark.

### ✅ Spark Streaming Consumer
- Connects to the Kafka topic and applies the ML model in real time.
- Outputs predictions (`Normal` or `Attack`) to the console or logs.

### ✅ Kafka + Zookeeper Setup
- Dockerized setup using `zk-single-kafka-single.yml`.
- Easily deploy Kafka and Zookeeper locally using Docker Compose.

---

## 📦 Requirements

- Python 3.7+
- Apache Spark 3.x
- Docker & Docker Compose
- Python Libraries:
  ```bash
  pip install pandas scikit-learn joblib kafka-python pyspark
🚀 Getting Started
- Clone the Repository

git clone https://github.com/snuka75/realtime-data-ingestion-with-kafka.git
cd kafka-intrusion-detection

- Start Kafka and Zookeeper

   docker-compose -f zk-single-kafka-single.yml up

- Train the Machine Learning Model
   
    python train_model.py
  
- Start Kafka Producer

    python kafka_producer.py

- Start Spark Consumer

   spark-submit spark_stream.py

🧠 Dataset Used

UNSW-NB15 Dataset

Captures 49 features related to network flow: protocol, packet counts, TTL, state, etc.

Labels: Normal vs Attack

📊 Sample Output
```
[2025-05-19 12:00:01] Prediction: NORMAL
[2025-05-19 12:00:02] Prediction: ATTACK
```
Future Enhancements

Integrate real-time dashboards using Streamlit or Grafana

Add email/SMS alerts for detected attacks

Model interpretability using SHAP or LIME

Dockerize the entire pipeline for deployment

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss your proposed changes.


