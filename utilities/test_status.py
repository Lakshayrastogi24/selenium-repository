from utilities.custom_logger import customLogger
from base.selenium_driver import SeleniumDriver

class TestStatus(SeleniumDriver):
    loggs=customLogger()
    def __init__(self,driver):
        super().__init__(driver)
        self.resultList=[]

    def setResult(self,result,resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append('Pass')
                    self.loggs.info("### VERIFICATION SUCCESSFUL :: "+resultMessage)
                else:
                    self.resultList.append('Fail')
                    self.loggs.info("### VERIFICATION FAILED :: " + resultMessage)
                    self.screenshot(resultMessage)
            else:
                self.resultList.append('Fail')
                self.loggs.error("### VERIFICATION FAILED :: " + resultMessage)
                self.screenshot(resultMessage)

        except:
            self.resultList.append('Fail')
            self.loggs.error("### VERIFICATION FAILED :: " + resultMessage)
            self.screenshot(resultMessage)

    def mark(self,result,resultMessage):
        self.setResult(result,resultMessage)

    def markFinal(self,testname,result,resultMessage):
        self.setResult(result,resultMessage)
        if 'Fail' in self.resultList:
            self.loggs.info(testname+' ### TEST FAILED')
            self.resultList.clear()
            assert True==False
        else:
            self.resultList.clear()
            self.loggs.info(testname + ' ### TEST PASSED')
