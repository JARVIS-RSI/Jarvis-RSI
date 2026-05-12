from selenium.webdriver.common.by import By
import time

def facebook_comment(driver, post_url, comment_text):
    """Sohail bhai, ye function khud FB post par ja kar comment likhay ga"""
    driver.get(post_url)
    time.sleep(5) # Page load hone ka waqt
    try:
        # Comment box dhoondna (Ye FB ke update ke mutabiq change ho sakta hai)
        comment_box = driver.find_element(By.XPATH, '//div[@role="textbox"]')
        comment_box.send_keys(comment_text)
        comment_box.send_keys("\n") # Enter dabana
        return "Sohail bhai, comment kar dia hai!"
    except:
        return "Sohail bhai, Facebook par comment box nahi mila."

def auto_scroll(driver):
    """Web page ko khud ba khud scroll karna"""
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    return "Sohail bhai, page scroll ho raha hai."
