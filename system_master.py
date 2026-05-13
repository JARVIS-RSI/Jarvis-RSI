import os
import ctypes
import subprocess

def system_action(task):
    task = task.lower()
    if "lock" in task:
        ctypes.windll.user32.LockWorkStation()
        return "System Locked."
    if "shutdown" in task:
        os.system("shutdown /s /t 5")
        return "Shutting down in 5 seconds."
    if "wifi" in task:
        subprocess.run("control netconnections")
        return "Opening Network Settings."
    return "Task not recognized."
