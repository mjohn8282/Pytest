from selenium.webdriver.common.by import By


class Locators():

    i='0'
    #Login Page

    username=(By.ID,'ctl00_ContentPlaceHolderBody_txtUserID')
    password=(By.ID,'ctl00_ContentPlaceHolderBody_txtPassword')
    Submit=(By.ID,'ctl00_ContentPlaceHolderBody_cmdLogin')


    #Homepage
    Welcome=(By.ID,'pHomeWelcome')

    #RTEstimtor
    RTEstimator = (By.XPATH, "//div[@id='divHomeMenu']/div[1]/ul/li[3]/a")
    RTdropdown=(By.ID,'ctl00_ContentPlaceHolderBody_PeriodTextBox')
   # RTLTL=(By.XPATH,'//div[@id="ctl00_ContentPlaceHolderBody_ddlPeriod"]/div/table/tbody/tr[@class="GridRow"]['+i+']/td[3]')