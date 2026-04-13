#🛡️ SPAM SHIELD - AI-POWERED SPAM DETECTION SYSTEM

A Machine Learning system that detects spam messages with 98.57% accuracy using NLP + Random Forest

---

📋 PROJECT OVERVIEW

This project builds an intelligent system that automatically identifies whether a message is SPAM or HAM (legitimate). It combines Natural Language Processing (NLP) to understand text and Random Forest to make accurate predictions.

How It Works: User Message → NLP Cleaning → TF-IDF Numbers → Random Forest → SPAM/HAM

---

👥 TEAM MEMBERS

| Name | Roll Number | Role |
|------|-------------|------|
| Tanzeela Fatima | 12 | NLP, Model Building, Backend, Flask Web App |
| Atif Zaheer | 7 | EDA, Visualizations, Frontend, Presentation |

---

📊 DATASET

Source: SMS Spam Collection (UCI)

- Total messages: 5,574
- Spam messages: 747 (13.4%)
- Ham messages: 4,827 (86.6%)

Dataset Link: https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection

---

🛠️ TECHNOLOGIES USED

| Category | Tools |
|----------|-------|
| Data Processing | Pandas, NumPy, re |
| Machine Learning | Scikit-learn |
| Web Framework | Flask |
| Development | Google Colab, VS Code |
| Version Control | Git, GitHub |

---

📈 RESULTS

| Model | Accuracy |
|-------|----------|
| Logistic Regression | 98.21% |
| Random Forest | 98.57% 🏆 |
| SVM | 98.30% |

Confusion Matrix - Random Forest:

| | Predicted Ham | Predicted Spam |
|---|---------------|----------------|
| Actual Ham | 960 | 6 |
| Actual Spam | 7 | 142 |

- True Negatives (Ham correct): 960
- False Positives (Ham as Spam): 6
- False Negatives (Spam as Ham): 7
- True Positives (Spam correct): 142

Best Model: Random Forest with 98.57% accuracy

---

🌐 FLASK WEB APP

Features:
- Real-time SPAM/HAM detection
- Confidence score display
- One-click test examples
- Modern UI with animations

How to Run:

cd spam_web_app
pip install -r requirements.txt
python create_model.py
python app.py

Then open: http://127.0.0.1:5000

---

📁 PROJECT STRUCTURE

Spam-Email-Detection/
├── spam_web_app/
│   ├── app.py
│   ├── create_model.py
│   ├── best_model.pkl
│   ├── tfidf_vectorizer.pkl
│   └── requirements.txt
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_evaluation.ipynb
└── README.md

---

🎯 TEST THE MODEL

| Message | Result |
|---------|--------|
| FREE MONEY! Click here to win $1000! | 🚨 SPAM |
| Hey, are we meeting for lunch? | ✅ SAFE |
| URGENT: Your account is compromised! | 🚨 SPAM |
| Can you send me the assignment? | ✅ SAFE |
| Congratulations! You won a free iPhone! | 🚨 SPAM |

---

📝 CONCLUSION

The Random Forest model achieved the best performance with 98.57% accuracy, correctly identifying 142 out of 149 spam messages and 960 out of 966 ham messages.

The Flask web app provides a user-friendly interface to test the model in real-time, making it accessible for demonstration and practical use.

---

🔗 LINKS

- GitHub Repository: https://github.com/TanzeelaFatima492/Spam-Email-Detection
- Dataset: https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection

---

🙏 ACKNOWLEDGMENTS

- Mam Naila – Course Instructor
- Atif Zaheer – Project Partner

---

📧 CONTACT

| Name | Roll Number |
|------|-------------|
| Tanzeela Fatima | 12 |
| Atif Zaheer | 7 |

---

**Course:** Machine Learning
**Submission Date:** 20-04-26
**Supervisor:** Mam Naila

⭐ Star this repository if you found it helpful!
