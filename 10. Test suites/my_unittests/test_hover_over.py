from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import unittest

from webdriver_manager.chrome import ChromeDriverManager


class Hover_elem(unittest.TestCase):

    ACCEPT_COOKIES = (By.ID, "onetrust-accept-btn-handler")
    AROMA = (By.XPATH, "//nav[@id='mainMenuBar']/ul/li[2]/a")

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.chrome.get("https://www.sabon.ro/ro/")
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_hover_over_arome(self):
        # accept cookies
        self.chrome.find_element(*self.ACCEPT_COOKIES).click()
        time.sleep(2)
        elem = self.chrome.find_element(*self.AROMA)
        action = ActionChains(self.chrome).move_to_element(elem).perform()
        time.sleep(3)
