from selenium.webdriver import Chrome, Firefox, Ie
from pathlib import Path
import os


class TestAmazonBase:
    def __init__(self, browser):
        self.browser = browser  # chrome, firefox, ie
        self.initialise_driver()
        self.driver.get("https://www.amazon.in")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def initialise_driver(self):
        if self.browser.upper() == "CHROME":
            self.driver = Chrome(str(Path(os.getcwd(),'drivers','chromedriver.exe').absolute()))
        elif self.browser.upper() == "FIREFOX":
            self.driver = Firefox()
        elif self.browser.upper == "IE":
            self.driver = Ie()
        else:
            print("Please enter validbrowser")
