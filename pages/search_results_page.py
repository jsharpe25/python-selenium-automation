from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultsPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, "//span[@class='h-text-bs h-display-flex h-flex-align-center h-text-grayDark']")

    def verify_search_results(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULTS_TEXT)
