def ecom_action(platform, task):
    """Amazon aur Shopify par kaam karna"""
    if platform == "amazon":
        # Yahan hum Selenium use kar ke Amazon seller central pe jayen ge
        return f"Sohail bhai, Amazon par {task} ka kaam shuru kar dia hai."
    elif platform == "shopify":
        return f"Sohail bhai, Shopify store ki inventory check ho rahi hai."
    return "Platform samajh nahi aaya."
