from utilities.webDriverHelper import WebDriverHelper
from uistore.newborn_gifts_locators import NewbornGiftsLocators
from utilities.screenshot import Screenshot
from time import sleep

class NewbornGiftsPage:
    """
    Page Class Name: NewbornGiftsPage
    Author: Karuna Narayankar
    Description: Handles actions and verifications on the Newborn Gifts page
    """

    def __init__(self, driver, logger):
        """
        Method Name: __init__
        Author: Karuna Narayankar
        Description: Initializes NewbornGiftsPage with driver and logger
        Parameters: driver (WebDriver), logger (Logger)
        Return Type: None
        """
        try:
            self.driver = driver
            self.logger = logger
            self.helper = WebDriverHelper(self.driver)
            self.logger.info("NewbornGiftsPage initialized successfully")
        except Exception as e:
            self.logger.error(f"NewbornGiftsPage initialization failed: {e}")
            raise

    def verify_logo(self):
        """
        Method Name: verify_logo
        Description: Verifies that the ELC logo is visible on the homepage
        Return Type: None
        """
        try:
            sleep(3)
            assert self.helper.is_element_visible(NewbornGiftsLocators.ELC_LOGO_IMAGE)
            self.logger.info("ELC logo verified successfully on homepage")
            Screenshot.capture_screenshot(self.driver, "elc_logo_verified")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "elc_logo_verification_error")
            self.logger.error(f"Failed to verify ELC logo: {e}")
            raise

    def wait_until_the_page_loaded(self):
        """
        Method Name: wait_until_the_page_loaded
        Description: Verifies page URL and footer visibility to confirm page load
        Return Type: None
        """
        try:
            self.helper.verify_url("skills")
            self.logger.info("Verified URL contains 'skills'")
            is_visible = self.helper.is_footer_visible_by_tag(self.driver, "footer")
            if is_visible:
                self.logger.info("Footer tag is visible, page loaded successfully")
            else:
                raise AssertionError("Page load failed: Footer tag not visible")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "page_load_error")
            self.logger.error(f"Page load verification failed: {e}")
            raise

    def close_popup(self):
        """
        Method Name: close_popup
        Description: Closes the cookie consent popup
        Return Type: None
        """
        try:
            sleep(3)
            self.helper.click(NewbornGiftsLocators.ACCEPT_COOKIES_BUTTON)
            self.logger.info("Popup closed successfully")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "popup_close_error")
            self.logger.error(f"Failed to close popup: {e}")
            raise

    def hover_on_shop_by_age(self):
        """
        Method Name: hover_on_shop_by_age
        Description: Hovers over 'Shop by age' menu
        Return Type: None
        """
        try:
            sleep(3)
            self.helper.hover(NewbornGiftsLocators.SHOP_BY_AGE_MENU)
            self.logger.info("Hovered on 'Shop by age' successfully")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "hover_shop_by_age_error")
            self.logger.error(f"Failed to hover on 'Shop by age': {e}")
            raise

    def click_newborn_gifts(self):
        """
        Method Name: click_newborn_gifts
        Description: Clicks on 'Newborn Gifts' link
        Return Type: None
        """
        try:
            sleep(3)
            self.helper.click(NewbornGiftsLocators.NEWBORN_GIFTS_LINK)
            self.logger.info("Clicked on 'Newborn Gifts' successfully")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_newborn_gifts_error")
            self.logger.error(f"Failed to click 'Newborn Gifts': {e}")
            raise

    def verify_url(self):
        """
        Method Name: verify_url
        Description: Verifies that the current URL contains 'new-born-baby-gift-ideas'
        Return Type: None
        """
        try:
            self.helper.verify_url("new-born-baby-gift-ideas")
            self.logger.info("Verified URL contains 'new-born-baby-gift-ideas'")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_url_error")
            self.logger.error(f"URL verification failed: {e}")
            raise

    def clicks(self):
        """
        Method Name: clicks
        Description: Performs multiple clicks on filters (Show more, Baby Activity Toys, ELC, Hand Eye Coordination)
        Return Type: None
        """
        try:
            self.helper.click(NewbornGiftsLocators.SHOW_MORE_BUTTON)
            self.logger.info("Clicked on 'Show more'")
            sleep(3)
            self.helper.click(NewbornGiftsLocators.BABY_ACTIVITY_TOYS_FILTER)
            self.logger.info("Clicked on 'Baby Activity Toys'")
            sleep(3)
            self.helper.click(NewbornGiftsLocators.EARLY_LEARNING_CENTRE_FILTER)
            self.logger.info("Clicked on 'Early Learning Centre'")
            sleep(3)
            self.helper.click(NewbornGiftsLocators.HAND_EYE_COORDINATION_FILTER)
            self.logger.info("Clicked on 'Hand Eye Coordination'")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "clicks_error")
            self.logger.error(f"Failed during clicks sequence: {e}")
            raise

    def verify_relevant_content(self):
        """
        Method Name: verify_relevant_content
        Description: Verifies that relevant content heading is visible
        Return Type: None
        """
        try:
            assert self.helper.is_element_visible(NewbornGiftsLocators.PAGE_HEADING_TEXT)
            self.logger.info("Relevant content verified successfully")
            Screenshot.capture_screenshot(self.driver, "relevant_content_verified")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "relevant_content_error")
            self.logger.error(f"Failed to verify relevant content: {e}")
            raise

    def click_first_product_and_add_cart(self):
        """
        Method Name: click_first_product_and_add_cart
        Description: Clicks first product, adds to basket, verifies 'Home' keyword, captures screenshot
        Return Type: None
        """
        try:
            sleep(3)
            self.helper.click(NewbornGiftsLocators.FIRST_PRODUCT_CARD)
            self.logger.info("Clicked on first product")
            sleep(3)
            self.helper.click(NewbornGiftsLocators.ADD_TO_BASKET_BUTTON)
            self.logger.info("Clicked on 'Add to Basket'")
            sleep(2)
            self.helper.click(NewbornGiftsLocators.CONTINUE_SHOPPING_LINK)
            self.logger.info("Clicked on 'Continue Shopping'")
            sleep(2)
            self.helper.verify_text(NewbornGiftsLocators.HOME_DELIVERY_RADIO, "Home")
            self.logger.info("Verified 'Home' keyword successfully")
            Screenshot.capture_screenshot(self.driver, "gift_added_to_cart")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "add_cart_error")
            self.logger.error(f"Failed to add product to cart: {e}")
            raise

    def clutter(self):
        """
        Method Name: clutter
        Description: Executes full test flow for Newborn Gifts page
        Return Type: None
        """
        try:
            self.verify_logo()
            self.close_popup()
            self.hover_on_shop_by_age()
            self.click_newborn_gifts()
            self.verify_url()
            self.clicks()
            self.click_first_product_and_add_cart()
            self.logger.info("Clutter flow executed successfully")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "clutter_flow_error")
            self.logger.error(f"Clutter flow execution failed: {e}")
            raise