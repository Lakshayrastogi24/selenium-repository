from pagess.courses.register_courses_page import RegisterCoursesPage
import pytest
import unittest
from pagess.courses.card_details_page import CarddetailsPage

@pytest.mark.usefixtures('oneTimeSetUp','setUp')
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self,oneTimeSetUp):
        self.rcp=RegisterCoursesPage(self.driver)
        self.cdp=CarddetailsPage(self.driver)

    @pytest.mark.run(order=1)
    def test_searchCourse(self):
        self.rcp.selectCourseToEnrol('JavaScript')
        result1=self.rcp.verifyCourse()
        assert result1==True
        self.cdp.enrolCourse('2135647891231234','0621','123')
        result2=self.cdp.verifyEnrollFailed()
        assert result2==True


