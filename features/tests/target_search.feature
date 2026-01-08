# Created by Sharpes at 1/5/2026
Feature: Tests Target search

  Scenario: User can search for a tea on Target
    Given Open Target main page
    When Search for tea
    Then Search results for tea are shown

  Scenario: User can search for a book on Target
    Given Open Target main page
