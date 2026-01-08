# Created by Sharpes at 1/6/2026
Feature: Tests Target cart

  Scenario: User can verify "Your cart is empty"
    Given Open Target main page
    When Open Target shopping cart
    Then Verify empty cart message
