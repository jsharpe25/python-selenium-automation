from selenium.webdriver.common.by import By
from behave import when, then


ACCOUNT_ICON = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
SIGN_IN_ICON = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
SIGN_IN_MESSAGE = (By.XPATH, "//h1[text()='Sign in or create account']")

@when('Open Target sign in form')
def open_target_sign_in_form(context):
    context.driver.find_element(*ACCOUNT_ICON).click()
    context.driver.find_element(*SIGN_IN_ICON).click()


@then('Verify sign in form opened')
def verify_sign_in_form(context):
    expected_text = 'Sign in or create account'
    actual_text = context.driver.find_element(*SIGN_IN_MESSAGE).text
    print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} not in actual text {actual_text}'
