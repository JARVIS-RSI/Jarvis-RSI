import json
import os
from datetime import datetime

TASK_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as f:
            return json.load(f)
    return {"active_projects": [], "completed_tasks": [], "deadlines": []}

def save_tasks(data):
    with open(TASK_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def manage_work(command, details):
    tasks = load_tasks()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 1. Naya Project Shuru Karna
    if "new project" in command:
        new_project = {
            "id": len(tasks['active_projects']) + 1,
            "title": details,
            "start_date": timestamp,
            "status": "In Progress"
        }
        tasks['active_projects'].append(new_project)
        save_tasks(tasks)
        return f"Sohail bhai, naya project '{details}' register kar lia gaya hai. Kaam shuru karein!"

    # 2. Task Mukammal Karna
    if "task done" in command:
        # Idhar hum list check kar ke task move karein ge
        return "Sohail bhai, main is task ko completed list mein daal raha hoon."

    return None
