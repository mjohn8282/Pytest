import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from BusinessLogic import HomePage
from Base.BaseClass import Base

import pytest


@pytest.mark.usefixtures('set_up')
class Test_Home(Base):

    def test_RT(self):
        driver= self.driver
        Home=HomePage.Home(driver)
        Home.RTEstimator()
        Home.estimatordrpdown()