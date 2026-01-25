from pages.base_page import Page
from selenium.webdriver.common.by import By

class AppPage(Page):
    PP_LINK = (By.CSS_SELECTOR, "a[aria-label*='privacy policy']")

    def open_app_page(self):
        self.open_url('/c/target-app/-/N-4th2r')

    def click_pp_link(self):
        self.wait_until_clickable_click(*self.PP_LINK)
