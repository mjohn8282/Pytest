# import sys, os
# myPath = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, myPath + '/../')

from BusinessLogic import Loginpage,HomePage
from Base.BaseClass import Base


import pytest


@pytest.mark.usefixtures('set_up')
class Test_Login(Base):

    @pytest.fixture(autouse=True)
    def setup(self,set_up):
        self.driver=set_up


    def test_loginsucess(self):
        driver=self.driver
        login=Loginpage.Login(driver)
        login.username()
        login.password()
        login.loginbth()
        currenturl=driver.current_url
        assert "https://fmicdev.dat.com/Web/Home/HomePage.aspx".find(currenturl)

    def test_RTEstimator(self):
        home=HomePage.Home(self.driver)
        home.RTEstimator()
        home.estimatordrpdown()

    # def test_RTEstimator(self):
    #     self.driver.find_element(By.ID,)