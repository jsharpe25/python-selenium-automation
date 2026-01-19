from selenium.webdriver.common.by import By
from behave import when, then


HEADER_LINKS = (By.CSS_SELECTOR, '[data-test*="@web/GlobalHeader/UtilityHeader/"]')


@when('Search for {product}')
def step_search_product(context, product):
    context.app.header.search_product(product)


@when('Click on shopping cart icon')
def step_click_cart(context):
    context.app.header.click_cart()


@then('Verify {expected_amount} top header links are shown')
def verify_top_links_shown(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*HEADER_LINKS)
    assert len(links) == expected_amount, f'Expected {expected_amount} header links, but got {len(links)}'
