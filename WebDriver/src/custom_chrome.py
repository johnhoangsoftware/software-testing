from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# Tuỳ chỉnh profile browser
def custom_chrome():
    service = Service(executable_path=ChromeDriverManager().install())
    options = Options()
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=service, options=options)

    print("[Open browser] Open Google Chrome")
    return driver
