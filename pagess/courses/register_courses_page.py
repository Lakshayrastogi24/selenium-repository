from base.selenium_driver import SeleniumDriver
from utilities.custom_logger import customLogger
import time
class RegisterCoursesPage(SeleniumDriver):
    logs=customLogger()
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    # locators
    _search='.form-control.find-input.dynamic-text'
    _search_btn='//i'
    _course='//h4[contains(text(),"{0}")]'
    _enroll_btn='//button[contains(text(),"Enroll in Course")]'

    def enterCourseName(self,courseName):
        self.sendKeys(courseName,self._search,'css')
        self.elementClick(self._search_btn,'xpath')

    def selectCourseToEnrol(self,cName):
        try:
            self.enterCourseName(cName)
            name=self._course.format(cName)
            time.sleep(2)
            self.elementClick(name,'xpath')
            # /elList=self.getElementList('h4','tagname')
            # self.logs.info('Element found : ' + elList)
            # for el in elList:
            #     self.logs.info('Element found : '+el)
            #     self.logs.info('Element text : ' + el.text)
            #     if fullCourseName in el.text:
            #         self.el.elementClick(element=el)
            self.elementClick(self._enroll_btn,'xpath')
        except:
            self.logs.info('error in selectCourseToEnrol')
    def verifyCourse(self):
        return True



