from pagess.courses.register_courses_page import RegisterCoursesPage
import pytest
import unittest
from pagess.courses.card_details_page import CarddetailsPage
from ddt import data,unpack,ddt
from utilities.read_data import getCsvData
from pagess.navigation_page import NavigationPage

@pytest.mark.usefixtures('oneTimeSetUp','setUp')
@ddt()
class RegisterCoursesCsvDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objSet(self,oneTimeSetUp):
        self.rcp=RegisterCoursesPage(self.driver)
        self.cdp=CarddetailsPage(self.driver)
        self.np=NavigationPage(self.driver)

    def setUp(self):
        print('abra 11111111111111111111111111111111111111')
        # self.driver.execute_script('window.scrollBy(0,-800)')
        # self.driver.find_element_by_css_selector('.img-fluid').click()
        self.np.scrolling('up')
        self.np.navigateToAllCourses()

    @pytest.mark.run(order=1)
    @data(*getCsvData(r'C:\Users\Lakshay\PycharmProjects\LetsKodeIt_lakshay\test_data.csv'))
    @unpack
    def test_searchCourse(self,courseName,cNum,cExp,cCvv):
        self.rcp.selectCourseToEnrol(courseName)
        result1 = self.rcp.verifyCourse()
        assert result1 == True
        self.cdp.enrolCourse(cNum, cExp, cCvv)
        result2 = self.cdp.verifyEnrollFailed()
        assert result2 == True



