# create_model.py - Run this first

import pandas as pd
import re
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("="*50)
print("Creating Spam Detection Model...")
print("="*50)

# Load dataset
url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
df = pd.read_csv(url, sep='\t', header=None, names=['label', 'message'])

# Add MORE spam examples so model learns
more_spam = pd.DataFrame({
    'label': ['spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam'],
    'message': [
        'FREE MONEY! Click here to win $1000 instantly!',
        'CONGRATULATIONS! You won a free iPhone! Claim now!',
        'URGENT! Your account will be closed. Verify immediately!',
        'You have won a lottery! Send money to claim prize!',
        'Click this link for a special discount just for you!',
        'FREE gift card! Claim within 24 hours!',
        'WINNER! You have been selected for a cash prize!'
    ]
})

df = pd.concat([df, more_spam], ignore_index=True)
print(f"Dataset shape: {df.shape}")

# Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

df['cleaned'] = df['message'].apply(clean_text)
df['label_binary'] = df['label'].map({'spam': 1, 'ham': 0})

# Split data
X = df['cleaned']
y = df['label_binary']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# TF-IDF
tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# Train Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train_tfidf, y_train)

# Test
y_pred = rf.predict(X_test_tfidf)
acc = accuracy_score(y_test, y_pred)
print(f"✅ Accuracy: {acc:.4f}")

# Test your specific message
test_msg = "FREE MONEY! Click here to win $1000 instantly!"
cleaned = clean_text(test_msg)
transformed = tfidf.transform([cleaned])
pred = rf.predict(transformed)[0]
print(f"\n🔍 Test Message: {test_msg}")
print(f"✅ Prediction: {'SPAM' if pred == 1 else 'HAM'}")

# Save models (in current folder, NOT in models folder)
joblib.dump(rf, 'best_model.pkl')
joblib.dump(tfidf, 'tfidf_vectorizer.pkl')
print("\n✅ Saved: best_model.pkl")
print("✅ Saved: tfidf_vectorizer.pkl")
print("\n✅ Model created successfully!")
print("Now run: python app.py")
