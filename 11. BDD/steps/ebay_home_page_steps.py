from behave import *


@given("Home page: I am on ebay homepage")
def step_impl(context):
    context.home_page_object.navigate_to_homepage()
    context.home_page_object.accept_cookies()


@when("Home page: I search for iphone from category Cell Phones & Accessories")
def step_impl(context):
    context.home_page_object.insert_search_value()
    context.home_page_object.choose_category()
    context.home_page_object.click_search_button()


@then("Home page: I have at least 1000 results returned")
def step_impl(context):
    context.home_page_object.check_search_results()


@when("Home page: I click on the advanced link")
def step_impl(context):
    context.home_page_object.click_advanced_search_link()
