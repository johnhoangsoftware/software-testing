import unittest
import HtmlTestRunner

from parameterized import parameterized
from steps.read_data_test import ReadDataTest
from steps.step_login import StepLogin
from verifys.verify_login import VerifyLogin
from utils.custom_chrome_driver import custom_chrome

dataTests = ReadDataTest().data_test_login()


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("========== [Begin Test] ==========")
        self.browser = custom_chrome()
        self.browser.get("http://www.facebook.com")

    def tearDown(self):
        self.browser.quit()
        print("========== [ End Test ] ========== \n")

    @parameterized.expand(dataTests)
    def test_login(self, no, username, password, desiredResult, pageName):
        StepLogin(self.browser).login(username, password)
        self.assertIn(pageName, VerifyLogin(self.browser).login())


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports'))