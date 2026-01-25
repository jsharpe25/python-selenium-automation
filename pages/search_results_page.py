from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResultsPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, "//span[@class='h-text-bs h-display-flex h-flex-align-center h-text-grayDark']")
    ADD_CART_BTN = (By.CSS_SELECTOR, '[data-test="chooseOptionsButton"]')
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    CONFIRM_CART_BTN = (By.CSS_SELECTOR, '[data-test="orderPickupButton"]')
    VIEW_CART_BTN = (By.CSS_SELECTOR, '[href="/cart"]')

    def verify_search_results(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULTS_TEXT)

    def add_to_cart_button(self):
        self.wait_until_clickable_click(*self.ADD_CART_BTN)

    def store_product_name(self):
        self.wait_until_element_present(*self.SIDE_NAV_PRODUCT_NAME)
        return self.grab_text(*self.SIDE_NAV_PRODUCT_NAME)[0:6]


    def confirm_cart_button(self):
        self.wait_until_clickable_click(*self.CONFIRM_CART_BTN)

    def view_cart_button(self):
        self.wait_until_clickable_click(*self.VIEW_CART_BTN)
