import pytest
from selenium import webdriver
from utilities.custom_logger import customLogger
from base.webdriver_factory import WebdriverFactory
from pagess.home.login_page import LoginPage

@pytest.fixture()
def setUp():
    print('method level set up')
    yield
    print('method level tear down')


@pytest.fixture(scope='class')
def oneTimeSetUp(request):
    print('class level set up')
    logg = customLogger()
    wdf=WebdriverFactory()
    driver=wdf.getWebdriverInstance()
    # url = 'https://courses.letskodeit.com/'
    # if browser == 'chrome':
    # driver = webdriver.Chrome(executable_path=r'C:\Users\Lakshay\downloads\chromedriver.exe')
    # driver.maximize_window()
    # driver.implicitly_wait(3)
    # driver.get(url)
    logg.info('one time set up')
    lp=LoginPage(driver)
    lp.login('lakshrstg@gmail.com','123456')

    # else:
    #     driver = webdriver.Chrome(executable_path=r'C:\Users\Lakshay\downloads\chromedriver.exe')
    #     driver.maximize_window()
    #     driver.implicitly_wait(3)
    #     driver.get(url)
    if request.cls is not None:
        request.cls.driver = driver
    logg.info('one time set up 1')
    yield driver
    print('class level tear down')
    driver.quit()


def addoption(parser):
    print('abra')
    parser.addoption("--browser", action="store")


@pytest.fixture()
def browser(request):
    print('dabra')
    return request.config.getoption("--browser")
