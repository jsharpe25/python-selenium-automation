from selenium.webdriver.common.by import By
from behave import when, then
from selenium.webdriver.support import expected_conditions as EC


ADD_CART_BTN = (By.CSS_SELECTOR, '[data-test="chooseOptionsButton"]')
CONFIRM_CART_BTN = (By.CSS_SELECTOR, '[data-test="orderPickupButton"]')
OPEN_CART_BTN = (By.CSS_SELECTOR, '[href="/cart"]')
TOTAL_TEXT = (By.CSS_SELECTOR, 'h2 [class*="styles_cart-summary-span"]')
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@then('Verify empty cart message')
def steps_verify_empty_cart_message(context):
    context.app.cart_page.verify_empty_cart_message()


@when('Click on Add to cart button')
def add_to_cart_button(context):
    context.driver.find_element(*ADD_CART_BTN).click()
    context.driver.wait.until(
        EC.element_to_be_clickable(CONFIRM_CART_BTN),
        message='Confirm cart button not clickable'
    )


@when('Store product name')
def store_product_name(context):
    context.product_before_adding = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    # print("Name saved: ")
    # print(context.product_before_adding)


@when('Confirm Add to cart button')
def confirm_add_to_cart_button(context):
    context.driver.find_element(*CONFIRM_CART_BTN).click()
    context.driver.wait.until(
        EC.element_to_be_clickable(OPEN_CART_BTN),
        message='Open cart button not clickable'
    )


@when('Open cart page')
def open_cart_page(context):
    context.driver.find_element(*OPEN_CART_BTN).click()


@then('Verify cart has {amount} item(s)')
def verify_cart_items (context, amount):
    context.driver.wait.until(
        EC.presence_of_element_located(TOTAL_TEXT),
        message='Subtotal text did not appear'
    )
    cart_summary = context.driver.find_element(*TOTAL_TEXT).text
    assert f'{amount} item' in cart_summary, f'Expected {amount} item(s) but got {cart_summary} in cart'

@then('Verify product in cart is correct')
def verify_product(context):
    product_in_cart = context.driver.find_element(*PRODUCT_NAME).text
    # print('\nProduct in cart:')
    # print(product_in_cart)
    expected = context.product_before_adding
    assert product_in_cart[:20] == expected[:20],\
        f'Expected product {expected[:20]} but got {product_in_cart[:20]}'
