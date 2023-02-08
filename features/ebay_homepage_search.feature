Feature: Test the search functionality in the homepage of Ebay

  Background:
    Given Home page: I am on Ebay homepage

      @T1 @regressionTesting @functionalTesting
  Scenario Outline: Check that the user can make a simple search in the Ebay homepage
    When Home page: I search for "<product_name>" from category "<category_name>"
    Then Home page: I have at least "<number_of_results>" results returned

      @electronics
      Examples:
        | product_name | category_name             | number_of_results |
        | iphone       | Cell Phones & Accessories | 1000              |
        | TV           | Consumer Electronics      | 20000             |


      @clothes
      Examples:
        | product_name | category_name                 | number_of_results |
        | sweter       | Clothing, Shoes & Accessories | 1000000           |

  @T2 @functionalTesting
  Scenario: Check that the user can make an advanced search for a product
    When Home page: When I click on the advanced link
    When Advanced search page: I type Pampers in the enter keyword textbox
    When Advanced search page: I select Exact words exact order from keyword options
    When Advanced search page: I choose Baby from the category list
    When Advanced search page: I click search button
    Then Home Page: I have at least "1000" results returned

   Scenario Outline: Check that the user can add a product to shopping cart
     When Home page: I search for "<product_name>" from category "<category_name>"
     When Search Results: I choose the first product in the list
     When Search Results: I choose "<colour_property>" as "<colour>"
     When Search Results: I choose "<storage_capacity_property>" as "<storage_capacity>"
     When Search Results: I choose "<lock_status_property>" as "<lock_status>"
     When Search Results: I choose "<sim_card_slot_property>" as "<sim_card_slot_property>"
     When Search Results: I click Add to Cart button
     When Search Results: I click on the shopping cart
     Then Shopping Cart: I have one product in the shopping cart


      @electronics
      Examples:
        | product_name | category_name             | colour_property | colour | storage_capacity_property | storage_capacity | lock_status_propery | lock_status      | sim_card_slot_property | sim_card_slot |  |
        | iphone       | Cell Phones & Accessories | colour          | gold   | storage_capacity          | 1TB              | lock_status         | Factory Unlocked | sim_card_property      | eSIM          |  |



