from Base.BaseClass import Base
import  pytest
from BusinessLogic.Navigate import Navigate
from Resources.Locators import  Locators

@pytest.mark.usefixtures('set_up')
class Test_Navigate(Base):

    @pytest.fixture(autouse=True)
    def setup(self,set_up):
        self.driver=set_up

    def test_NavRTEstimator(self,modelgroup):
        navigate=Navigate(self.driver)
        navigate.RTEstimator(modelgroup)



