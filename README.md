# 🔴 DDoS Intrusion Detection System

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Deep learning system that detects DDoS network attacks with **97.3% accuracy** and **<1% false positive rate** — trained on 2M+ real network flow records.

---

## 📊 Results

| Metric | Score |
|---|---|
| Detection Accuracy | **97.3%** |
| False Positive Rate | **< 1%** |
| Dataset Size | **2M+ records** |
| Class Imbalance Handled | 15:1 ratio via SMOTE |

---

## 🧠 Model Architecture

**Why CNN + LSTM?**
- CNN extracts local feature patterns from packet sequences
- LSTM captures temporal dependencies in network traffic flow
- Combined architecture outperformed standalone models by 4.2%

---

## 📁 Dataset

**CIC-IDS2018** (Canadian Institute for Cybersecurity)
- 2M+ labeled network flow records
- Attack types: DDoS, DoS, Botnet, Infiltration, Web attacks
- Severe class imbalance (15:1 benign:attack) handled with **SMOTE oversampling**

---

## 🚀 Quick Start
```bash
git clone https://github.com/saiujwal-glitch/ddos-attack-detection-.git
cd ddos-attack-detection-
pip install -r requirements.txt
python src/preprocess.py --data_path data/raw/
python src/train.py --epochs 50 --batch_size 128
python src/evaluate.py --model_path models/cnn_lstm_best.h5
```

---

## 📂 Project Structure
```
ddos-attack-detection/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Preprocessing.ipynb
│   └── 03_Model_Training.ipynb
├── src/
│   ├── preprocess.py
│   ├── model.py
│   ├── train.py
│   └── evaluate.py
├── models/
│   └── cnn_lstm_best.h5
├── requirements.txt
└── README.md
```

---

## 📦 Requirements
```
tensorflow>=2.10
scikit-learn>=1.0
imbalanced-learn>=0.9
pandas>=1.4
numpy>=1.22
matplotlib>=3.5
seaborn>=0.11
```

---

## 📚 Related Publication

> **Regression Metrics in Advanced Machine Learning** — IEEE & IRJET, 2024

---

## 👤 Author

**Sai Ujwal Veerapalli**
- LinkedIn: [linkedin.com/in/saiujwalveerapalli](https://www.linkedin.com/in/saiujwalveerapalli)
- Email: saiujwal@iastate.edu
