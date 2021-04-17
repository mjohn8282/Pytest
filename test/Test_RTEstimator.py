import time

from  Base.BaseClass import Base
from BusinessLogic.Navigate import Navigate
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures('setup')
class Test_RTEstimator(Base):

    @pytest.fixture(autouse=True)
    def setup(self,set_up):
        self.driver=set_up

    def test_3PLRTEstimator(self):
        navigate=Navigate(self.driver)
        RTestimators=('LTL','3PL Truckload','FMIC Truckload')
        for i in RTestimators:
            navigate.RTEstimator(i)
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located())

    # def test_3PLRTEstimator(self):
    #     navigate=Navigate(self.driver)
    #     navigate.RTEstimator('3PL Truckload')