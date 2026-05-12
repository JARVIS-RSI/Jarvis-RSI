import speech_recognition as sr
from gtts import gTTS
import os
import playsound

def speak(text):
    """Sohail bhai, ye function Jarvis ko bolne ki taqat deta hai"""
    print(f"Jarvis: {text}")
    try:
        tts = gTTS(text=text, lang='ur')
        filename = "voice.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)
    except Exception as e:
        print(f"Bolne mein masla hua: {e}")

def listen():
    """Sohail bhai, ye function Jarvis ko aapki baat sunne ke qabil banata hai"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Sunte hain Sohail bhai... (Boliye)")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='ur-PK')
            print(f"Aap ne kaha: {query}")
            return query.lower()
        except sr.UnknownValueError:
            return ""
        except Exception as e:
            print(f"Error: {e}")
            return ""
