from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class HelpPage(Page):
    TOPIC_HEADER = (By.XPATH, "//h1[text()=' {TOPIC_HEADER}']")
    SELECT_TOPIC_DD = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")

    # Dynamic locators
    def _get_header_topic_locator(self, topic): # helper method starts with _
        return (
            self.TOPIC_HEADER[0],
            self.TOPIC_HEADER[1].replace('{TOPIC_HEADER}', topic)
        )

    def open_help_returns(self):
        self.driver.get(
            'https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def select_topic(self, option_value):
        drop_down = self.find_element(*self.SELECT_TOPIC_DD)
        select = Select(drop_down)
        select.select_by_value(option_value)

    def verify_help_topic_opened(self, topic):
        locator = self._get_header_topic_locator(topic)
        self.wait_until_element_present(*locator)
