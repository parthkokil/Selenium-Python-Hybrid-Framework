from utilities.webDriverHelper import WebDriverHelper
from uistore.huffy_page_locator import HuffyPageLocator
from utilities.screenshot import Screenshot
from time import sleep

class HuffyPage:
    def __init__(self, driver, logger):
        """
        Method name: __init__
        Author name: Saptarshi
        Short description of method:
            Initializes the Huffy page object with required utilities
        Return type:
            None
        Parameter list:
            driver, logger
        """
        try:
            self.driver = driver
            self.logger = logger
            self.helper = WebDriverHelper(self.driver)
            self.logger.info("HuffyPage initialized successfully")
        except Exception as e:
            self.logger.error(f"Error initializing HuffyPage: {e}")
            raise

    def click_toddler_bikes(self):
        """
        Method name: click_toddler_bikes
        Author name: Saptarshi
        Short description of method:
            Clicks on Toddler Bikes using JavaScript click
        Return type:
            None
        Parameter list:
            None
        """
        try:
            sleep(2)
            self.helper.js_scroll(HuffyPageLocator.toddler_bikes)
            self.helper.click(HuffyPageLocator.toddler_bikes)
            self.logger.info(f"Toddler bikes clicked")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_toddler_bikes_failure")
            self.logger.error(f"Failed to click toddler bikes: {e}")
            raise

    def verify_keyword_search(self):
        """
        Method name: verify_keyword_search
        Author name: Saptarshi
        Short description of method:
            Verifies the 'Search' text is present in keyword search area
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.helper.verify_text(HuffyPageLocator.search,"Search")
            self.logger.info(f"Keyword search clicked")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_keyword_search_failure")
            self.logger.error(f"Failed to verify keyword search text: {e}")
            raise

    def click_disney(self):
        """
        Method name: click_disney
        Author name: Saptarshi
        Short description of method:
            Clicks on Disney option using JavaScript click
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.helper.js_scroll(HuffyPageLocator.disney)
            self.helper.click(HuffyPageLocator.disney)
            self.logger.info(f"Disney page will appear")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_disney_failure")
            self.logger.error(f"Failed to click Disney option: {e}")
            raise

    def huffy_page_clutter(self):
        """
        Method name: huffy_page_clutter
        Author name: Saptarshi
        Short description of method:
            Executes the complete Huffy page flow (toddler bikes click -> sleep -> verify search -> sleep -> click disney)
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.click_toddler_bikes()
            self.verify_keyword_search()
            self.click_disney()
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "huffy_page_clutter_failure")
            self.logger.error(f"Failed in huffy_page_clutter flow: {e}")
            raise