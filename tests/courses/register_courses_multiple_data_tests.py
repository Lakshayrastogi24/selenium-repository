from pagess.courses.register_courses_page import RegisterCoursesPage
import pytest
import unittest
from pagess.courses.card_details_page import CarddetailsPage
from ddt import data,unpack,ddt

@pytest.mark.usefixtures('oneTimeSetUp','setUp')
@ddt()
class RegisterCoursesMultipleDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self,oneTimeSetUp):
        self.rcp=RegisterCoursesPage(self.driver)
        self.cdp=CarddetailsPage(self.driver)



    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "2135647891231234", "0621", "123"),('JavaScript for beginners', '213516', '0621', '123'))
    @unpack
    def test_searchCourse(self,courseName,cNum,cExp,cCvv):
        self.rcp.selectCourseToEnrol(courseName)
        result1=self.rcp.verifyCourse()
        assert result1==True
        self.cdp.enrolCourse(cNum,cExp,cCvv)
        result2=self.cdp.verifyEnrollFailed()
        assert result2==True
        self.driver.execute_script('window.scrollBy(0,-800)')
        self.driver.find_element_by_css_selector('.img-fluid').click()

