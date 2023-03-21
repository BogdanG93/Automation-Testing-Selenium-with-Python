from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import unittest
from webdriver_manager.chrome import ChromeDriverManager


class Context_Menu(unittest.TestCase):
    BOX = (By.ID, "hot-spot")

    def setUp(self) -> None:
        # all activities that need to be executed before any test
        self.chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.chrome.get("https://the-internet.herokuapp.com/context_menu")
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)

    def tearDown(self) -> None:
        # all activities that need to be executed after finishing any test
        self.chrome.quit()

    def test_context_menu(self):
        action = ActionChains(self.chrome)  # create ActionChains object
        elem = self.chrome.find_element(*self.BOX)
        action.context_click(elem).perform()
        time.sleep(2)
        self.chrome.switch_to.alert.accept()
        time.sleep(2)
