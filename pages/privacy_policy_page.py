from pages.base_page import Page

class PrivacyPolicyPage(Page):

    def verify_pp_page_opened(self):
        self.verify_url_contains('target-privacy-policy')
