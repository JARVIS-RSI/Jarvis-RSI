import json
import os
from datetime import datetime

MEMORY_FILE = 'memory.json'

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_memory(data):
    with open(MEMORY_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def process_logic(user_input):
    memory = load_memory()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 1. Chat History Save Karna
    chat_entry = {"time": timestamp, "user": user_input}
    memory['chat_history'].append(chat_entry)
    
    user_input_lower = user_input.lower()

    # 2. Important Notes & Reminders
    if "important" in user_input_lower or "yaad rakhna" in user_input_lower:
        memory['important_reminders'].append({"time": timestamp, "note": user_input})
        save_memory(memory)
        return "Sohail bhai, maine ye important baat note kar li hai aur history mein bhi daal di hai."

    # 3. Online Work Details
    if "online kaam" in user_input_lower or "project update" in user_input_lower:
        memory['online_projects'].append({"time": timestamp, "detail": user_input})
        save_memory(memory)
        return "Sohail bhai, aapke online project ki details update ho gayi hain."

    # Har surat mein memory save karna (History ke liye)
    save_memory(memory)

    # Specific trigger for introduction
    if any(word in user_input_lower for word in ["kon ho", "intro"]):
        return f"Main Jarvis hoon, Sohail bhai. Aapki poori chat history aur online kaam ka record mere paas mahfooz hai."

    return None
