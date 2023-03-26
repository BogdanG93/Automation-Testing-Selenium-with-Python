from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base_page import Base_page


class Home_page(Base_page):
    SEARCH_BOX = ()
    SEARCH_BUTTON = ()
    SEARCH_CATEGORIES = ()
    ADVANCED_SEARCH_LINK = ()
    SEARCH_RESULTS = ()
    HOMEPAGE_URL = ""

    def navigate_to_homepage(self):
        self.chrome.get(self.HOMEPAGE_URL)

    def insert_search_value(self):
        self.chrome.find_element(*self.SEARCH_BOX).send_keys("iphone")

    def choose_category(self):
        category_dropdown = Select(self.chrome.find_element(*self.SEARCH_CATEGORIES))
        category_dropdown.select_by_visible_text("Cell Phones & Accessories")

    def click_search_button(self):
        self.chrome.find_element(*self.SEARCH_BUTTON).click()

    def check_search_results(self):
        self.chrome.find_element(*self.SEARCH_RESULTS)

    def click_advanced_search_link(self):
        self.chrome.find_element(*self.ADVANCED_SEARCH_LINK)
