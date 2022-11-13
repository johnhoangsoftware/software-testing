import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import unittest


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        print("========== [Begin Test] ==========")
        options = Options()
        options.add_argument("--disable-notifications")
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            #desired_capabilities=DesiredCapabilities.CHROME
            options= options
            # desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True}
            )

        
    
    def test_new(self):
        print("========== [Run Test] ==========")
        driver = self.driver
        driver.get("https://facebook.com")
        assert "Facebook" in driver.title
        username = driver.find_element(By.ID, "email")
        username.send_keys("0904838631")
        password = driver.find_element(By.ID, "pass")
        password.send_keys("")
        password.send_keys(Keys.ENTER)
        time.sleep(10)
        assert "No results found." not in driver.page_source
            
    def tearDown(self):
        self.driver.close()
        print("========== [ End Test ] ========== \n")

if __name__ == '__main__':
    unittest.main()

