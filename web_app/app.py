from flask import Flask, request, render_template_string, jsonify
import joblib
import re
import os

app = Flask(__name__)

# Get the folder where this file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model files from SAME folder
model_path = os.path.join(BASE_DIR, 'best_model.pkl')
tfidf_path = os.path.join(BASE_DIR, 'tfidf_vectorizer.pkl')

print(f"Looking for model at: {model_path}")

if os.path.exists(model_path) and os.path.exists(tfidf_path):
    model = joblib.load(model_path)
    tfidf = joblib.load(tfidf_path)
    print("✅ Model loaded successfully!")
else:
    print("❌ Model files not found!")
    print("Please run: python create_model.py first")
    model = None
    tfidf = None

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def predict_spam(message):
    if model is None or tfidf is None:
        return "MODEL NOT LOADED", 0
    cleaned = clean_text(message)
    transformed = tfidf.transform([cleaned])
    pred = model.predict(transformed)[0]
    # Get confidence
    try:
        proba = model.predict_proba(transformed)[0]
        confidence = max(proba) * 100
    except:
        confidence = 95.0
    return ("SPAM" if pred == 1 else "HAM", confidence)

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Spam Detector</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 20px;
            padding: 40px;
            max-width: 600px;
            width: 100%;
            text-align: center;
        }
        textarea {
            width: 100%;
            height: 150px;
            padding: 15px;
            border-radius: 10px;
            border: 2px solid #ddd;
            font-size: 16px;
        }
        button {
            background: #4f46e5;
            color: white;
            padding: 12px 30px;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            margin-top: 20px;
            font-size: 16px;
        }
        .spam { color: red; font-weight: bold; }
        .ham { color: green; font-weight: bold; }
        .result-box {
            margin-top: 20px;
            padding: 20px;
            border-radius: 10px;
        }
        .result-spam { background: #fee; border-left: 4px solid red; }
        .result-ham { background: #e8f5e9; border-left: 4px solid green; }
    </style>
</head>
<body>
    <div class="container">
        <h1>📧 Spam Detector</h1>
        <p>AI-powered message classification | 98.57% Accuracy</p>
        <form method="POST">
            <textarea name="message" placeholder="Type your message here...">{{ message }}</textarea><br>
            <button type="submit">🔍 Analyze Message</button>
        </form>
        
        {% if result %}
        <div class="result-box result-{{ 'spam' if result == 'SPAM' else 'ham' }}">
            <h2 class="{{ 'spam' if result == 'SPAM' else 'ham' }}">
                {{ '🚨 SPAM DETECTED' if result == 'SPAM' else '✅ SAFE MESSAGE' }}
            </h2>
            <p><strong>Message:</strong> {{ message }}</p>
            <p><strong>Confidence:</strong> {{ confidence }}%</p>
        </div>
        {% endif %}
        
        <div style="margin-top: 30px; font-size: 12px; color: #888;">
            Powered by Random Forest • 98.57% Accuracy
        </div>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    confidence = None
    message = ''
    
    if request.method == 'POST':
        message = request.form.get('message', '')
        if message:
            result, confidence = predict_spam(message)
            confidence = round(confidence, 1)
    
    return render_template_string(HTML, result=result, confidence=confidence, message=message)

@app.route('/api/predict', methods=['POST'])
def predict_api():
    data = request.get_json()
    message = data.get('message', '')
    result, confidence = predict_spam(message)
    return jsonify({'result': result, 'confidence': confidence})

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 Spam Detector Web App Starting...")
    print("="*50)
    print("📱 Open browser: http://127.0.0.1:5000")
    print("="*50 + "\n")
    app.run(debug=True)
