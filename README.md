🛡️ Real-Time Intrusion Detection System (RTIDS)
This project implements a Real-Time Intrusion Detection System that leverages machine learning to detect potential cyberattacks in streaming network traffic data. It uses Kafka for streaming, Spark Structured Streaming for real-time ML prediction, and Streamlit for dynamic visualization. The predictions are stored locally and optionally pushed to Amazon S3 for long-term storage or further analysis.

📊 Features
✅ Real-time data ingestion using Kafka

✅ Machine Learning classification using a trained Random Forest model

✅ Stream processing and prediction with PySpark

✅ Interactive Streamlit dashboard with:

Live prediction counts

Time-based attack trends

Top attack protocols & services

Feature distributions by class

Hour-of-day heatmaps

Dynamic filters (protocol, hour, attack class)

✅ CSV export of predictions

✅ Optional AWS S3 upload for persistent storage

📁 Project Structure
python
Copy
Edit
intrusion-detection-pipeline/
├── kafka_producer.py         # Reads from test set and sends to Kafka
├── spark_stream.py           # Spark job to predict and write to CSV
├── dashboard.py              # Streamlit dashboard
├── train_model.py            # ML training pipeline (RandomForest)
├── rf_model.pkl              # Trained ML model
├── predictions.csv           # Output predictions (generated dynamically)
├── UNSW_NB15_training-set.csv
├── UNSW_NB15_testing-set.csv
├── zk-single-kafka-single.yml  # Docker Compose config
└── README.md
⚙️ Technologies Used
Apache Kafka – Real-time data streaming

Apache Spark (Structured Streaming) – Streaming pipeline and batch inference

Scikit-learn – ML model (Random Forest Classifier)

Streamlit – Real-time interactive dashboard

Pandas, Matplotlib, Altair – Data processing & plotting

AWS S3 – Cloud-based storage (optional)

🚀 Getting Started
1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/yourusername/intrusion-detection-pipeline.git
cd intrusion-detection-pipeline
2. Setup Virtual Environment
bash
Copy
Edit
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
Ensure pyspark, kafka-python, streamlit, boto3, pandas, scikit-learn, altair are in requirements.txt

3. Start Kafka and Zookeeper
bash
Copy
Edit
docker-compose -f zk-single-kafka-single.yml up
4. Train the Model (Optional)
bash
Copy
Edit
python train_model.py
5. Start the Kafka Producer
bash
Copy
Edit
python kafka_producer.py
6. Run Spark Streaming Job
bash
Copy
Edit
python spark_stream.py
7. Launch Streamlit Dashboard
bash
Copy
Edit
streamlit run dashboard.py
🌐 Optional: Store in AWS S3
To save predictions to Amazon S3:

Set your AWS credentials in environment variables:

bash
Copy
Edit
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=us-east-2
Update the S3 upload logic in spark_stream.py:

python
Copy
Edit
import boto3

s3 = boto3.client("s3")
s3.upload_file("predictions.csv", "your-s3-bucket-name", "predictions.csv")
📈 Sample Dashboard Preview

📌 Insights Available
📊 Total and real-time prediction counts

⏰ Hour-of-day attack heatmaps

⚠️ Alert spikes in attack activity

📡 Protocols and services used in attacks

🔍 Boxplots of key feature distributions

📋 Future Improvements
GeoIP location visualizations

Email/SMS alerts on attack surges

Integration with security monitoring tools (e.g., ELK stack)

Real-time streaming to Redshift, BigQuery

👩‍💻 Contributors
Samhitha Nuka – Data Science and ML Implementation

You can contribute by opening a pull request or reporting issues!

📄 License
This project is licensed under the MIT License.

