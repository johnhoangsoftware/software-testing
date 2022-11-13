import selenium
import HtmlTestRunner
import unittest, time

class NewTest(unittest.TestCase):
    def setUp(self):
        print("========== [Begin Test] ==========")
        

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://www.google.com/")
        self.selenium.start()
    
    def test_new(self):
        sel = self.selenium
        sel.open("/")
        sel.type("q", "selenium rc")
        sel.click("btnG")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_text_present("Results * for selenium rc"))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)
        print("========== [ End Test ] ========== \n")

if __name__ == '__main__':
    unittest.main()#testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports'))