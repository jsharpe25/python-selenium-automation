from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep

SEARCH_FIELD = (By.ID, 'search')
SEARCH_ICON = (By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]')
CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartIcon"]')
HEADER_LINKS = (By.CSS_SELECTOR, '[data-test*="@web/GlobalHeader/UtilityHeader/"]')


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_ICON).click()
    sleep(10)


@when('Click on shopping cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()

@then('Verify {expected_amount} top header links are shown')
def verify_top_links_shown(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*HEADER_LINKS)
    assert len(links) == expected_amount, f'Expected {expected_amount} header links, but got {len(links)}'
