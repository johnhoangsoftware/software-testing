import time

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import unittest
# Run server
#java -jar selenium-server-4.6.0.jar standalone

class TestLogin(unittest.TestCase):

    @classmethod
    def setUp(cls):
        print("========== [Begin Test] ==========")
        f = open('data_test', 'r')
        cls.data_test = f.read().split('\n')
        f.close()
        options = Options()
        options.add_argument("--disable-notifications")
        cls.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            # desired_capabilities=DesiredCapabilities.CHROME
            options=options
            # desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True}
        )

    def test0(self):
        print("========== [Run Test] ==========")
        data = self.data_test[0].split('|')

        username = data[1]
        password = data[2]
        driver = self.driver
        driver.get("https://facebook.com")
        assert "Facebook" in driver.title
        un = driver.find_element(By.ID, "email")
        un.send_keys(username)
        pw = driver.find_element(By.ID, "pass")
        pw.send_keys(password)
        pw.send_keys(Keys.ENTER)
        time.sleep(7)
        assert "No results found." not in driver.page_source

    def test1(self):
        print("========== [Run Test] ==========")
        data = self.data_test[1].split('|')

        username = data[1]
        password = data[2]
        driver = self.driver
        driver.get("https://facebook.com")
        assert "Facebook" in driver.title
        un = driver.find_element(By.ID, "email")
        un.send_keys(username)
        pw = driver.find_element(By.ID, "pass")
        pw.send_keys(password)
        pw.send_keys(Keys.ENTER)
        time.sleep(7)
        assert "No results found." not in driver.page_source

    def test2(self):
        print("========== [Run Test] ==========")
        data = self.data_test[2].split('|')

        username = data[1]
        password = data[2]
        driver = self.driver
        driver.get("https://facebook.com")
        assert "Facebook" in driver.title
        un = driver.find_element(By.ID, "email")
        un.send_keys(username)
        pw = driver.find_element(By.ID, "pass")
        pw.send_keys(password)
        pw.send_keys(Keys.ENTER)
        time.sleep(7)
        assert "No results found." not in driver.page_source

    def test3(self):
        print("========== [Run Test] ==========")
        data = self.data_test[3].split('|')

        username = data[1]
        password = data[2]
        driver = self.driver
        driver.get("https://facebook.com")
        assert "Facebook" in driver.title
        un = driver.find_element(By.ID, "email")
        un.send_keys(username)
        pw = driver.find_element(By.ID, "pass")
        pw.send_keys(password)
        pw.send_keys(Keys.ENTER)
        time.sleep(5)
        assert "No results found." not in driver.page_source

    def test4(self):
        print("========== [Run Test] ==========")
        data = self.data_test[4].split('|')

        username = data[1]
        password = data[2]
        driver = self.driver
        driver.get("https://facebook.com")
        assert "Facebook" in driver.title
        un = driver.find_element(By.ID, "email")
        un.send_keys(username)
        pw = driver.find_element(By.ID, "pass")
        pw.send_keys(password)
        pw.send_keys(Keys.ENTER)
        time.sleep(5)
        assert "No results found." not in driver.page_source

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        print("========== [ End Test ] ========== \n")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:/Study/KiemThu/software-testing/RC/reports'))
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports'))

    # element = driver.find_element_by_id("passwd-id")
    # element = driver.find_element_by_name("passwd")
    # element = driver.find_element_by_xpath("//input[@id='passwd-id']")
