from pages.base_page import Page

class TermsPage(Page):

    def verify_terms_page(self):
        self.verify_url_contains('terms-conditions')
