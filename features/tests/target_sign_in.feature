# Created by Sharpes at 1/7/2026
Feature: Tests Target sign in page

  Scenario: User can navigate to sign in form
    Given Open Target main page
    When Open Target sign in form
    Then Verify sign in form opened


#Example Scenario Outline to varify error messages
#  Scenario Outline: Login error shown for invalid login
#    Given Open login page
#    When Enter login username <username>
#    And Enter login password <password>
#    Then Verify login error message <err_message>
#    Examples:
#    |username  |password        |err_message                   |
#    |non_exist |password122     |this account not found        |
#    |user123   |incorrect_pass  |this password is not correct  |
  