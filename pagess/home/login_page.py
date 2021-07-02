from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from utilities.custom_logger import customLogger
import time

class LoginPage(SeleniumDriver):
    lo = customLogger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _sign = '//a[contains(@href,"login")]'
    _email = 'email'
    _password = 'password'
    _login_btn = '.btn.btn-default.btn-block.btn-md.dynamic-button'

    def clickSignIn(self):
        self.elementClick(self._sign, 'XPATH')

    def enterEmail(self, username):
        self.sendKeys(username, self._email)

    def enterPassword(self, password):
        self.sendKeys(password, self._password)

    def clickLoginBtn(self):
        self.elementClick(self._login_btn, 'css')

    def login(self, usnm, pswd):
        time.sleep(2)
        self.clickSignIn()
        self.clearFields()
        self.enterEmail(usnm)
        self.enterPassword(pswd)
        self.clickLoginBtn()

    def verifyLoginSuccessful(self):
        res = self.isElementPresent( 'search','name')
        return res

    def verifyLoginFailed(self):
        res=self.isElementPresent('//span[contains(text(),"Your username or password is invalid. Please try again.")]','xpath')
        return res

    def clearFields(self):
        ele1=self.getElement(self._email)
        ele1.clear()
        ele2=self.getElement(self._password)
        ele2.clear()

    def verifyTitle(self):
        if 'Login' in self.getTitle():
            return True
        else:
            return False


