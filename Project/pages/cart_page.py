from utilities.webDriverHelper import WebDriverHelper
from uistore.cart_page_locator import CartPageLocator
from utilities.screenshot import Screenshot
from time import sleep


class CartPage:
    def __init__(self, driver, logger):
        """
        Method name: __init__
        Author name: Saptarshi
        Short description of method:
            Initializes the Cart page object with required utilities
        Return type:
            None
        Parameter list:
            driver, logger
        """
        try:
            self.driver = driver
            self.logger = logger
            self.helper = WebDriverHelper(self.driver)
            self.logger.info("CartPage initialized successfully")
        except Exception as e:
            self.logger.error(f"Error initializing CartPage: {e}")
            raise

    # to check it's a cart page
    def verify_cart_page(self):
        """
        Method name: verify_cart_page
        Author name: Saptarshi
        Short description of method:
            Verifies that the current URL contains 'cart'
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.helper.verify_url("cart")
            self.logger.info("Verified url of cart page")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_cart_page_failure")
            self.logger.error(f"Failed to verify cart page URL: {e}")
            raise

    def close_the_pop_up(self):
        """
        Method name: close_the_pop_up
        Author name: Saptarshi
        Short description of method:
            Closes the cart pop-up using JavaScript click
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.helper.js_click(CartPageLocator.pop_up)
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "close_the_pop_up_failure")
            self.logger.error(f"Failed to close the pop-up: {e}")
            raise

    def verify_the_text_continue_shopping(self):
        """
        Method name: verify_the_text_continue_shopping
        Author name: Saptarshi
        Short description of method:
            Verifies the 'Continue Shopping' text is present and captures screenshot
        Return type:
            None
        Parameter list:
            None
        """
        try:
            # el = self.driver.find_element(*CartPageLocator.continue_button)
            # txt = el.get_attribute("innerText").strip()  # more reliable than .text
            # self.helper.verify_text(CartPageLocator.continue_button, "innerText")
            self.helper.verify_attribute(CartPageLocator.continue_button,"innerText","Continue Shopping")
            self.logger.info("Continue shopping text present")
            Screenshot.capture_screenshot(self.driver, "cart")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_the_text_continue_shopping_failure")
            self.logger.error(f"Failed to verify Continue Shopping text: {e}")
            raise

    def cart_page_clutter(self):
        """
        Method name: cart_page_clutter
        Author name: Saptarshi
        Short description of method:
            Executes the complete Cart page flow (sleep -> url verify -> close popup -> verify text)
        Return type:
            None
        Parameter list:
            None
        """
        try:
            sleep(3)
            self.verify_cart_page()
            self.close_the_pop_up()
            self.verify_the_text_continue_shopping()
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "cart_page_clutter_failure")
            self.logger.error(f"Failed in cart_page_clutter flow: {e}")
            raise