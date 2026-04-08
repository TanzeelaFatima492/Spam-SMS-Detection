# 🚀 Spam Email Detection System

A Machine Learning based classification system to detect spam emails with high accuracy (98.57%)

---

## 📋 Project Overview

This project implements a binary classification system that automatically identifies whether an email is spam or legitimate (ham). Using various machine learning algorithms, we preprocess email data, extract meaningful features, and build predictive models to classify emails accurately.

### Problem Statement
With the increasing volume of emails received daily, spam detection has become crucial for email security and user productivity. This project aims to build an automated system that can distinguish spam emails from legitimate ones with high accuracy and minimal false positives.

---

## 👥 Team Members & Contributions

| Name | Roll Number | Responsibilities | Contribution |
|------|-------------|------------------|--------------|
| Tanzeela Fatima | 12 | Data Preprocessing, Model Building, Evaluation, Code Implementation, Flask Web App | 50% |
| Atif Zaheer | 7 | EDA, Visualization, Presentation, Panaflex Design | 50% |

---

## 📊 Dataset Information

**Source:** SMS Spam Collection v.1 (UCI Machine Learning Repository)

| Feature | Description |
|---------|-------------|
| label | 'spam' or 'ham' |
| message | SMS text content |
| Samples | 5,574 messages |
| Spam | 747 messages (13.4%) |
| Ham | 4,827 messages (86.6%) |

### 🔗 Dataset Links

- **UCI Repository:** https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection
- **Direct Download:** https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv

---

## 🧠 What is NLP?

**NLP (Natural Language Processing)** teaches computers to understand human language.

### NLP Steps in This Project:

| Step | Code | What It Does |
|------|------|--------------|
| 1 | `text.lower()` | Convert to lowercase |
| 2 | `re.sub(r'[^\w\s]', '', text)` | Remove punctuation |
| 3 | `re.sub(r'\d+', '', text)` | Remove numbers |
| 4 | `re.sub(r'\s+', ' ', text).strip()` | Remove extra spaces |
| 5 | `TfidfVectorizer()` | Convert text to numbers |

**Example:**
```
Input: "FREE MONEY! Click here to win $1000!"
After NLP: "free money click here to win"
After TF-IDF: [0.85, 0.92, 0.00, 0.67, ...] (Numbers computer understands)
```

---

## 🌲 What is Random Forest?

**Random Forest** = 100 decision trees voting together to make predictions.

### Why Random Forest for Spam Detection?

| Feature | Benefit |
|---------|---------|
| 100 trees voting | More accurate than single tree |
| Handles text patterns | Perfect for spam detection |
| No overfitting | Generalizes well to new messages |
| Feature importance | Shows which words matter most |

### How Random Forest Works:

```
        Input Message
              ↓
    ┌─────────┼─────────┐
    ↓         ↓         ↓
 Tree 1    Tree 2    Tree 100
  (SPAM)    (HAM)     (SPAM)
    ↓         ↓         ↓
    └─────────┼─────────┘
              ↓
         VOTING (7 vs 3)
              ↓
        FINAL: SPAM ✅
```

---

## 🛠️ Technologies Used

| Category | Tools/Libraries |
|----------|-----------------|
| Data Processing | Pandas, NumPy, re |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Web Framework | Flask |
| Development | Google Colab, Jupyter Notebook, VS Code |
| Version Control | Git, GitHub |

---

## 🌐 Flask Web App

A professional web interface to test the spam detection model in real-time.

### Features

| Feature | Description |
|---------|-------------|
| Real-time Prediction | Instant SPAM/HAM detection |
| Confidence Score | Shows prediction confidence |
| Example Messages | One-click test examples |
| Modern UI | Gradient background, smooth animations |
| Responsive Design | Works on mobile and desktop |
| Keyboard Shortcut | Ctrl+Enter to analyze |

---

## 📈 Results

### Model Performance Comparison

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| Logistic Regression | 98.21% | 0.9714 | 0.9524 | 0.9618 |
| Random Forest | **98.57%** | **0.9800** | 0.9524 | **0.9660** |
| SVM | 98.30% | 0.9762 | 0.9524 | 0.9641 |

**🏆 Best Model: Random Forest with 98.57% accuracy**

### Confusion Matrix - Random Forest

| | Predicted Ham | Predicted Spam |
|---|---|---|
| **Actual Ham** | 960 | 6 |
| **Actual Spam** | 7 | 142 |

- True Negatives (Ham correct): 960
- False Positives (Ham as Spam): 6
- False Negatives (Spam as Ham): 7
- True Positives (Spam correct): 142

### Key Findings
- Random Forest outperformed other algorithms with 98.57% accuracy
- Feature importance shows words like "free", "win", "click" are strong spam indicators
- TF-IDF with n-grams (1,2) performed better than unigrams alone
- Only 13 misclassifications out of 1,115 test messages

---

## 📁 Project Structure

```
Spam-Email-Detection/
│
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_evaluation.ipynb
│
├── spam_web_app/
│   ├── app.py                 # Flask web application
│   ├── create_model.py        # Train and save model
│   ├── best_model.pkl         # Trained Random Forest
│   ├── tfidf_vectorizer.pkl   # TF-IDF converter
│   └── requirements.txt       # Dependencies
│
├── README.md
└── requirements.txt
```

---

## 🚀 How to Run

### Option 1: Flask Web App (Easiest - Test in Browser)

```bash
cd spam_web_app
pip install -r requirements.txt
python create_model.py
python app.py
# Open http://127.0.0.1:5000
```

### Option 2: Google Colab (No Installation)

1. Open [Google Colab](https://colab.research.google.com)
2. Upload notebooks from `notebooks/` folder
3. Run in order:
   - `01_data_preprocessing.ipynb`
   - `02_feature_engineering.ipynb`
   - `03_model_training.ipynb`
   - `04_evaluation.ipynb`

### Option 3: Local Machine with Jupyter

```bash
# Clone repository
git clone https://github.com/TanzeelaFatima492/Spam-Email-Detection.git
cd Spam-Email-Detection

# Install dependencies
pip install -r requirements.txt

# Run notebooks in Jupyter
jupyter notebook notebooks/
```

---

## 🎯 Test the Model

Try these messages in the web app:

| Message | Expected Result |
|---------|-----------------|
| "FREE MONEY! Click here to win $1000!" | 🚨 SPAM |
| "Hey, are we meeting for lunch?" | ✅ SAFE |
| "URGENT: Your account is compromised!" | 🚨 SPAM |
| "Can you send me the assignment?" | ✅ SAFE |
| "Congratulations! You won a free iPhone!" | 🚨 SPAM |

---

## 📝 Conclusion

The Random Forest model achieved the best performance with **98.57% accuracy**, correctly identifying 142 out of 149 spam messages and 960 out of 966 ham messages.

The Flask web app provides a user-friendly interface to test the model in real-time, making it accessible for demonstration and practical use.

---

## 🔗 Links

- **GitHub Repository:** https://github.com/TanzeelaFatima492/Spam-Email-Detection
- **Dataset:** https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection

---

## 🙏 Acknowledgments

- **Mam Naila** – Course Instructor
- **Atif Zaheer** – Project Partner

---

## 📧 Contact

| Name | Roll Number |
|------|-------------|
| Tanzeela Fatima | 12 |
| Atif Zaheer | 7 |

---

**Course:** Machine Learning  
**Submission Date:** 20-04-26  
**Supervisor:** Mam Naila

---

⭐ Star this repository if you found it helpful!
