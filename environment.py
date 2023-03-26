from browser import Browser
from ebay_home_page import Home_page


def before_all(context):
    context.browser = Browser()

    context.home_page_object = Home_page()


def after_all(context):
    context.browser.close()
