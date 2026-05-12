import webbrowser
import os
import subprocess

def execute_command(command):
    command = command.lower()

    # 1. Website Opening (Vercel, WhatsApp, etc.)
    if "open vercel" in command:
        webbrowser.open("https://vercel.com")
        return "Sohail bhai, Vercel open kar dia hai. Main online hoon aur project monitor kar raha hoon."

    if "open whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com")
        return "WhatsApp open ho raha hai. Kis ko message bhejna hai?"

    # 2. System Settings (Basic Control)
    if "shutdown computer" in command:
        # os.system("shutdown /s /t 1") # Ye line computer band kar degi
        return "Sohail bhai, kya aap waqai system band karna chahte hain?"

    # 3. Running Projects
    if "run project" in command or "deploy" in command:
        return "Sohail bhai, main deployment scripts check kar raha hoon. Build process shuru hai."

    return None
