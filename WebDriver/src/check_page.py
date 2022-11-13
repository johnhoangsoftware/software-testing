from selenium.webdriver.common.by import By
import time

from element import get_xpath_button_profile, get_id_username


class CheckPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        page_name = self.waitLoginFinish()

        return page_name

    # Get element
    def waitLoginFinish(self):
        print("[+] Wait login finish")
        time.sleep(15)
        try:
            self.driver.find_element(By.ID, get_id_username())
            return "Login Page"
        except:
            try:
                self.driver.find_element(By.XPATH, get_xpath_button_profile())
                return "Home Page"
            except:
                return "Error"
