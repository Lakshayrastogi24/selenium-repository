from base.selenium_driver import SeleniumDriver

class NavigationPage(SeleniumDriver):

    #locator
    _ste_icon='.img-fluid'
    _user_settings_icon='//div[@class="dropdown"]/button'
    _logout='//a[@href="/logout"]'

    def __init__(self,driver):
        super(NavigationPage, self).__init__(driver)
        self.driver=driver

    def navigateToAllCourses(self):
        self.elementClick(self._ste_icon,'css')

    def navigateToUserSettings(self):
        # element1=self.waitForElement(self._user_settings_icon,'xpath',pollFrequency=1,timeOut=10)
        self.elementClick(self._user_settings_icon,'xpath')
        # element2=self.waitForElement(self._logout,'xpath')
        self.elementClick(self._logout,'xpath')
