from voice_engine import speak, listen
from brain import process_logic
from fingers import JarvisHands
from market_brain import analyze_crypto
import sys

def start_jarvis():
    hands = JarvisHands()
    speak("Sohail bhai, main active hoon. Kya hukum hai?")

    while True:
        query = listen()
        
        if not query:
            continue

        # 1. Binaice/Crypto ka hukum
        if "crypto" in query or "price" in query:
            speak("Checking market, Sohail bhai...")
            status = analyze_crypto("SOL")
            speak(status)

        # 2. Browser/Vercel ka hukum
        elif "open" in query:
            speak("Ji Sohail bhai, abhi kholta hoon.")
            hands.activate_fingers()
            if "vercel" in query:
                hands.open_website("https://vercel.com")
            elif "facebook" in query:
                hands.open_website("https://facebook.com")

        # 3. Dimagh (Brain.py) se mashwara
        else:
            response = process_logic(query)
            if response:
                speak(response)
            else:
                speak("Sohail bhai, is par main ghor kar raha hoon.")

        # Exit Command
        if "sleep" in query or "off" in query:
            speak("Allah Hafiz Sohail bhai, apna khyal rakhiye ga.")
            hands.close_browser()
            sys.exit()

if __name__ == "__main__":
    start_jarvis()
