from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class JarvisHands:
    def __init__(self):
        self.driver = None

    def activate_fingers(self):
        """Browser open karne aur ungliyan tayyar karne ka amal"""
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless") # Agar back-end pe chalana ho to ye on karein
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()

    def open_website(self, url):
        """Kisi bhi website ko open karna"""
        if not self.driver: self.activate_fingers()
        self.driver.get(url)
        return f"Sohail bhai, {url} open ho chuki hai."

    def auto_login_vercel(self, email, password):
        """Vercel par account handling ka amal"""
        self.driver.get("https://vercel.com/login")
        time.sleep(2)
        # Yahan hum mazeed automation steps add karein ge
        return "Vercel login page par pahunch gaya hoon."

    def search_and_act(self, query):
        """Google par search kar ke results nikalna"""
        self.driver.get("https://www.google.com")
        search = self.driver.find_element(By.NAME, "q")
        search.send_keys(query)
        search.send_keys(Keys.RETURN)
        time.sleep(2)
        return f"Sohail bhai, maine '{query}' ke liye research shuru kar di hai."

    def close_browser(self):
        if self.driver:
            self.driver.quit()
