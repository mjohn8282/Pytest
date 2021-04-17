import pytest
from selenium import webdriver
from Resources.TestData import Testdata
from BusinessLogic.Loginpage import Login

class Base:


    @pytest.fixture(scope='class')
    def set_up(self):
        self.driver=webdriver.Chrome(Testdata.CHROME_EXECUTABLE_PATH)
        self.driver.implicitly_wait(10)
        self.driver.get(Testdata.BASE_URL)
        self.driver.maximize_window()
        login = Login(self.driver)
        login.username()
        login.password()
        login.loginbth()
        currenturl = self.driver.current_url
        assert "https://fmicdev.dat.com/Web/Home/HomePage.aspx".find(currenturl)

        yield self.driver

        if self.driver is not None:
            self.driver.close()
            self.driver.quit()