Feature: Test the search functionality in the homepage of ebay

  Background:
    Given Home page: I am on ebay homepage

  @T1
  Scenario Outline: Check that the user can make a simple search in the Ebay homepage

    When Home page: I search for "<product_name>" from category "<category_name>"
    Then Home page: I have at least "<no_of_results>" results returned

    Examples:
      | product_name | category_name             | no_of_results |
      | iphone       | Cell Phones & Accessories | 1000          |
      | TV           | Consumer Electronics      | 10000         |


  @T2
  Scenario Outline: Check that the user can make an advanced search for a product
    When Home page: I click on the advanced link
    When Advanced search page: I type "<keyword_or_item_number>" in the enter keyword textbox
    When Advanced search page: I select "<keyword_option>" from keyboard options
    When Advanced search page: I choose "<category>" from the category list
    When Advanced search page: I click search button
    Then Home page: I have at least "<no_of_results>" results returned

    Examples:
      | keyword_or_item_number | keyword_option           | category             | no_of_results |
      | Pampers                | Exact words, exact order |Baby                  | 1000          |
      | TV                     | All words, any order     | Consumer Electronics | 800000        |
