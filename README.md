SPAM SHIELD - AI SPAM DETECTION

Accuracy: 98.57% | Model: Random Forest

TEAM:
Tanzeela Fatima (Roll 12) - Model, Web App, Backend
Atif Zaheer (Roll 7) - EDA, Visuals, Presentation

DATASET:
SMS Spam Collection (UCI)
5,574 messages (747 spam, 4,827 ham)

RESULTS:
Logistic Regression: 98.21%
Random Forest: 98.57% (BEST)
SVM: 98.30%

Confusion Matrix (Random Forest):
- Ham correct: 960
- Ham as Spam: 6
- Spam as Ham: 7
- Spam correct: 142

HOW TO RUN:
cd spam_web_app
pip install -r requirements.txt
python create_model.py
python app.py
Open http://127.0.0.1:5000

TEST:
"FREE MONEY!" → SPAM
"Hey, meeting?" → SAFE

LINKS:
GitHub: https://github.com/TanzeelaFatima492/Spam-Email-Detection
Dataset: https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection

COURSE:
Machine Learning | Submission: 20-04-26 | Supervisor: Mam Naila
