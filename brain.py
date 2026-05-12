CORE_DATA = {
    "name": "Jarvis-RSI",
    "owner": "Raja Sohail Imran",
    "age": 25,
    "mission": "Solar & Furniture Business Growth",
    "status": "Active"
}

def process_logic(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["kon ho", "intro", "shanakht"]):
        return f"Sohail bhai, main aapka Jarvis hoon. Raja Nazakat Ali ka beta aur 25 saal ka jawan mehnat kash insaan, Raja Sohail Imran, mera maalik hai. Mera maqsad aapke Solar aur Furniture business ko scale karna hai."

    if "yaad rakhna" in user_input or "note kar lo" in user_input:
        return "Sohail bhai, maine ye baat zehan nasheen kar li hai. Main ise memory file mein save kar raha hoon."

    if "solar" in user_input:
        return "Solar business ke liye net metering aur panel rates ki monitoring zaroori hai. Sohail bhai, aapka 5 saal ka experience inventory management mein yahan kaam aaye ga."

    if "furniture" in user_input and "china" in user_input:
        return "China (Guangdong) se modern furniture sourcing ke liye humein logistics aur container costs ka purana data check karna chahiye."

    if "faisla" in user_input or "mashwara" in user_input:
        return "Sohail bhai, data ke mutabiq aapko scalability par focus karna chahiye. Business ko automate karna hi agla step hai."

    return None
