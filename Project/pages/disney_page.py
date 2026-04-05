from utilities.webDriverHelper import WebDriverHelper
from uistore.disney_page_locator import DisneyPageLocator
from utilities.screenshot import Screenshot
from time import sleep


class DisneyPage:
    def __init__(self, driver, logger):
        """
        Method name: __init__
        Author name: Saptarshi
        Short description of method:
            Initializes the Disney page object with required utilities
        Return type:
            None
        Parameter list:
            driver, logger
        """
        try:
            self.driver = driver
            self.logger = logger
            self.helper = WebDriverHelper(self.driver)
            self.logger.info("DisneyPage initialized successfully")
        except Exception as e:
            self.logger.error(f"Error initializing DisneyPage: {e}")
            raise

    # to verify disney page loaded or not
    def verify_disney_page(self):
        """
        Method name: verify_disney_page
        Author name: Saptarshi
        Short description of method:
            Verifies that the current URL contains 'Disney'
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.helper.verify_url("Disney")
            self.logger.info("Verified Disney")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_disney_page_failure")
            self.logger.error(f"Failed to verify Disney page URL: {e}")
            raise

    def click_first_product(self):
        """
        Method name: click_first_product
        Author name: Saptarshi
        Short description of method:
            Clicks on the first product on Disney page
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.helper.click(DisneyPageLocator.first_product)
            self.logger.info("Verified First Product")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_first_product_failure")
            self.logger.error(f"Failed to click first product on Disney page: {e}")
            raise

    def disney_page_clutter(self):
        """
        Method name: disney_page_clutter
        Author name: Saptarshi
        Short description of method:
            Executes the complete Disney page flow (sleep -> url verify -> click first product)
        Return type:
            None
        Parameter list:
            None
        """
        try:
            sleep(2)
            self.verify_disney_page()
            self.click_first_product()
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "disney_page_clutter_failure")
            self.logger.error(f"Failed in disney_page_clutter flow: {e}")
            raise