from base.selenium_driver import SeleniumDriver
import time
from utilities.custom_logger import customLogger


class CarddetailsPage(SeleniumDriver):
    losd=customLogger()
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver


    #locators
    _card_number='//div/span/input[@name="cardnumber"]'
    _card_exp='//input[contains(@placeholder,"MM / YY")]'
    _card_cvv='//input[contains(@placeholder,"Security Code")]'
    _error='//span[text()="Your card number is invalid."]'
    _btn='//div/button[1]/i/parent::button'


    def enterCardNumber(self,cNo):
        self.switchFrameByIndex(self._card_number,'xpath')
        self.sendKeys(cNo,self._card_number,'xpath')
        self.switchToDefaultContent()

    def enterCardExp(self,cExp):
        self.switchFrameByIndex(self._card_exp,'xpath')
        self.sendKeys(cExp,self._card_exp,'xpath')
        self.switchToDefaultContent()

    def enterCardCvv(self,cCvv):
        self.switchFrameByIndex(self._card_cvv,'xpath')
        self.sendKeys(cCvv,self._card_cvv,'xpath')
        self.switchToDefaultContent()

    def enrolCourse(self,cno,cexp,ccvv):
        try:
            time.sleep(2)
            # self.driver.execute_script('window.scrollBy(0,800)')
            self.scrolling()
            self.losd.info('enrolCourse1')
            self.enterCardNumber(cno)
            self.losd.info('enrolCourse2')
            self.enterCardExp(cexp)
            self.losd.info('enrolCourse3')
            self.enterCardCvv(ccvv)
        except:
            self.losd.info('error in enrolCourse4')

    def verifyEnrollFailed(self):
        # el=self.waitForElement(self._error,'xpath')
        if self.isEnabled('',self._btn,'xpath'):
            return False
        else:
            return True
