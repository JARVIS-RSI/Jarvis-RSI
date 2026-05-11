import os
import requests
from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

# اب یہ ورسل کی سیٹنگز سے چابی اٹھائے گا
API_KEY = os.getenv("GOOGLE_API_KEY")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get("message", "")
    
    # اگر چابی نہ ملے تو یہ میسج دکھائے گا
    if not API_KEY:
        return jsonify({"reply": "Jarvis Error: API Key missing in Vercel settings."})

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
    
    headers = {'Content-Type': 'application/json'}
    payload = {"contents": [{"parts": [{"text": user_input}]}]}

    for i in range(3):
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=15)
            if response.status_code == 200:
                data = response.json()
                return jsonify({"reply": data['candidates'][0]['content']['parts'][0]['text']})
            else:
                time.sleep(2)
        except Exception as e:
            if i == 2:
                return jsonify({"reply": f"Jarvis: Connection issue. Error: {str(e)}"})
            time.sleep(2)

    return jsonify({"reply": "Jarvis: Google is not responding. Check VPN Location or API Key."})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
