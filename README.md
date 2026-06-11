# SPAM SHIELD – AI Spam Detection System

## Project Overview

SPAM SHIELD is an AI-based SMS spam detection system that classifies messages as SPAM or HAM (safe).  
It is built using Machine Learning techniques and trained on the UCI SMS Spam Collection dataset.

---

## Team Members

- Tanzeela Fatima (Roll No: 12)  
  Role: Model Development, Web Application, Backend Integration  

- Atif Zaheer (Roll No: 7)  
  Role: Data Analysis (EDA), Visualization, Presentation  

---

## Dataset

- Source: UCI SMS Spam Collection Dataset  
- Total Messages: 5,574  
  - Spam: 747  
  - Ham: 4,827  

---

## Machine Learning Models

- Logistic Regression → 98.21%  
- SVM → 98.30%  
- Random Forest → 98.57% (Best Model)  

---

## Confusion Matrix (Random Forest)

- Correct Ham Predictions: 960  
- Ham misclassified as Spam: 6  
- Spam misclassified as Ham: 7  
- Correct Spam Predictions: 142  

---

## How to Run the Project

1. Clone the repository:
   git clone https://github.com/TanzeelaFatima492/Spam-Email-Detection

2. Move into project folder:
   cd spam_web_app

3. Install dependencies:
   pip install -r requirements.txt

4. Train the model:
   python create_model.py

5. Run the application:
   python app.py

6. Open in browser:
   http://127.0.0.1:5000

---

## Testing Examples

- "FREE MONEY!" → SPAM  
- "Hey, meeting?" → SAFE  

---

## Technologies Used

- Python  
- Scikit-learn  
- Pandas  
- NumPy  
- Flask  
- HTML / CSS  

---

## Links

- GitHub Repository: https://github.com/TanzeelaFatima492/Spam-Email-Detection  
- Dataset: https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection  

---

## Course Information

- Course: Machine Learning  
- Submission Date: 20-04-2026  
- Supervisor: Mam Naila  

---

## Features

- Real-time spam detection  
- Machine Learning based classification  
- Web interface using Flask  
- High accuracy model  

---

## Future Improvements

- Deploy on cloud (AWS / Render / Heroku)  
- Add Deep Learning models (LSTM / BERT)  
- Improve UI design  
- Email spam detection support  
