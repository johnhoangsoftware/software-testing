import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def inputUserName(self, username):
    pass


class StepLogin:
    def __init__(self, driver):
        self.driver = driver

    # flow control: nhập username → nhập password → nhấn nút login.
    def login(self, username, password):
        print("[Step] Login")
        self.input_user_name(username)
        time.sleep(2)
        self.input_password(password)
        time.sleep(2)
        self.click_button_login()

    # Action
    def input_user_name(self, email):
        print("[+] Input username")
        self.get_textfield_username().send_keys(email)

    def input_password(self, password):
        print("[+] Input password")
        self.get_textfield_password().send_keys(password)

    def click_button_login(self):
        print("[+] Click button login")
        self.get_textfield_password().send_keys(Keys.ENTER)

    # Get element
    def get_textfield_username(self):
        return self.driver.find_element(By.ID, 'email')

    def get_textfield_password(self):
        return self.driver.find_element(By.ID, 'pass')
