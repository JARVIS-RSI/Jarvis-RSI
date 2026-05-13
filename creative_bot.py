import pyautogui
import time

def start_designing(platform):
    if "canva" in platform.lower():
        pyautogui.press('win')
        pyautogui.write('chrome')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.write('https://www.canva.com')
        pyautogui.press('enter')
        return "Sohail bhai, Canva open ho raha hai."
    return "Platform not supported yet."
