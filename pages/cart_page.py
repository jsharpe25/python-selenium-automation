from pages.base_page import Page
from selenium.webdriver.common.by import By

class CartPage(Page):
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    empty_cart_message = 'Your cart is empty' # Easier to update message here
    TOTAL_TEXT = (By.CSS_SELECTOR, 'h2 [class*="styles_cart-summary-span"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def open_cart_page(self):
        self.open_url(end_url='cart')

    def verify_empty_cart_message(self):
        self.wait_until_url_contains('cart')
        self.verify_url(f'{self.base_url}/cart')
        self.verify_partial_text(self.empty_cart_message, *self.EMPTY_CART_MESSAGE)

    def verify_cart_items(self, amount):
        self.wait_until_element_present(*self.TOTAL_TEXT)
        self.verify_partial_text(amount, *self.TOTAL_TEXT)

    def verify_product(self, expected_product_name):
        self.wait_until_element_present(*self.PRODUCT_NAME)
        self.verify_partial_text(expected_product_name, *self.PRODUCT_NAME)
