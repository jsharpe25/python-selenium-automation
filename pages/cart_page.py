from pages.base_page import Page
from selenium.webdriver.common.by import By

class Cart(Page):
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    empty_cart_message = 'Your cart is empty' # Easier to update here

    def open_cart_page(self):
        self.open_url(end_url='cart')

    def verify_empty_cart_message(self):
        self.wait_until_url_contains('cart')
        self.verify_url(f'{self.base_url}/cart')
        self.verify_partial_text(self.empty_cart_message, *self.EMPTY_CART_MESSAGE)
