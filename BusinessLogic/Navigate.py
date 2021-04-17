from selenium.webdriver.common.by import By
from Resources.Locators import Locators
from Resources.TestData import Testdata

class Navigate:

    def __init__(self,driver):
        self.driver=driver

    def RTEstimator(self,modelgroup):
        self.driver.find_element(*Locators.RTEstimator).click()
        self.driver.find_element(*Locators.RTdropdown).click()
        for i in  modelgroup:
          text=  self.driver.find_element(By.XPATH,'//div[@id="ctl00_ContentPlaceHolderBody_ddlPeriod"]/div/table/tbody/tr[@class="GridRow"]['+str(i)+']/td[3]').text
          print(text)
          if text==modelgroup:
              self.driver.find_element(By.XPATH,'//div[@id="ctl00_ContentPlaceHolderBody_ddlPeriod"]/div/table/tbody/tr[@class="GridRow"]['+str(i)+']/td[3]').click()
              break




