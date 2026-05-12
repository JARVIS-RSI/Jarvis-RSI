import os

def upgrade_code(file_name, new_feature_name, code_content):
    """Sohail bhai, ye function Jarvis ke purane code mein naya feature dalti hai"""
    try:
        # 1. Purani file parhna
        with open(file_name, 'a') as f:
            # 2. Naya code file ke aakhir mein joarna
            f.write(f"\n\n# New Feature Added by Jarvis: {new_feature_name}\n")
            f.write(code_content)
        
        return f"Sohail bhai, '{new_feature_name}' ka code main ne '{file_name}' mein add kar dia hai. System update ke liye tayyar hai."
    except Exception as e:
        return f"Upgrade mein masla hua: {e}"

def search_new_tech(topic):
    """Market mein naye features dhoondna (Future Scope)"""
    return f"Sohail bhai, main ne '{topic}' ke baare mein research kar li hai. Kya main iska code likhna shuru karun?"
