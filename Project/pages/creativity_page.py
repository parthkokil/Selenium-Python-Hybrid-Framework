from utilities.webDriverHelper import WebDriverHelper
from uistore.creativity_page_loactor import CreativityPageLocator
from utilities.screenshot import Screenshot
from time import sleep


class CreativityPage:
    def __init__(self, driver, logger):
        """
        Method name: __init__
        Author name: Saptarshi
        Short description of method:
            Initializes the Creativity page object with required utilities
        Return type:
            None
        Parameter list:
            driver, logger
        """
        try:
            self.driver = driver
            self.logger = logger
            self.helper = WebDriverHelper(self.driver)
            self.logger.info("CreativityPage initialized successfully")
        except Exception as e:
            self.logger.error(f"Error initializing CreativityPage: {e}")
            raise

    # to verify creativity page loaded or not
    def verify_creativity_page(self):
        """
        Method name: verify_creativity_page
        Author name: Saptarshi
        Short description of method:
            Verifies that the current URL contains 'creativity'
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.helper.verify_url("creativity")
            self.logger.info("Verified url of creativity page")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_creativity_page_failure")
            self.logger.error(f"Failed to verify creativity page URL: {e}")
            raise

    def scroll_down_and_click_art_and_crafts(self):
        """
        Method name: scroll_down_and_click_art_and_crafts
        Author name: Saptarshi
        Short description of method:
            Scrolls down to Arts and Crafts section and clicks it
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.helper.js_scroll(CreativityPageLocator.arts_and_craft)
            self.helper.js_click(CreativityPageLocator.arts_and_craft)
            self.logger.info("Scroll down and clicked art and crafts")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "scroll_down_and_click_art_and_crafts_failure")
            self.logger.error(f"Failed to scroll/click arts and crafts: {e}")
            raise

    def click_creativity(self):
        """
        Method name: click_creativity
        Author name: Saptarshi
        Short description of method:
            Clicks on the Creativity option using JavaScript click
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.helper.js_click(CreativityPageLocator.Creativity)
            self.logger.info("creativity option clicked")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_creativity_failure")
            self.logger.error(f"Failed to click creativity option: {e}")
            raise

    def creativity_page_clutter(self):
        """
        Method name: creativity_page_clutter
        Author name: Saptarshi
        Short description of method:
            Executes the complete Creativity page flow (sleep -> url verify -> sleep -> scroll/click -> click creativity)
        Return type:
            None
        Parameter list:
            None
        """
        try:
            sleep(3)
            self.verify_creativity_page()
            self.scroll_down_and_click_art_and_crafts()
            self.click_creativity()
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "creativity_page_clutter_failure")
            self.logger.error(f"Failed in creativity_page_clutter flow: {e}")
            raise