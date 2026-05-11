import requests
from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

# Aapki API Key
API_KEY = "AIzaSyB7TkosMYIR-lcutULeWpdlufAeVkJP6ZI"
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get("message", "")
    # Multiple endpoints taakay ek band ho to doosra chalay
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
    
    headers = {'Content-Type': 'application/json'}
    payload = {"contents": [{"parts": [{"text": user_input}]}]}

    # Retry mechanism: 3 baar koshish karega agar error aaye
    for i in range(3):
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=15)
            if response.status_code == 200:
                data = response.json()
                return jsonify({"reply": data['candidates'][0]['content']['parts'][0]['text']})
            else:
                # Agar Google error de, to thora intezar kar ke dubara try karein
                time.sleep(2)
        except Exception as e:
            # Agar network fail ho, tab bhi try karein
            if i == 2:
                return jsonify({"reply": f"Jarvis: Connection unsafe hai. Error: {str(e)}"})
            time.sleep(2)

    return jsonify({"reply": "Jarvis: Google is not responding. Check VPN Location."})

if __name__ == '__main__':
    app.run(debug=True, port=5000)