from selenium.webdriver.common.by import By
from behave import given, then

STORYCARDS = (By.CSS_SELECTOR, "[class='sc-448837bd-1 ZtQGh storycard--text']")


@given('Open Target Circle page')
def open_circle(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify {expected_amount} storycards are shown')
def verify_storycards_shown(context, expected_amount):
    expected_amount = int(expected_amount)
    cards = context.driver.find_elements(*STORYCARDS)
    assert len(cards) == expected_amount, f'Expected {expected_amount} storycards, but got {len(cards)}'
