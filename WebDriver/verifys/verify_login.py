from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import get_xpath_button_profile
from pages.login_page import get_id_username
import time

#from pages.Page_login import msg_result


class VerifyLogin:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.waitLoginFinish()
        page_name = self.waitLoginFinish()

        return page_name

    # Get element
    def waitLoginFinish(self):
        print("[+] Wait login finish")
        time.sleep(10)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, get_xpath_button_profile())) or 
                                            EC.presence_of_element_located(By.ID, get_id_username()))
        if self.driver.find_element(By.ID, get_id_username()) :
            return "Login Page"
        elif self.driver.find_element(By.XPATH, get_xpath_button_profile()) :
            return "Home Page"
        else :
            return "Error"