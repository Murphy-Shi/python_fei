from selenium import webdriver

class SelenumUtil:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def stary(self, url: str):
       self.driver.get(url)