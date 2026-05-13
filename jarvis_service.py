import time
import socket
import subprocess

def keep_connected():
    """Sohail bhai, ye function net on hotay hi Jarvis ko jaga dega"""
    remote_server = "www.google.com"
    while True:
        try:
            # Check karna ke internet hai ya nahi
            host = socket.gethostbyname(remote_server)
            s = socket.create_connection((host, 80), 2)
            print("◎ JARVIS: Online aur Connected hai!")
            # Yahan wo code chalega jo Jarvis ko active rakhta hai
            time.sleep(60) # Har minute baad check karein
        except:
            print("◎ JARVIS: Connection toot gaya, dubara koshish jari hai...")
            time.sleep(5) # 5 second baad dubara connect karne ki koshish

if __name__ == "__main__":
    keep_connected()
