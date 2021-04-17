from selenium.webdriver.common.by import By


from Resources.Locators import Locators
from Resources.TestData import Testdata

class Login:
    def __init__(self,driver):
        self.driver=driver

    def username(self):
        self.driver.find_element(*Locators.username).send_keys(Testdata.username)
    def password(self):
        self.driver.find_element(*Locators.password).send_keys(Testdata.password)
    def loginbth(self):
        self.driver.find_element(*Locators.Submit).click()








