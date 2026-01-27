from pages.app_page import AppPage
from pages.base_page import Page
from pages.cart_page import CartPage
from pages.header import Header
from pages.help_page import HelpPage
from pages.main_page import MainPage
from pages.privacy_policy_page import PrivacyPolicyPage
from pages.search_results_page import SearchResultsPage
from pages.sign_in_page import SignInPage
from pages.terms_page import TermsPage

class Application:

    def __init__(self, driver):

        self.app_page = AppPage(driver)
        self.base_page = Page(driver)
        self.cart_page = CartPage(driver)
        self.header = Header(driver)
        self.help_page = HelpPage(driver)
        self.main_page = MainPage(driver)
        self.privacy_policy_page = PrivacyPolicyPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.terms_page = TermsPage(driver)
