import unittest

import HtmlTestRunner
from test_alerts import Alerts
from test_context_menu import Context_Menu
from test_firefox_authentication import Authentication_in_Firefox
from test_keys import Keyboard
from test_verificators import Login


class TestSuite(unittest.TestCase):

    def test_suite(self):
        tests_to_run = unittest.TestSuite()
        tests_to_run.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
                               unittest.defaultTestLoader.loadTestsFromTestCase(Context_Menu),
                               unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard),
                               unittest.defaultTestLoader.loadTestsFromTestCase(Authentication_in_Firefox),
                               unittest.defaultTestLoader.loadTestsFromTestCase(Login)])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,  # generates a single report for all the classes
            report_title="Test Execution Report",
            report_name="Test Results"
        )

        runner.run(tests_to_run)
