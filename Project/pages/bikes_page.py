from utilities.webDriverHelper import WebDriverHelper
from uistore.bikes_page_locator import BikesPageLocator
from utilities.screenshot import Screenshot


class BikesPage:
    def __init__(self, driver, logger):
        """
        Method name: __init__
        Author name: Saptarshi
        Short description of method:
            Initializes the Bikes page object with required utilities
        Return type:
            None
        Parameter list:
            driver, logger
        """
        try:
            self.driver = driver
            self.logger = logger
            self.helper = WebDriverHelper(self.driver)
            self.logger.info("BikesPage initialized successfully")
        except Exception as e:
            self.logger.error(f"Error initializing BikesPage: {e}")
            raise

    # functions to verify the page is loaded
    def verify_the_url_contain_bikes(self):
        """
        Method name: verify_the_url_contain_bikes
        Author name: Saptarshi
        Short description of method:
            Verifies that the current URL contains 'bikes'
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.helper.verify_url("bikes")
            self.logger.info("Bikes page url is verified")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_the_url_contain_bikes_failure")
            self.logger.error(f"Failed to verify Bikes page URL contains bikes: {e}")
            raise

    def click_on_show_more(self):
        """
        Method name: click_on_show_more
        Author name: Saptarshi
        Short description of method:
            Clicks on the 'Show more' option on bikes page
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.helper.click(BikesPageLocator.show_more_option)
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_on_show_more_failure")
            self.logger.error(f"Failed to click on show more option: {e}")
            raise

    def click_on_huffy(self):
        """
        Method name: click_on_huffy
        Author name: Saptarshi
        Short description of method:
            Clicks on the 'Huffy' option on bikes page
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.helper.click(BikesPageLocator.huffy)
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_on_huffy_failure")
            self.logger.error(f"Failed to click on Huffy option: {e}")
            raise

    def bike_page_clutter(self):
        """
        Method name: bike_page_clutter
        Author name: Saptarshi
        Short description of method:
            Executes the complete Bikes page flow (URL verify -> show more -> huffy click)
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.verify_the_url_contain_bikes()
            self.click_on_show_more()
            self.click_on_huffy()
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "bike_page_clutter_failure")
            self.logger.error(f"Failed in bike_page_clutter flow: {e}")
            raise