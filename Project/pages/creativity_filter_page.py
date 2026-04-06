from utilities.webDriverHelper import WebDriverHelper
from uistore.creativity_filter_page_locator import CreativityFilterPageLocator
from utilities.screenshot import Screenshot
from time import sleep


class CreativityFilterPage:
    def __init__(self, driver, logger):
        """
        Method name: __init__
        Author name: Saptarshi
        Short description of method:
            Initializes the Creativity Filter page object with required utilities
        Return type:
            None
        Parameter list:
            driver, logger
        """
        try:
            self.driver = driver
            self.logger = logger
            self.helper = WebDriverHelper(self.driver)
            self.logger.info("CreativityFilterPage initialized successfully")
        except Exception as e:
            self.logger.error(f"Error initializing CreativityFilterPage: {e}")
            raise

    # verification of creativity filter page
    def verify_creativity_filter_page(self):
        """
        Method name: verify_creativity_filter_page
        Author name: Saptarshi
        Short description of method:
            Verifies that the current URL contains 'Creativity'
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.helper.verify_url("Creativity")
            self.logger.info("Verified url of creativity filter page contains Creativity")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_creativity_filter_page_failure")
            self.logger.error(f"Failed to verify creativity filter page URL: {e}")
            raise

    def click_first_product(self):
        """
        Method name: click_first_product
        Author name: Saptarshi
        Short description of method:
            Clicks on the first product using JavaScript click
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.helper.js_click(CreativityFilterPageLocator.first_product)
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_first_product_failure")
            self.logger.error(f"Failed to click first product: {e}")
            raise

    def creativity_filter_page_clutter(self):
        """
        Method name: creativity_filter_page_clutter
        Author name: Saptarshi
        Short description of method:
            Executes the complete Creativity Filter page flow (sleep -> url verify -> click first product)
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.verify_creativity_filter_page()
            self.click_first_product()
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "creativity_filter_page_clutter_failure")
            self.logger.error(f"Failed in creativity_filter_page_clutter flow: {e}")
            raise