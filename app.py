import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# آپ کی نئی اے پی آئی کی
API_KEY = "AIzaSyCp6mzAf3xj2pMCnl11CWCoEQDWE5SQaPM"
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
            return jsonify({"reply": "کچھ تو لکھیں..."})
        
        response = model.generate_content(user_input)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"Jarvis: ابھی رابطہ نہیں ہو پا رہا۔ وجہ: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
