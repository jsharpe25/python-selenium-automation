# Created by Sharpes at 1/11/2026
Feature: Tests for Target main page

  Scenario: User can see top header links
    Given Open Target main page
    Then Verify 6 top header links are shown
