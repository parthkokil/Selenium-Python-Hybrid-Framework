from utilities.webDriverHelper import WebDriverHelper
from uistore.product_page_locator import ProductPageLocator
from utilities.screenshot import Screenshot


class ProductPage:
    def __init__(self, driver, logger):
        """
        Method name: __init__
        Author name: Saptarshi
        Short description of method:
            Initializes the Product page object with required utilities
        Return type:
            None
        Parameter list:
            driver, logger
        """
        try:
            self.driver = driver
            self.logger = logger
            self.helper = WebDriverHelper(self.driver)
            self.logger.info("ProductPage initialized successfully")
        except Exception as e:
            self.logger.error(f"Error initializing ProductPage: {e}")
            raise

    # verifiy the add busket button to know product page loaded
    def verify_the_add_basket_button(self):
        """
        Method name: verify_the_add_basket_button
        Author name: Saptarshi
        Short description of method:
            Verifies 'Add to Basket' button exists on product page
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.helper.verify_text(ProductPageLocator.add_to_basket,"Add")
            self.logger.info("Add To Basket exist means it is in product page")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_the_add_basket_button_failure")
            self.logger.error(f"Failed to verify Add to Basket button: {e}")
            raise

    # for test case3
    def verify_the_quantity_as_one(self):
        """
        Method name: verify_the_quantity_as_one
        Author name: Saptarshi
        Short description of method:
            Verifies that the quantity value is '1'
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.helper.verify_attribute(ProductPageLocator.one, "value", "1")
            self.logger.info("Quantity value is 1 checked")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_the_quantity_as_one_failure")
            self.logger.error(f"Failed to verify quantity as one: {e}")
            raise

    def click_add_to_basket(self):
        """
        Method name: click_add_to_basket
        Author name: Saptarshi
        Short description of method:
            Clicks on Add to Basket using JavaScript click
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.helper.js_scroll(ProductPageLocator.add_to_basket)
            self.helper.click(ProductPageLocator.add_to_basket)
            self.logger.info("Add To Basket")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_add_to_basket_failure")
            self.logger.error(f"Failed to click Add to Basket: {e}")
            raise

    # verify check_out for page load
    def verify_check_out(self):
        """
        Method name: verify_check_out
        Author name: Saptarshi
        Short description of method:
            Verifies 'Check out' text is present
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.helper.verify_text(ProductPageLocator.check_out,"Check out")
            self.logger.info("Check Out exist")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_check_out_failure")
            self.logger.error(f"Failed to verify Check out text: {e}")
            raise

    def click_check_out(self):
        """
        Method name: click_check_out
        Author name: Saptarshi
        Short description of method:
            Clicks on Check out using JavaScript click
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.helper.js_scroll(ProductPageLocator.check_out)
            self.helper.click(ProductPageLocator.check_out)
            self.logger.info("Check Out clicked")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_check_out_failure")
            self.logger.error(f"Failed to click Check out: {e}")
            raise

    # for test case 4
    def verify_the_keyword_minutes(self):
        """
        Method name: verify_the_keyword_minutes
        Author name: Saptarshi
        Short description of method:
            Clicks on keyword 'minutes' using JavaScript click
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.helper.js_scroll(ProductPageLocator.minutes)
            self.helper.click(ProductPageLocator.minutes)
            self.logger.info("Keyword minutes checked")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_the_keyword_minutes_failure")
            self.logger.error(f"Failed to verify keyword minutes: {e}")
            raise

    def product_page_clutter(self):
        """
        Method name: product_page_clutter
        Author name: Saptarshi
        Short description of method:
            Executes product flow (verify add basket -> sleep -> verify qty -> sleep -> add basket -> sleep -> verify checkout -> click checkout)
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.verify_the_add_basket_button()
            self.verify_the_quantity_as_one()
            self.click_add_to_basket()
            self.verify_check_out()
            self.click_check_out()
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "product_page_clutter_failure")
            self.logger.error(f"Failed in product_page_clutter flow: {e}")
            raise

    def product_page_clutter2(self):
        """
        Method name: product_page_clutter2
        Author name: Saptarshi
        Short description of method:
            Executes product flow for test case 4 (verify add basket -> verify minutes -> sleep -> add basket -> sleep -> checkout)
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.verify_the_add_basket_button()
            self.verify_the_keyword_minutes()
            self.click_add_to_basket()
            self.click_check_out()
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "product_page_clutter2_failure")
            self.logger.error(f"Failed in product_page_clutter2 flow: {e}")
            raise