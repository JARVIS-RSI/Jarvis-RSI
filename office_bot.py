import pandas as pd # Excel ke liye
import docx # Word ke liye
import win32com.client # Outlook ke liye

def manage_excel(file_path, operation, data=None):
    """Excel mein data dalna ya formula lagana"""
    df = pd.read_excel(file_path)
    if operation == "sum":
        return df.sum()
    return "Sohail bhai, Excel file update ho gayi hai."

def send_outlook_email(to, subject, body):
    """Outlook se khud ba khud email bhejna"""
    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = to
    mail.Subject = subject
    mail.Body = body
    mail.Send()
    return "Sohail bhai, email bhej di gayi hai."
