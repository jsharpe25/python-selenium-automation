# Created by Sharpes at 1/6/2026
Feature: Tests Target cart

  Scenario: User can verify "Your cart is empty"
    Given Open Target main page
    When Click on shopping cart icon
    Then Verify empty cart message


  @smoke
  Scenario: User can add product to shopping cart
    Given Open Target main page
    When Search for cereal
    And Click on Add to cart button
    And Store product name
    And Confirm Add to cart button
    And Click on View cart button
    Then Verify cart has 1 item(s)
    And Verify product in cart is correct
