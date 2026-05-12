import requests
from flask import Flask, render_template, request, jsonify
import json
try:
    import brain
    USE_BRAIN = True
except:
    USE_BRAIN = False
app = Flask(__name__)

# Aapki New API Key jo aapne abhi banai hai
API_KEY = "AIzaSyCjIAfPjWKu5iPvwC50aLSDK-AcAAt2bSw"

def get_latest_model():
    # Ye function check karega ke kon sa model available hai
    url = f"https://generativelanguage.googleapis.com/v1/models?key={API_KEY}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            models = response.json().get('models', [])
            for m in models:
                if 'generateContent' in m.get('supportedGenerationMethods', []):
                    return m['name']
        return "models/gemini-pro"
    except:
        return "models/gemini-pro"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get("message", "")
    # Check if brain.py has something special to say
    if USE_BRAIN:
        try:
            advanced_reply = brain.process_logic(user_input)
            if advanced_reply:
                return jsonify({"reply": advanced_reply})
        except:
            pass # Agar brain.py mein error ho, to purana code chalne do
    # Active model ka sahi naam hasil karna
    active_model = get_latest_model()
    
    # Paka aur purana URL jo pehle kaam kar raha tha
    url = f"https://generativelanguage.googleapis.com/v1/{active_model}:generateContent?key={API_KEY}"
    
    headers = {'Content-Type': 'application/json'}
    payload = {"contents": [{"parts": [{"text": user_input}]}]}

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=30)
        if response.status_code == 200:
            data = response.json()
            return jsonify({"reply": data['candidates'][0]['content']['parts'][0]['text']})
        else:
            return jsonify({"reply": f"Jarvis: Google is checking the model. Please try again in a moment. (Code: {response.status_code})"})
    except Exception as e:
        return jsonify({"reply": f"Network Error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
