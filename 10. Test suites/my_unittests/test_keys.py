from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import unittest
from webdriver_manager.chrome import ChromeDriverManager


class Keyboard(unittest.TestCase):
    USERNAME = (By.ID, "username")

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.chrome.get("https://the-internet.herokuapp.com/login")
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_select_all(self):
        user = self.chrome.find_element(*self.USERNAME)
        user.send_keys("Albatros")
        time.sleep(2)
        user.clear()
        time.sleep(2)
        user.send_keys("tosmih")
        time.sleep(2)
        # select all and backspace
        user.send_keys(Keys.CONTROL, 'a')
        time.sleep(2)
        user.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        user.send_keys("tomsmith")
        time.sleep(2)
        user.send_keys(Keys.ARROW_LEFT)
        time.sleep(3)
