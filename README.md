# 🔴 DDoS Intrusion Detection System — Real-Time ML API

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)](https://docker.com)
[![AWS EC2](https://img.shields.io/badge/AWS_EC2-FF9900?style=flat&logo=amazonaws&logoColor=white)](https://aws.amazon.com/ec2)

> CNN + LSTM model deployed as a **FastAPI REST API on AWS EC2** — real-time inference on 2M+ network flow records with **97.3% accuracy**, **AUC-ROC 0.98**, and **<200ms latency**.

---

## 📊 Results

| Metric | Score |
|--------|-------|
| Detection Accuracy | **97.3%** |
| AUC-ROC | **0.98** |
| False Positive Rate | **< 1%** |
| Inference Latency | **< 200ms** |
| Dataset Size | **2M+ records** |
| Class Imbalance | 15:1 → resolved with SMOTE |

---

## 🧱 Architecture
```
CIC-IDS2018 Data → ETL Pipeline → Feature Engineering
→ CNN + LSTM Model → FastAPI REST API → AWS EC2
→ Model Monitoring + Logging
```

---

## 📡 API Usage
```bash
POST /predict
Content-Type: application/json

{
  "features": [0.12, 0.87, 0.34, ...]
}
```

Response:
```json
{
  "prediction": "attack",
  "confidence": 0.973,
  "latency_ms": "<200ms"
}
```

---

## 🚀 Run Locally
```bash
git clone https://github.com/saiujwalveerapalli/ddos-attack-detection-.git
cd ddos-attack-detection-
pip install -r requirements.txt
uvicorn app:app --reload
```

---

## 🐳 Docker
```bash
docker build -t ddos-api .
docker run -p 8000:8000 ddos-api
```

---

## 📁 Project Structure
```
ddos-detection-api/
├── app.py              # FastAPI REST API
├── src/
│   └── preprocess.py   # ETL pipeline + SMOTE
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 📚 Related Publication

**Regression Metrics in Advanced Machine Learning** — IRJET, 2024

---

## 👤 Author

**Sai Ujwal Veerapalli** · [LinkedIn](https://linkedin.com/in/saiujwalveerapalli) · [Portfolio](https://saiujwalveerapalli.github.io)
