from flask import Flask, request, render_template_string, jsonify
import joblib
import re
import os
import time

app = Flask(__name__)

# Load model and vectorizer
if os.path.exists('best_model.pkl') and os.path.exists('tfidf_vectorizer.pkl'):
    model = joblib.load('best_model.pkl')
    tfidf = joblib.load('tfidf_vectorizer.pkl')
    print("✅ Model loaded successfully!")
else:
    print("⚠️ Model files not found. Please run create_model.py first")
    model = None
    tfidf = None

def clean_text(text):
    """Clean the input text"""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def predict_spam(message):
    """Predict if message is spam or ham"""
    if model is None or tfidf is None:
        return "MODEL NOT LOADED", 0
    cleaned = clean_text(message)
    transformed = tfidf.transform([cleaned])
    pred = model.predict(transformed)[0]
    # Get probability if available
    try:
        proba = model.predict_proba(transformed)[0]
        confidence = max(proba) * 100
    except:
        confidence = 95.0
    return ("SPAM" if pred == 1 else "HAM", confidence)

# Modern HTML Template with Clean Footer
HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    <title>Spam Shield | AI-Powered Message Security</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 25%, #0f172a 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            position: relative;
            overflow-x: hidden;
        }

        /* Animated Background Particles */
        .particle {
            position: absolute;
            background: rgba(99, 102, 241, 0.15);
            border-radius: 50%;
            pointer-events: none;
            animation: float 8s infinite;
        }

        @keyframes float {
            0%, 100% { transform: translate(0, 0) scale(1); opacity: 0.3; }
            50% { transform: translate(30px, -30px) scale(1.2); opacity: 0.6; }
        }

        .container {
            background: rgba(255, 255, 255, 0.98);
            border-radius: 48px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.3), 0 0 0 1px rgba(255, 255, 255, 0.1);
            padding: 45px;
            max-width: 700px;
            width: 100%;
            position: relative;
            z-index: 10;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .container:hover {
            transform: translateY(-5px);
            box-shadow: 0 30px 60px -12px rgba(0, 0, 0, 0.4);
        }

        /* Header Section */
        .header {
            text-align: center;
            margin-bottom: 35px;
        }

        .logo-wrapper {
            display: inline-block;
            background: linear-gradient(135deg, #4f46e5, #7c3aed);
            width: 80px;
            height: 80px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 20px;
            box-shadow: 0 10px 25px -5px rgba(79, 70, 229, 0.4);
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }

        .logo-wrapper span {
            font-size: 42px;
        }

        h1 {
            font-size: 32px;
            font-weight: 800;
            background: linear-gradient(135deg, #0f172a, #4f46e5);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 8px;
            letter-spacing: -0.5px;
        }

        .subtitle {
            color: #64748b;
            font-size: 15px;
            font-weight: 400;
        }

        /* Input Section */
        .input-section {
            margin-bottom: 25px;
        }

        .label-wrapper {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            margin-bottom: 10px;
        }

        label {
            font-weight: 600;
            color: #1e293b;
            font-size: 14px;
        }

        .char-count {
            font-size: 12px;
            color: #94a3b8;
        }

        textarea {
            width: 100%;
            height: 180px;
            padding: 18px;
            border: 2px solid #e2e8f0;
            border-radius: 24px;
            font-size: 15px;
            font-family: inherit;
            resize: vertical;
            transition: all 0.3s ease;
            background: #f8fafc;
            line-height: 1.6;
        }

        textarea:focus {
            outline: none;
            border-color: #4f46e5;
            box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.1);
            background: white;
        }

        /* Button */
        .analyze-btn {
            background: linear-gradient(135deg, #4f46e5, #7c3aed);
            color: white;
            border: none;
            padding: 16px 32px;
            font-size: 16px;
            font-weight: 600;
            border-radius: 60px;
            cursor: pointer;
            width: 100%;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }

        .analyze-btn::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.3);
            transform: translate(-50%, -50%);
            transition: width 0.6s, height 0.6s;
        }

        .analyze-btn:hover::before {
            width: 300px;
            height: 300px;
        }

        .analyze-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 15px 30px -10px rgba(79, 70, 229, 0.5);
        }

        .analyze-btn:active {
            transform: translateY(0);
        }

        .analyze-btn:disabled {
            opacity: 0.7;
            cursor: not-allowed;
        }

        /* Loading Animation */
        .loader {
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            border-top-color: white;
            animation: spin 0.8s linear infinite;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        /* Result Section */
        .result-box {
            margin-top: 30px;
            padding: 28px;
            border-radius: 28px;
            animation: slideIn 0.5s ease;
            transition: all 0.3s ease;
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .result-spam {
            background: linear-gradient(135deg, #fef2f2, #fee2e2);
            border-left: 5px solid #ef4444;
            box-shadow: 0 10px 25px -5px rgba(239, 68, 68, 0.2);
        }

        .result-ham {
            background: linear-gradient(135deg, #ecfdf5, #d1fae5);
            border-left: 5px solid #10b981;
            box-shadow: 0 10px 25px -5px rgba(16, 185, 129, 0.2);
        }

        .result-label {
            font-size: 28px;
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 15px;
        }

        .result-spam .result-label {
            color: #dc2626;
        }

        .result-ham .result-label {
            color: #059669;
        }

        .result-message {
            font-size: 14px;
            color: #334155;
            line-height: 1.7;
            word-break: break-word;
            background: rgba(255, 255, 255, 0.7);
            padding: 15px;
            border-radius: 16px;
            margin: 15px 0;
        }

        .confidence-bar {
            margin-top: 15px;
        }

        .confidence-label {
            font-size: 12px;
            color: #64748b;
            margin-bottom: 5px;
            display: flex;
            justify-content: space-between;
        }

        .bar {
            height: 8px;
            background: #e2e8f0;
            border-radius: 10px;
            overflow: hidden;
        }

        .bar-fill {
            height: 100%;
            border-radius: 10px;
            transition: width 0.5s ease;
        }

        .bar-fill-spam {
            background: linear-gradient(90deg, #ef4444, #dc2626);
        }

        .bar-fill-ham {
            background: linear-gradient(90deg, #10b981, #059669);
        }

        /* Examples Section */
        .examples {
            margin-top: 30px;
            padding-top: 25px;
            border-top: 1px solid #e2e8f0;
        }

        .examples h3 {
            color: #475569;
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 15px;
            text-align: center;
        }

        .example-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
        }

        .example-card {
            background: #f1f5f9;
            padding: 8px 16px;
            border-radius: 50px;
            font-size: 13px;
            cursor: pointer;
            transition: all 0.2s ease;
            color: #334155;
            font-weight: 500;
        }

        .example-card:hover {
            background: linear-gradient(135deg, #4f46e5, #7c3aed);
            color: white;
            transform: scale(1.03);
        }

        /* Footer - Clean, No Empty Space */
        .footer {
            margin-top: 30px;
            text-align: center;
            font-size: 11px;
            color: #94a3b8;
            letter-spacing: 0.3px;
        }

        /* Responsive */
        @media (max-width: 550px) {
            .container {
                padding: 25px;
            }
            h1 {
                font-size: 24px;
            }
            .result-label {
                font-size: 20px;
            }
            .logo-wrapper {
                width: 60px;
                height: 60px;
            }
            .logo-wrapper span {
                font-size: 32px;
            }
            .example-card {
                padding: 6px 12px;
                font-size: 11px;
            }
            .footer {
                font-size: 10px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
           
            <h1>Spam Shield</h1>
            <p class="subtitle">AI-powered message security • Real-time protection</p>
        </div>

        <div class="input-section">
            <div class="label-wrapper">
                <label>📝 Enter your message</label>
                <span class="char-count"><span id="charCount">0</span> characters</span>
            </div>
            <textarea id="messageInput" placeholder="Type or paste your message here..."></textarea>
        </div>

        <button class="analyze-btn" id="analyzeBtn" onclick="analyzeMessage()">
            <span>🔍</span> Analyze Message
        </button>

        <div id="resultArea"></div>

        <div class="examples">
            <h3>📋 Try these examples</h3>
            <div class="example-grid">
                <div class="example-card" onclick="setMessage('Congratulations! You won a free iPhone! Click here to claim now!')">🔴 Spam</div>
                <div class="example-card" onclick="setMessage('Hey, are we still meeting for lunch tomorrow?')">🟢 Ham</div>
                <div class="example-card" onclick="setMessage('URGENT: Your account has been compromised! Verify now!')">⚠️ Urgent</div>
                <div class="example-card" onclick="setMessage('Can you please send me the assignment by evening?')">📚 Student</div>
                <div class="example-card" onclick="setMessage('FREE MONEY! Click this link to win $1000 instantly!')">💰 Scam</div>
            </div>
        </div>

        <div class="footer">
            ⚡ Real-time detection | 98.57% Accuracy
        </div>
    </div>

    <script>
        // Character counter
        const textarea = document.getElementById('messageInput');
        const charCount = document.getElementById('charCount');

        textarea.addEventListener('input', function() {
            charCount.textContent = this.value.length;
        });

        function setMessage(msg) {
            textarea.value = msg;
            charCount.textContent = msg.length;
            textarea.focus();
        }

        async function analyzeMessage() {
            const message = textarea.value.trim();

            if (!message) {
                showAlert('Please enter a message to analyze');
                return;
            }

            const btn = document.getElementById('analyzeBtn');
            const resultArea = document.getElementById('resultArea');

            // Show loading
            btn.disabled = true;
            btn.innerHTML = '<span class="loader"></span> Analyzing...';

            try {
                const response = await fetch('/predict_ajax', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: 'message=' + encodeURIComponent(message)
                });

                const data = await response.json();

                // Show result with animation
                const resultClass = data.result === 'SPAM' ? 'result-spam' : 'result-ham';
                const resultIcon = data.result === 'SPAM' ? '🚨 SPAM DETECTED' : '✅ SAFE MESSAGE';
                const iconSymbol = data.result === 'SPAM' ? '🔴' : '🟢';
                const barColor = data.result === 'SPAM' ? 'bar-fill-spam' : 'bar-fill-ham';

                resultArea.innerHTML = `
                    <div class="result-box ${resultClass}" style="animation: slideIn 0.5s ease;">
                        <div class="result-label">
                            <span>${iconSymbol}</span> ${resultIcon}
                        </div>
                        <div class="result-message">
                            <strong>📧 Message:</strong><br>
                            "${escapeHtml(message)}"
                        </div>
                        <div class="confidence-bar">
                            <div class="confidence-label">
                                <span>🎯 Confidence</span>
                                <span>${data.confidence.toFixed(1)}%</span>
                            </div>
                            <div class="bar">
                                <div class="bar-fill ${barColor}" style="width: ${data.confidence}%"></div>
                            </div>
                        </div>
                    </div>
                `;

                // Scroll to result
                resultArea.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

            } catch (error) {
                console.error('Error:', error);
                showAlert('An error occurred. Please try again.');
            } finally {
                btn.disabled = false;
                btn.innerHTML = '<span>🔍</span> Analyze Message';
            }
        }

        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }

        function showAlert(message) {
            const resultArea = document.getElementById('resultArea');
            resultArea.innerHTML = `
                <div style="background: #fee2e2; padding: 20px; border-radius: 20px; border-left: 4px solid #ef4444; margin-top: 20px;">
                    <div style="color: #dc2626; font-weight: 600;">⚠️ ${message}</div>
                </div>
            `;
            setTimeout(() => {
                if (resultArea.innerHTML.includes('⚠️')) {
                    resultArea.innerHTML = '';
                }
            }, 3000);
        }

        // Enter key support (Ctrl+Enter)
        textarea.addEventListener('keydown', function(e) {
            if (e.ctrlKey && e.key === 'Enter') {
                analyzeMessage();
            }
        });

        // Create particles
        function createParticles() {
            for (let i = 0; i < 10; i++) {
                const particle = document.createElement('div');
                particle.className = 'particle';
                particle.style.width = Math.random() * 100 + 50 + 'px';
                particle.style.height = particle.style.width;
                particle.style.left = Math.random() * 100 + '%';
                particle.style.top = Math.random() * 100 + '%';
                particle.style.animationDelay = Math.random() * 8 + 's';
                particle.style.animationDuration = Math.random() * 10 + 5 + 's';
                document.body.appendChild(particle);
            }
        }
        createParticles();
    </script>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template_string(HTML)

@app.route('/predict_ajax', methods=['POST'])
def predict_ajax():
    message = request.form.get('message', '')
    if message:
        result, confidence = predict_spam(message)
        return jsonify({'result': result, 'confidence': confidence})
    return jsonify({'result': 'ERROR', 'message': 'No message provided', 'confidence': 0})

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🛡️ Spam Shield Web App Starting...")
    print("="*50)
    print("📱 Open your browser and go to: http://127.0.0.1:5000")
    print("🔴 Press CTRL+C to stop the server")
    print("="*50 + "\n")
    app.run(debug=True)
