def change_look(theme_name):
    """Jarvis ka huliya badalna (Dark Mode, Blue Mode etc)"""
    themes = {
        "dark": {"bg": "#000", "text": "#fff"},
        "neon": {"bg": "#0f0", "text": "#000"}
    }
    # Ye settings memory.json mein save hon gi
    return f"Sohail bhai, naya '{theme_name}' theme apply ho gaya hai."
