from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from webdriver_manager.chrome import ChromeDriverManager


class Login(unittest.TestCase):
    """ here we define all constant variables """

    TITLE_PAGE = (By.XPATH, "//h2[text()='Login Page']")
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "radius")
    LOGOUT_BUTTON = (By.XPATH, "//*[@class='button secondary radius']")
    ALERT_ACTION_MESSAGE = (By.ID, "flash")
    CLOSE_ALERT_ACTION_MESSAGE = (By.XPATH, "//*[@class='close']")
    PAGE_POWERED_BY = (By.XPATH, "//*[text()='Elemental Selenium']")
    LOGIN_PAGE_TEXT = (By.XPATH, "//*[@class='subheader']")

    # setUP method
    def setUp(self) -> None:
        # all activities that need to be executed before every test
        self.chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.chrome.get("https://the-internet.herokuapp.com")
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.find_element(By.XPATH, "//a[text()='Form Authentication']").click()

    # tearDown method
    def tearDown(self) -> None:
        # all activities that need to be executed after every test
        self.chrome.quit()

    """ the methods we defined to execute tests """
    def test_url_check(self):
        """ Checks if the URL is correct """
        current_url = self.chrome.current_url
        expected_url = "https://the-internet.herokuapp.com/login"
        self.assertEqual(expected_url, current_url, f"ERROR. Expected: {expected_url}, Actual: {current_url}")

    def test_title_login(self):
        """ Checks if the title in the Login Page is correct """
        current_title = self.chrome.find_element(*self.TITLE_PAGE).text
        expected_title = "Login Page"
        self.assertEqual(expected_title, current_title, f"ERROR. Expected: {expected_title}, Actual: {current_title}")

    def test_xpath_text_title(self):
        """ Checks if the XPath element of the title in the login page is correct """
        element_to_verify = self.chrome.find_element(By.XPATH, "//h2").text
        expected_text = "Login Page"
        self.assertEqual(expected_text, element_to_verify,
                         f"ERROR: Expected {expected_text}, Actual: {element_to_verify}")

    def test_login_button_is_displayed(self):
        """ Checks if the login button is displayed """
        login_button = WebDriverWait(self.chrome, 5).until(EC.visibility_of_element_located(self.LOGIN_BUTTON))
        self.assertTrue(login_button.is_displayed(), "ERROR. Login button is not displayed.")

    def test_href_attribute(self):
        """ Checks if the href attribute on the login page is correct """
        link = self.chrome.find_element(*self.PAGE_POWERED_BY)
        href_attribute = link.get_attribute("href")
        expected_href = "http://elementalselenium.com/"
        self.assertEqual(expected_href, href_attribute, f"ERROR. Expected: {expected_href}, Actual: {href_attribute}")

    def test_alert_message_empty_login(self):
        """ Checks the alert message when you perform an empty login """
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        empty_login_alert_message = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
        expected_alert_message = "Your username is invalid!"
        self.assertTrue(expected_alert_message in empty_login_alert_message,
                        f"ERROR. Expected: {expected_alert_message}, Actual: {empty_login_alert_message}")

    def test_alert_message_invalid_user_password(self):
        """ Checks the alert message when invalid user and password are introduced """
        self.chrome.find_element(*self.USERNAME).send_keys("test")
        self.chrome.find_element(*self.PASSWORD).send_keys("test")
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        invalid_alert_message = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
        expected_alert_message = "Your username is invalid!"
        self.assertIn(expected_alert_message, invalid_alert_message,
                      f"ERROR. Expected: {expected_alert_message}, Actual: {invalid_alert_message}")

    def test_login_error_dismisses_when_x_pressed(self):
        """Checks if the alert message disappears when clicking the 'x' in the text, when logging with no credentials"""
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.CLOSE_ALERT_ACTION_MESSAGE).click()
        try:
            WebDriverWait(self.chrome, 2).until(EC.staleness_of(self.chrome.find_element(*self.ALERT_ACTION_MESSAGE)))
        except TimeoutException:
            self.fail(f"Error. Expected: None, Actual: {self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text}")

    def test_username_and_password_labels(self):
        """ Checks if the correct username and password labels are displayed on the login page """
        list_of_labels = self.chrome.find_elements(By.XPATH, "//label")
        username_label, password_label = list_of_labels[0].text, list_of_labels[1].text
        expected_username_label = "Username"
        expected_password_label = "Password"
        self.assertEqual(expected_username_label, username_label,
                         f"ERROR: Expected {expected_username_label}, Actual: {username_label}")
        self.assertEqual(expected_password_label, password_label,
                         f"ERROR: Expected {expected_password_label}, Actual: {password_label}")

    def test_valid_signup(self):
        """ Checks the expected outcome of a successful sign-up with
        valid username and password, alert action message and URL"""
        self.chrome.find_element(*self.USERNAME).send_keys("tomsmith")
        self.chrome.find_element(*self.PASSWORD).send_keys("SuperSecretPassword!")
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        alert_action_message = WebDriverWait(self.chrome, 5) \
            .until(EC.visibility_of_element_located(self.ALERT_ACTION_MESSAGE))
        current_alert_message = alert_action_message.text
        current_url = self.chrome.current_url
        flash_displayed = alert_action_message.is_displayed()
        assert (("/secure" in current_url) and flash_displayed and
                ("secure area!" in current_alert_message)), \
            f"ERROR. At least one out of the three failed:\n" \
            f"- the current URL '{current_url}' doesn't contain '/secure'\n" \
            f"- element with class='flash success' is not displayed\n" \
            f"- the current alert message '{current_alert_message}' doesn't contain 'secure area!'"

    def test_login_logout_functionality(self):
        """ Checks the log-in/log-out functionality and the corresponding sign-out URL """
        self.chrome.find_element(*self.USERNAME).send_keys("tomsmith")
        self.chrome.find_element(*self.PASSWORD).send_keys("SuperSecretPassword!")
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.LOGOUT_BUTTON).click()
        current_url = self.chrome.current_url
        expected_url = "https://the-internet.herokuapp.com/login"
        self.assertEqual(expected_url, current_url,
                         f"ERROR: Expected {expected_url}, Actual: {current_url}")

    def test_password_brute_force(self):
        login_page_text = self.chrome.find_element(*self.LOGIN_PAGE_TEXT).text
        potential_passwords = login_page_text.split()
        for potential_password in potential_passwords:
            username = self.chrome.find_element(*self.USERNAME)
            password = self.chrome.find_element(*self.PASSWORD)
            username.clear()
            password.clear()
            username.send_keys("tomsmith")
            password.send_keys(potential_password)
            login_button = self.chrome.find_element(*self.LOGIN_BUTTON)
            login_button.click()
            remove_alert_action_message = WebDriverWait(self.chrome, 10) \
                .until(EC.presence_of_element_located(self.CLOSE_ALERT_ACTION_MESSAGE))
            remove_alert_action_message.click()
            actual_url = self.chrome.current_url
            if "/secure" in actual_url:
                print("The secret password is", potential_password)
                break
        else:
            self.fail("We haven't identified the password.")
