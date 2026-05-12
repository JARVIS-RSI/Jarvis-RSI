import requests

def analyze_crypto(coin_symbol="SOL"):
    """Sohail bhai, ye function market se live rate uthaye ga aur mashwara de ga"""
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin_symbol}USDT"
    try:
        response = requests.get(url)
        data = response.json()
        price = float(data['price'])
        
        # Logic: Agar price aik khaas limit se neechay ho to alert dena
        if coin_symbol == "SOL" and price < 130:
            return f"Sohail bhai, Solana {price} par aa gaya hai. Loss se bachne ke liye abhi sell na karein ya hold rakhein."
        return f"Sohail bhai, {coin_symbol} ki price abhi {price} hai. Market stable lag rahi hai."
    except:
        return "Sohail bhai, market data nahi mil raha. Internet check karein."
