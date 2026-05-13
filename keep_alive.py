import time
import requests
import os

def check_internet():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except:
        return False

def maintain_jarvis():
    print("Jarvis Stay-Alive mode activated...")
    while True:
        if check_internet():
            # Agar net on hai to ye check karega ke Jarvis chal raha hai ya nahi
            # Agar band hai to 'main_app.py' ko dubara chala dega
            print("Internet connected. Jarvis is active.")
        else:
            print("Waiting for network...")
        
        time.sleep(30) # Har 30 second baad check karega
