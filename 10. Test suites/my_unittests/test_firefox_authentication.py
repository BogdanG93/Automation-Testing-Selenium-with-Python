from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import unittest
from webdriver_manager.firefox import GeckoDriverManager


class Authentication_in_Firefox(unittest.TestCase):
    USERNAME = 'admin'
    PASSWORD = 'admin'
    AUTH_TEXT = (By.XPATH, "//p")
    lINK_TEXT = (By.XPATH, "//p/a")
    NOTIFICATION_MESSAGE = (By.ID, "flash")
    INPUT_TEXT_LOCATION = (By.ID, "target")
    TEXT_ENTERED = (By.ID, "result")

    def setUp(self) -> None:
        self.firefox = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.firefox.maximize_window()
        self.firefox.implicitly_wait(3)

    def tearDown(self) -> None:
        self.firefox.quit()

    def test_auth(self):
        self.firefox.get('https://' + self.USERNAME + ':' + self.PASSWORD + '@the-internet.herokuapp.com/basic_auth')
        time.sleep(2)
        current_text = self.firefox.find_element(*self.AUTH_TEXT).text
        expected_text = "Congratulations! You must have the proper credentials."
        self.assertEqual(expected_text, current_text, f"ERROR: Expected {expected_text}, Actual: {current_text}")

    def test_notification_messages(self):
        self.firefox.get("https://the-internet.herokuapp.com/notification_message_rendered")
        self.firefox.find_element(*self.lINK_TEXT).click()
        time.sleep(2)
        current_notification_message = self.firefox.find_element(*self.NOTIFICATION_MESSAGE).text
        expected_notification_message = ["Action successful\n×", "Action unsuccesful, please try again\n×"]
        self.assertIn(current_notification_message, expected_notification_message,
                      f"ERROR: Expected {expected_notification_message}, Actual: {current_notification_message}")

    def test_key_pressed(self):
        self.firefox.get("https://the-internet.herokuapp.com/key_presses")
        self.firefox.find_element(*self.INPUT_TEXT_LOCATION).send_keys("automation")
        current_text_key_pressed = self.firefox.find_element(*self.TEXT_ENTERED).text
        time.sleep(2)
        expected_text_key_pressed = "You entered: N"
        self.assertEqual(expected_text_key_pressed, current_text_key_pressed,
                         f"ERROR: Expected {expected_text_key_pressed}, Actual: {current_text_key_pressed}")
