import unittest

from check_page import CheckPage
from custom_chrome import custom_chrome
from runner_report import HTMLTestRunner
from step_login import StepLogin




class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("========== [Begin Test] ==========")
        self.browser = custom_chrome()
        self.browser.get("http://www.facebook.com")
        f = open('data_test', 'r')

        self.data_test = f.read().split('\n')
        f.close()

    def tearDown(self):
        self.browser.quit()
        print("========== [ End Test ] ========== \n")

    def test_login_1(self):
        data = self.data_test[0].split('|')

        username = data[1]
        password = data[2]
        expected_output = data[4]

        StepLogin(self.browser).login(username, password)
        result = CheckPage(self.browser).login()
        print(result)
        self.assertEqual(expected_output, result)

    def test_login_2(self):
        data = self.data_test[1].split('|')

        username = data[1]
        password = data[2]
        expected_output = data[4]
        print(expected_output)
        StepLogin(self.browser).login(username, password)
        result = CheckPage(self.browser).login()
        print(result)
        self.assertEqual(expected_output, result)

    def test_login_3(self):
        data = self.data_test[2].split('|')

        username = data[1]
        password = data[2]
        expected_output = data[4]
        print(expected_output)
        StepLogin(self.browser).login(username, password)
        result = CheckPage(self.browser).login()
        print(result)
        self.assertEqual(expected_output, result)

    def test_login_4(self):
        data = self.data_test[3].split('|')

        username = data[1]
        password = data[2]
        expected_output = data[4]
        print(expected_output)
        StepLogin(self.browser).login(username, password)
        result = CheckPage(self.browser).login()
        print(result)
        self.assertEqual(expected_output, result)

    def test_login_5(self):
        data = self.data_test[4].split('|')

        username = data[1]
        password = data[2]
        expected_output = data[4]
        print(expected_output)
        StepLogin(self.browser).login(username, password)
        result = CheckPage(self.browser).login()
        print(result)
        self.assertEqual(expected_output, result)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='./reports'))
