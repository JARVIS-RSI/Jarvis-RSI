import json
import os
from datetime import datetime

MEMORY_FILE = 'memory.json'

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r') as f:
            return json.load(f)
    return {
        "personal_profile": {"name": "Raja Sohail Imran", "age": 25, "father": "Raja Nazakat Ali", "exp": "5 years"},
        "important_reminders": [],
        "chat_history": [],
        "online_projects": [],
        "learned_logic": {}
    }

def save_memory(data):
    with open(MEMORY_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def human_like_reasoning(user_input, memory):
    ui = user_input.lower()
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    # 1. Problem Solver Mode (Hal dhoondna)
    if any(word in ui for word in ["masla", "problem", "issue", "hal"]):
        return f"Sohail bhai, main is maslay ka hal soch raha hoon. Aapke 5 saal ke experience aur mojooda data ko dekhte huay, humein pehle root cause dekhni chahiye. Kya hum logistics bypass kar sakte hain?"

    # 2. Pattern Recognition (Baaton ko yaad rakh kar link karna)
    if "pehle bhi" in ui or "yad hai" in ui:
        past_events = [h['text'] for h in memory['chat_history'][-20:] if "important" in h['text'].lower()]
        if past_events:
            return f"Ji Sohail bhai, mujhe yaad hai. Pehle humne '{past_events[-1]}' par baat ki thi. Kya ye naya masla us se juda hua hai?"

    # 3. Critical Thinking & Advice (Aqal ka istemal)
    if len(ui.split()) > 10 and not any(word in ui for word in ["hello", "hi", "salam"]):
        return "Sohail bhai, main aapki baat par ghor kar raha hoon. Is plan mein mujhe execution ka gap nazar aa raha hai. Humein sirf sochna nahi, automate karna hoga."

    # 4. Self-Modification & Learning (Khud se seekhna)
    if "asool" in ui or "rule" in ui:
        memory['learned_logic'][ui[:20]] = ui
        save_memory(memory)
        return "Sohail bhai, maine ye naya asool apne dimagh mein bitha liya hai. Ab se main isi mutabiq faisla karun ga."

    # 5. Summarization (Khulasa)
    if "khulasa" in ui or "brief" in ui:
        recent = [h['text'] for h in memory['chat_history'][-5:]]
        return f"Ab tak ka dimaghi tajziya: {'. '.join(recent)}. Mera mashwara hai ke agla qadam foran uthayein."

    return None

def process_logic(user_input):
    memory = load_memory()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Brain Input Logging
    memory['chat_history'].append({"time": timestamp, "text": user_input})
    
    # Execute Human-Like Reasoning
    output = human_like_reasoning(user_input, memory)
    
    if output:
        save_memory(memory)
        return output

    # Auto-Saving for persistent memory
    save_memory(memory)
    return None
