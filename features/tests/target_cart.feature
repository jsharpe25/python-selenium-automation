# Created by Sharpes at 1/6/2026
Feature: Tests Target cart

  Scenario: User can verify "Your cart is empty"
    Given Open Target main page
    When Click on shopping cart icon
    Then Verify empty cart message


  Scenario: User can add product to shopping cart
    Given Open Target main page
    When Search for cereal
    And Click on Add to cart button
    And Confirm Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)
