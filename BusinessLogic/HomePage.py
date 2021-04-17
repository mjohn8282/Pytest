from selenium.webdriver.common.by import By
from Resources.Locators import Locators
from Resources.TestData import Testdata

class Home:

    def __init__(self,driver):
        self.driver=driver

    def ishomepage(self):
        return self.driver.find_element(By.ID,Locators.Welcome).text

    def RTEstimator(self):
        self.driver.find_element(By.XPATH,Locators.RTEstimator).click()

    def estimatordrpdown(self):
        self.driver.find_element(By.ID,Locators.dropdown).click()
