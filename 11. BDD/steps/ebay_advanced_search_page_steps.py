from behave import *


@when('Advanced search page: I type "{keyword_or_item_number}" in the enter keyword textbox')
def step_impl(context, keyword_or_item_number):
    context.advanced_search_object.enter_keywords_or_item_number(keyword_or_item_number)


@when('Advanced search page: I select "{keyboard_option}" from keyboard options')
def step_impl(context, keyboard_option):
    context.advanced_search_object.select_keywords_option(keyboard_option)


@when('Advanced search page: I choose "{category}" from the category list')
def step_impl(context, category):
    context.advanced_search_object.select_search_category(category)


@when('Advanced search page: I click search button')
def step_impl(context):
    context.advanced_search_object.click_search_button()
