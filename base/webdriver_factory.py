from selenium import webdriver
class WebdriverFactory():
    def __init__(self):
        pass

    def getWebdriverInstance(self):
        url = 'https://courses.letskodeit.com/'
        driver=webdriver.Chrome(executable_path=r'C:\Users\Lakshay\downloads\chromedriver.exe')
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(3)
        return driver
