# 🛡️ Spam Shield

## AI-Powered Spam Detection System

> A Machine Learning system that detects spam messages with **98.57% accuracy** using NLP + Random Forest

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Team Members](#team-members)
- [Dataset](#dataset)
- [Technologies Used](#technologies-used)
- [Results](#results)
- [Flask Web App](#flask-web-app)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Test the Model](#test-the-model)
- [Conclusion](#conclusion)
- [Links](#links)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## 📋 Project Overview

This project builds an intelligent system that automatically identifies whether a message is **SPAM** or **HAM** (legitimate).

### How It Works
User Message → NLP Cleaning → TF-IDF Numbers → Random Forest → SPAM/HAM


### Problem Statement

Millions of spam messages are sent daily. This system helps filter them automatically with high accuracy.

---

## 👥 Team Members

| Name | Roll Number | Role |
|------|-------------|------|
| **Tanzeela Fatima** | 12 | NLP, Model Building, Backend, Flask Web App |
| **Atif Zaheer** | 7 | EDA, Visualizations, Frontend, Presentation |

### Contribution Breakdown

| Task | Owner |
|------|-------|
| Data Preprocessing | Tanzeela |
| Feature Engineering | Tanzeela |
| Model Training & Evaluation | Tanzeela |
| Flask Web App | Tanzeela |
| EDA & Visualizations | Atif |
| Presentation & Panaflex | Atif |

---

## 📊 Dataset

**Source:** SMS Spam Collection v.1 (UCI Machine Learning Repository)

| Feature | Value |
|---------|-------|
| Total messages | 5,574 |
| Spam messages | 747 (13.4%) |
| Ham messages | 4,827 (86.6%) |

### Dataset Links

- 🔗 [UCI Repository](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection)
- 🔗 [Direct Download](https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv)

---

## 🛠️ Technologies Used

### Core Technologies

| Category | Tools |
|----------|-------|
| **Data Processing** | Pandas, NumPy, re |
| **Machine Learning** | Scikit-learn |
| **Web Framework** | Flask |
| **Development** | Google Colab, VS Code |
| **Version Control** | Git, GitHub |

### NLP Techniques Used

| Technique | Purpose |
|-----------|---------|
| Lowercase | Convert all text to same case |
| Remove punctuation | Clean special characters |
| Remove numbers | Remove digits |
| TF-IDF | Convert text to numbers |

---

## 📈 Results

### Model Performance Comparison

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| Logistic Regression | 98.21% | 0.9714 | 0.9524 | 0.9618 |
| **Random Forest** | **98.57%** | **0.9800** | 0.9524 | **0.9660** |
| SVM | 98.30% | 0.9762 | 0.9524 | 0.9641 |

### Confusion Matrix - Random Forest

| | Predicted Ham | Predicted Spam |
|---|---------------|----------------|
| **Actual Ham** | 960 | 6 |
| **Actual Spam** | 7 | 142 |

### Key Metrics

- ✅ **True Negatives** (Ham correct): 960
- ❌ **False Positives** (Ham as Spam): 6
- ❌ **False Negatives** (Spam as Ham): 7
- ✅ **True Positives** (Spam correct): 142

### Key Findings

- Random Forest outperformed other algorithms with **98.57% accuracy**
- Words like "free", "win", "click" are strong spam indicators
- TF-IDF with n-grams (1,2) performed better than unigrams alone
- Only **13 misclassifications** out of 1,115 test messages

---

## 🌐 Flask Web App

### Features

| Feature | Description |
|---------|-------------|
| **Real-time Prediction** | Instant SPAM/HAM detection |
| **Confidence Score** | Shows prediction confidence percentage |
| **Example Messages** | One-click test examples |
| **Modern UI** | Gradient background, smooth animations |
| **Responsive Design** | Works on mobile and desktop |


### How to Run Web App

```bash
cd spam_web_app
pip install -r requirements.txt
python create_model.py
python app.py
Then open: http://127.0.0.1:5000

Spam-Email-Detection/
│
├── spam_web_app/
│   ├── app.py                 # Flask web application
│   ├── create_model.py        # Train and save model
│   ├── best_model.pkl         # Trained Random Forest
│   ├── tfidf_vectorizer.pkl   # TF-IDF converter
│   └── requirements.txt       # Dependencies
│
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_evaluation.ipynb
│
├── README.md
└── requirements.txt
