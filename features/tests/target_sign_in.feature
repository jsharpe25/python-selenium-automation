# Created by Sharpes at 1/7/2026
Feature: Tests Target sign in page

  Scenario: User can navigate to sign in form
    Given Open Target main page
    When Open Target sign in form
    Then Verify sign in form opened
