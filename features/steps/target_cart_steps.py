from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep

EMPTY_CART_TEXT = (By.XPATH, "//h1[text()='Your cart is empty']")
ADD_CART_BTN = (By.CSS_SELECTOR, '[data-test="chooseOptionsButton"]')
CONFIRM_CART_BTN = (By.CSS_SELECTOR, '[data-test="orderPickupButton"]')
OPEN_CART_BTN = (By.CSS_SELECTOR, '[href="/cart"]')
TOTAL_TEXT = (By.CSS_SELECTOR, 'h2 [class*="styles_cart-summary-span"]')


@then('Verify empty cart message')
def verify_empty_cart_message(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(*EMPTY_CART_TEXT).text
    print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} not in actual text {actual_text}'


@when('Click on Add to cart button')
def add_to_cart_button(context):
    context.driver.find_element(*ADD_CART_BTN).click()


@when('Confirm Add to cart button')
def confirm_add_to_cart_button(context):
    context.driver.find_element(*CONFIRM_CART_BTN).click()


@when('Open cart page')
def open_cart_page(context):
    context.driver.find_element(*OPEN_CART_BTN).click()

@then('Verify cart has {amount} item(s)')
def verify_cart_message(context, amount):
    cart_summary = context.driver.find_element(*TOTAL_TEXT).text
    assert f'{amount} item' in cart_summary, f'Expected {amount} item(s) but got {cart_summary} in cart'
