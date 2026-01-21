from pages.base_page import Page
from selenium.webdriver.common.by import By

class SignInPage(Page):
    ACCOUNT_ICON = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    SIGN_IN_ICON = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    SIGN_IN_MESSAGE = (By.XPATH, "//h1[text()='Sign in or create account']")
    sign_in_message = 'Sign in or create account'

    def open_sign_in_form(self):
        self.wait_until_clickable_click(*self.ACCOUNT_ICON)
        self.wait_until_clickable_click(*self.SIGN_IN_ICON)

    def verify_sign_in_form(self):
        self.wait_until_element_present(*self.SIGN_IN_MESSAGE)
        self.verify_partial_text(self.sign_in_message, *self.SIGN_IN_MESSAGE)
