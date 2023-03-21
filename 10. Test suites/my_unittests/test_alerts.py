from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import unittest
from webdriver_manager.chrome import ChromeDriverManager


class Alerts(unittest.TestCase):
    # we define the constants
    JS_ALERT_BUTTON = (By.XPATH, "//*[text()='Click for JS Alert']")
    JS_CONFIRM_BUTTON = (By.XPATH, "//*[text()='Click for JS Confirm']")
    JS_PROMPT_BUTTON = (By.XPATH, "//*[text()='Click for JS Prompt']")
    ALERT_ACTION_MESSAGE = (By.ID, "result")
    INSERT_TEXT = "This is a test"

    # setUP method
    def setUp(self) -> None:
        # all activities that need to be executed before any test
        self.chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.chrome.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)

    # tearDown method
    def tearDown(self) -> None:
        # all activities that need to be executed after finishing any test
        self.chrome.quit()

    # from here we write our tests
    def test_js_alert_accept(self):
        # '*' unpacks the tuple
        self.chrome.find_element(*self.JS_ALERT_BUTTON).click()
        time.sleep(2)
        js_alert = self.chrome.switch_to.alert
        js_alert.accept()
        time.sleep(2)
        # test action text
        js_alert_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
        expected_text = "You successfully clicked an alert"
        time.sleep(2)
        self.assertEqual(expected_text, js_alert_text, f"ERROR! Expected: {expected_text}, Actual: {js_alert_text}")

    def test_js_confirm_accept_alert(self):
        self.chrome.find_element(*self.JS_CONFIRM_BUTTON).click()
        time.sleep(2)
        js_confirm = self.chrome.switch_to.alert
        js_confirm.accept()
        time.sleep(2)
        js_confirm_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
        expected_text = "You clicked: Ok"
        time.sleep(2)
        self.assertEqual(expected_text, js_confirm_text, f"ERROR! Expected: {expected_text}, Actual: {js_confirm_text}")

    def test_js_confirm_cancel_alert(self):
        self.chrome.find_element(*self.JS_CONFIRM_BUTTON).click()
        time.sleep(2)
        js_cancel = self.chrome.switch_to.alert
        js_cancel.dismiss()
        time.sleep(2)
        js_cancel_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
        expected_text = "You clicked: Cancel"
        time.sleep(2)
        self.assertEqual(expected_text, js_cancel_text, f"ERROR! Expected: {expected_text}, Actual: {js_cancel_text}")

    def test_js_prompt_accept_alert_with_text(self):
        self.chrome.find_element(*self.JS_PROMPT_BUTTON).click()
        time.sleep(2)
        js_prompt = self.chrome.switch_to.alert
        js_prompt.send_keys(self.INSERT_TEXT)
        time.sleep(2)
        js_prompt.accept()
        time.sleep(2)
        js_prompt_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
        expected_text = f"You entered: {self.INSERT_TEXT}"
        self.assertEqual(expected_text, js_prompt_text, f"ERROR! Expected: {expected_text}, Actual: {js_prompt_text}")

    def test_js_prompt_alert_without_text(self):
        self.chrome.find_element(*self.JS_PROMPT_BUTTON).click()
        time.sleep(2)
        js_prompt = self.chrome.switch_to.alert
        js_prompt.accept()
        time.sleep(2)
        js_prompt_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
        expected_text = "You entered:"
        self.assertEqual(expected_text, js_prompt_text, f"ERROR! Expected: {expected_text}, Actual: {js_prompt_text}")

    def test_js_prompt_cancel(self):
        self.chrome.find_element(*self.JS_PROMPT_BUTTON).click()
        time.sleep(2)
        js_prompt = self.chrome.switch_to.alert
        js_prompt.dismiss()
        time.sleep(2)
        js_prompt_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
        expected_text = "You entered: null"
        self.assertEqual(expected_text, js_prompt_text, f"ERROR! Expected: {expected_text}, Actual: {js_prompt_text}")

    def test_js_prompt_cancel_with_text(self):
        self.chrome.find_element(*self.JS_PROMPT_BUTTON).click()
        time.sleep(2)
        js_prompt = self.chrome.switch_to.alert
        js_prompt.send_keys(self.INSERT_TEXT)
        js_prompt.dismiss()
        time.sleep(2)
        js_prompt_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
        expected_text = "You entered: null"
        self.assertEqual(expected_text, js_prompt_text, f"ERROR! Expected: {expected_text}, Actual: {js_prompt_text}")
