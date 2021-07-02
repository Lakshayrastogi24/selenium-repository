import unittest
from pagess.home.login_page import LoginPage
import pytest
from utilities.test_status import TestStatus
from pagess.navigation_page import NavigationPage

@pytest.mark.usefixtures('oneTimeSetUp','setUp')
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self,oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts=TestStatus(self.driver)
        self.np=NavigationPage(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        print('valid')
        result1=self.lp.verifyTitle()
        self.ts.mark(result1,'title verified')
        self.lp.login('lakshrstg@gmail.com','123456')
        result2 =self.lp.verifyLoginSuccessful()
        self.ts.markFinal('Verify valid login',result2, 'login successful')


    @pytest.mark.run(order=1)
    def test_inValidLogin(self):
        self.np.navigateToUserSettings()
        print('invalid')
        self.lp.login('lakshrstg@gmail.com', '123456123456')
        result = self.lp.verifyLoginFailed()
        assert result == True




