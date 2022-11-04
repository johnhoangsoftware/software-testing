from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import threading
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def main():
    service = Service(executable_path=ChromeDriverManager().install())
    options = Options()
    options.add_argument("--disable-notifications")
    # Step 1) 
    browser = webdriver.Chrome(service=service, options=options)
    # Step 2) Navigate to Facebook
    browser.get("http://www.facebook.com")

    # Step 3) Search & Enter the Email or Phone field & Enter Password
    username = browser.find_element(By.ID,"email")
    time.sleep(1)
    username.send_keys("0904838631")
    time.sleep(1)

    password = browser.find_element(By.ID,"pass")
    password.send_keys("")
    time.sleep(1)

    # Step 4) Click Login
    password.send_keys(Keys.ENTER)
    time.sleep(10)
    
    


    menu = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[2]/div[4]/div[1]/span/div/div[1]")
    menu.click()
    time.sleep(3)
    time.sleep(3)
    browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[5]/div").click()
    time.sleep(3)

    browser.close()


if __name__ == '__main__':
    main()
