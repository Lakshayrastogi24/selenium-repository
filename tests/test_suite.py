from tests.home.login_tests import LoginTests
from tests.courses.register_courses_csv_data_tests import RegisterCoursesCsvDataTests
import pytest
import unittest

tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2=unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCsvDataTests)

smokeTest=unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)