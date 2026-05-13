import google.generativeai as genai
import json
import os
from datetime import datetime

MEMORY_FILE = 'memory.json'

# 1. Purani Yaad-dash load karna (Sohail bhai ka purana logic)
def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r') as f:
            return json.load(f)
    return {
        "personal_profile": {"name": "Raja Sohail Imran", "age": 25, "father": "Raja Nazakat Ali", "exp": "5 years"},
        "chat_history": []
    }

# 2. Dunya ka har ilm (Google AI Setup)
def setup_ai():
    # Secrets.json se key uthana
    with open('secrets.json', 'r') as f:
        secrets = json.load(f)
        genai.configure(api_key=secrets['GEMINI_API_KEY'])
    return genai.GenerativeModel('gemini-1.5-flash')

# 3. Super Brain Function (Tez Damagh)
def get_jarvis_response(user_input):
    memory = load_memory()
    model = setup_ai()
    
    # Sohail bhai ki profile ka context taake Jarvis ko pata ho wo kisse baat kar raha hai
    context = f"Aapka naam JARVIS hai. Aap Raja Sohail Imran ke assistant hain. " \
              f"Unka 5 saal ka experience sales aur furniture packing mein hai. " \
              f"Wo Wah Cantt/Taxila mein rehte hain. Ab is sawal ka jawab dunya ki har khabar ke mutabiq den: {user_input}"

    try:
        # AI se jawab mangna
        response = model.generate_content(context)
        final_answer = response.text
        
        # Yaad-dash mein save karna
        memory['chat_history'].append({"time": str(datetime.now()), "user": user_input, "jarvis": final_answer})
        with open(MEMORY_FILE, 'w') as f:
            json.dump(memory, f, indent=4)
            
        return final_answer
    except Exception as e:
        return f"Sohail Bhai, damagh connect karne mein masla aa raha hai: {e}"
