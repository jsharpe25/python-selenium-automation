# Created by Sharpes at 1/26/2026
Feature: Tests for Help pages

  Scenario: User can select Help topic Promotions & Coupons
    Given Open Help page for Returns
    Then Verify Help Returns page opened
    When Select Help topic Promotions & Coupons
    Then Verify Help Current promotions page opened

  Scenario: User can select Help topic Target Circle
    Given Open Help page for Returns
    Then Verify Help Returns page opened
    When Select Help topic Target Circle™
    Then Verify Help About Target Circle page opened

  Scenario: User can select Help topic Gift Cards
    Given Open Help page for Returns
    Then Verify Help Returns page opened
    When Select Help topic Gift Cards
    Then Verify Help Target GiftCard balance page opened
