from pages.base_page import BasePage
from uistore.home_locators import HomeLocators

class HomePage(BasePage):
    """
    # Class Name    : HomePage
    # Author        : Parth
    # Description   : Page object for Home page operations.
    #                 Inherits from BasePage and uses the unified perform_action dispatcher.
    #                 No duplicate wrappers (like hover_on_menu) are needed here anymore!
    """

    def __init__(self, web_driver, logger):
        super().__init__(web_driver, logger)

    def verify_logo(self):
        """
        Method Name   : verify_logo
        Description   : Verifies that the ELC logo is visible on the homepage
        """
        self.perform_action("VERIFY_VISIBLE", HomeLocators.elc_logo, "ELC Logo")