from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep


@when('Open Target sign in form')
def open_target_sign_in_form(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()


@then('Verify sign in form opened')
def verify_sign_in_form(context):
    expected_text = 'Sign in or create account'
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']").text
    print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} not in actual text {actual_text}'
    sleep(2)
