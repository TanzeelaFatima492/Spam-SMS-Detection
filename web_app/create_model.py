# THIS CODE HAS A BUG - Classifies SPAM as HAM

import pandas as pd
import re
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

print("Loading dataset...")
url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
df = pd.read_csv(url, sep='\t', header=None, names=['label', 'message'])

# BUG 1: Not adding enough spam examples to training data
# The model doesn't learn modern spam patterns

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    return text  # BUG 2: Missing space cleaning

df['cleaned'] = df['message'].apply(clean_text)
df['label_binary'] = df['label'].map({'spam': 1, 'ham': 0})

X_train, X_test, y_train, y_test = train_test_split(
    df['cleaned'], df['label_binary'], test_size=0.2, random_state=42
)  # BUG 3: Missing stratify parameter

# BUG 4: Too few features (only 1000 instead of 5000)
tfidf = TfidfVectorizer(max_features=1000)  # Should be 5000
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# BUG 5: Too few trees in Random Forest
rf = RandomForestClassifier(n_estimators=10, random_state=42)  # Should be 100
rf.fit(X_train_tfidf, y_train)

# Test with spam message
test_msg = "FREE MONEY! Click here to win $1000 instantly!"
cleaned = clean_text(test_msg)
transformed = tfidf.transform([cleaned])
pred = rf.predict(transformed)[0]

print(f"Message: {test_msg}")
print(f"Prediction: {'HAM' if pred == 0 else 'SPAM'}")
# This will print HAM even though it's SPAM!
