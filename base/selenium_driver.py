
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import *
import time

from utilities.custom_logger import customLogger

class SeleniumDriver:


    lo=customLogger()
    def  __init__(self,driver):
        self.driver=driver

    def screenshot(self,resultMessage):
        try:
            filename=resultMessage+ str(round(time.time()*1000))+'.png'
            dirr=r'C:\Users\Lakshay\PycharmProjects\LetsKodeIt_lakshay\screenshots'
            filePath=dirr+"\\"+filename
            self.driver.save_screenshot(filePath)
            self.lo.info('Screenshot has been saved '+dirr)
        except:
            self.lo.info('Screenshot has not been saved ')

    def getTitle(self):
        return self.driver.title

    def getByType(self,locatorType):
        ltype=locatorType.lower()

        if ltype=='id':
            return By.ID
        elif ltype=='classname':
            return By.CLASS_NAME
        elif ltype=='css':
            return By.CSS_SELECTOR
        elif ltype=='name':
            return By.NAME
        elif ltype=='linktext':
            return By.LINK_TEXT
        elif ltype=='xpath':
            return By.XPATH
        elif ltype=='tagname':
            return By.TAG_NAME
        else:
            self.lo.info('Locator Type '+ltype+ ' not supported')

    def getElement(self,locator,locatorType='id'):
        try:
            bytype=self.getByType(locatorType)
            element=self.driver.find_element(bytype,locator)
            self.lo.info('element found with locator: '+locator+' and locatorType: '+locatorType)
        except:
            self.lo.info('element not found with locator: '+locator+' and locatorType: '+locatorType)
        return element

    def elementClick(self,locator="",locatorType='id',element=None):
        try:
            if locator!="":
                element=self.getElement(locator,locatorType);
            element.click()
            self.lo.info('Clicked on element with locator: '+locator+' and locatorType: '+locatorType)
        except:
            self.lo.info('Cannot Click on element with locator: ' + locator + ' and locatorType: ' + locatorType)
            print_stack()

    def sendKeys(self,data,locator,locatorType='id'):
        try:
            ele=self.getElement(locator,locatorType)
            ele.send_keys(data)
            self.lo.info('Sent data on element with locator: '+locator+' and locatorType: '+locatorType)
        except:
            self.lo.info('Not sent data on element with locator: '+locator+' and locatorType: '+locatorType)
            print_stack()

    def isElementPresent(self,locator,locatorType='id'):
        try:
            ele=self.getElement(locator,locatorType)
            if ele is not None:
                self.lo.info('element found')
                return True
            else:
                return False('element not found with locator: '+locator+' and locatorType: '+locatorType)
        except:
                self.lo.info('element not found with locator: '+locator+' and locatorType: '+locatorType)
                return False

    def elementPresenceChcek(self,locator,byType):
        try:
            eleList=self.driver.find_elements(byType,locator)
            if len(eleList)>0:
                self.lo.info('element found with locator: '+locator+' and locatorType: '+byType)
                return True
            else:
                self.lo.info('element not found with locator: '+locator+' and locatorType: '+byType)
                return False
        except:
            self.lo.info('element not found with locator: '+locator+' and locatorType: '+byType)
            return False

    def waitForElement(self,locator,locatorType='id',timeOut=10,pollFrequency=0.5):
        try:
            bytype=self.getByType(locatorType)

            wait=WebDriverWait(self.driver,timeOut,pollFrequency=1,ignored_exceptions=[NoSuchElementException,
                                                                                       ElementNotVisibleException,
                                                                                       ElementNotSelectableException])
            ele=wait.until(expected_conditions.element_to_be_clickable(bytype,locator))
            self.lo.info('element appeared on webpage with locator: '+locator+' and locatorType: '+locatorType)
        except:
            self.lo.info('element not appeared on webpage with locator: '+locator+' and locatorType: '+locatorType)
            print_stack()
        return ele

    def getElementList(self,locator,locatorType='id'):
        try:
            byType=self.getByType(locatorType)
            self.lo.info('element list bytype: ' + byType+' :'+locator+' :'+byType)
            elementList=self.driver.find_elements(byType,locator)
            self.lo.info('element list found: '+elementList)
        except:
            self.lo.info('element not appeared on webpage with locator: '+locator+' and locatorType: '+locatorType)
        return elementList

    def scrolling(self,scrl='down'):
        try:
            if scrl=='down':
                self.driver.execute_script('window.scrollBy(0,800)')
            else:
                self.driver.execute_script('window.scrollBy(0,-800)')
        except:
            self.lo.info('cannot scroll due to some issue')

    def switchToFrame(self,id='',name='',index=None):

        if id:
            self.driver.switch_to.frame(id)
        if name:
            self.driver.switch_to.frame(name)
        if index:
            self.driver.switch_to.frame(index)
        
    def switchToDefaultContent(self):
        self.driver.switch_to.default_content()


    def getElementAttributeValue(self,attr,locator,locatorType='id'):

        ele=self.getElement(locator,locatorType)
        value=ele.get_attribute(attr)
        return value

    def isEnabled(self,attr,locator,locatorType='id'):
        ena = False
        try:
            ele=self.getElement(locator,locatorType)
            val=self.getElementAttributeValue('disabled',locator,locatorType)
            if val is not None:
                ena=ele.is_enabled()
            else:
                val = self.getElementAttributeValue('class', locator, locatorType)
                ena= not('disabled' in val)
            if ena:
                self.lo.info('element enabled on webpage with locator: '+locator+' and locatorType: '+locatorType)
            else:
                self.lo.info('element disabled on webpage with locator: ' + locator + ' and locatorType: ' + locatorType)
        except:
            self.lo.error('element not found on webpage with locator: ' + locator + ' and locatorType: ' + locatorType)
        return ena


    def switchFrameByIndex(self,locator,locatorType):

        res=False
        try:
            iframe_list=self.getElementList('//div/iframe','xpath')
            for i in range(len(iframe_list)):
                self.switchToFrame(index=iframe_list[i])
                res=self.isElementPresent(locator,locatorType)
                if res:
                    break
                else:
                    self.switchToDefaultContent()
        except:
            self.lo.error('element not found on webpage with locator: ' + locator + ' and locatorType: ' + locatorType)
        return res






