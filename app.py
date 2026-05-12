import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Aapki mazboot API Key
API_KEY = "AIzaSyCjIAfPjWKu5iPvwC50aLSDK-AcAAt2bSw"

# Official Google AI Setup
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        user_input = request.json.get("message", "")
        if not user_input:
            return jsonify({"reply": "Sohail bhai, kuch to likhein..."})
        
        # Direct connection to Google's brain
        response = model.generate_content(user_input)
        return jsonify({"reply": response.text})
        
    except Exception as e:
        # Agar koi masla ho to real error bataye ga
        return jsonify({"reply": f"Jarvis: Connection mein masla hai. Error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
