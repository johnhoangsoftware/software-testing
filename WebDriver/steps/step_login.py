from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.login_page import get_id_username, get_id_password

class StepLogin:
    def __init__(self, driver):
        self.driver = driver

    # flow control: nhập username → nhập password → nhấn nút login.
    def login(self, username, password):
        print("[Step] Login")
        self.inputUserName(username)
        self.inputPassword(password)
        self.clickButtonLogin()

    # Action
    def inputUserName(self, email):
        print("[+] Input username")
        self.get_textfield_username().send_keys(email)

    def inputPassword(self, password):
        print("[+] Input password")
        self.get_textfield_password().send_keys(password)

    def clickButtonLogin(self):
        print("[+] Click button login")
        self.get_textfield_password().send_keys(Keys.ENTER)

    # Get element
    def get_textfield_username(self):
        return self.driver.find_element(By.ID, get_id_username())

    def get_textfield_password(self):
        return self.driver.find_element(By.ID, get_id_password())