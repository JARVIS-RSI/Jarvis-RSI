import tkinter as tk
from gui_app import JarvisFace
from jarvis_service import keep_connected
from system_master import system_action
from smart_filter import extract_specific_data
import threading
import sys

# 1. Background Connection Thread (WhatsApp Style)
def start_background_services():
    """Jarvis ko hamesha connected rakhne ke liye background thread"""
    service_thread = threading.Thread(target=keep_connected, daemon=True)
    service_thread.start()
    print("◎ JARVIS: Background Services Active (Always Connected)")

# 2. Main GUI Launch
def launch_jarvis_ui():
    root = tk.Tk()
    root.title("JARVIS RSI - Version 2.0")
    
    # Screen ke top par rakhne ke liye
    root.attributes("-topmost", True)
    
    # Interface load karna
    app = JarvisFace(root)
    
    print("◎ JARVIS: Interface Loaded. Welcome back, Sohail Bhai!")
    
    # Yahan hum commands ka intezar karenge
    # Example: system_action("lock") ya extract_specific_data("file.xlsx", "Ali")
    
    root.mainloop()

# 3. Main Execution
if __name__ == "__main__":
    try:
        # Pehle background service shuru hogi
        start_background_services()
        
        # Phir Jarvis ka "Face" samne ayega
        launch_jarvis_ui()
        
    except KeyboardInterrupt:
        print("\nSystem shutting down gracefully...")
        sys.exit()
    except Exception as e:
        print(f"Critical Error: {e}")
