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
    user_input_lower = user_input.lower()
    
    # 1. Automatic Chat Logger (Har baat save hogi)
    memory['chat_history'].append({"time": timestamp, "text": user_input})
    
    # 2. Memory Retrieval (Purani baaton ka tajziya)
    # Agar aap puchen ge "kya yaad hai", to wo history check kare ga
    if "kya yaad hai" in user_input_lower or "check history" in user_input_lower:
        if memory['important_reminders']:
            last_note = memory['important_reminders'][-1]['note']
            return f"Sohail bhai, mujhe yaad hai aapne kaha tha: '{last_note}'"
        return "Sohail bhai, abhi tak koi important note save nahi hua."

    # 3. Smart Category Sorting
    if "important" in user_input_lower or "yaad rakhna" in user_input_lower:
        memory['important_reminders'].append({"time": timestamp, "note": user_input})
        save_memory(memory)
        return "Sohail bhai, maine ye point 'Important' category mein save kar liya hai."

    if "online kaam" in user_input_lower or "project" in user_input_lower:
        memory['online_projects'].append({"time": timestamp, "detail": user_input})
        save_memory(memory)
        return "Sohail bhai, project details update ho gayi hain. Main iska record rakh raha hoon."

    # 4. Contextual Awareness (Aapki profile se jawab dena)
    if any(word in user_input_lower for word in ["kon hon main", "mera naam"]):
        name = memory['personal_profile']['name']
        return f"Aap {name} hain, Raja Nazakat Ali ke sahabzade. Aap 25 saal ke hain aur 5 saal ka tajurba rakhte hain."

    # Final save to keep history updated
    save_memory(memory)
    return None
