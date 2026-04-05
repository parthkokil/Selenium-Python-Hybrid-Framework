from utilities.webDriverHelper import WebDriverHelper
from uistore.soft_toys_locators import SoftToysLocators
from utilities.screenshot import Screenshot
from time import sleep

class SoftToysPage:
    """
    Page Class Name: SoftToysPage
    Author: Karuna Narayankar
    Description: Handles actions and verifications on the Soft Toys page
    """

    def __init__(self, driver, logger):
        """
        Method Name: __init__
        Description: Initializes SoftToysPage with driver and logger
        Parameters: driver (WebDriver), logger (Logger)
        Return Type: None
        """
        try:
            self.driver = driver
            self.logger = logger
            self.helper = WebDriverHelper(self.driver)
            self.logger.info("SoftToysPage initialized successfully")
        except Exception as e:
            self.logger.error(f"SoftToysPage initialization failed: {e}")
            raise

    def verify_logo(self):
        """
        Method Name: verify_logo
        Description: Verifies that the ELC logo is visible on the homepage
        Return Type: None
        """
        try:
            sleep(5)
            assert self.helper.is_element_visible(SoftToysLocators.ELC_LOGO_IMAGE)
            self.logger.info("ELC logo verified successfully on homepage")
            Screenshot.capture_screenshot(self.driver, "softtoys_logo_verified")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "softtoys_logo_error")
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
            Screenshot.capture_screenshot(self.driver, "softtoys_page_load_error")
            self.logger.error(f"Page load verification failed: {e}")
            raise

    def close_popup(self):
        """
        Method Name: close_popup
        Description: Closes the cookie consent popup
        Return Type: None
        """
        try:
            sleep(5)
            self.helper.click(SoftToysLocators.ACCEPT_COOKIES_BUTTON)
            self.logger.info("Popup closed successfully")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "softtoys_popup_error")
            self.logger.error(f"Failed to close popup: {e}")
            raise

    def hover_on_type_of_toy(self):
        """
        Method Name: hover_on_type_of_toy
        Description: Hovers over 'Type of toy' menu
        Return Type: None
        """
        try:
            sleep(3)
            self.helper.hover(SoftToysLocators.TYPE_OF_TOY_MENU)
            self.logger.info("Hovered on 'Type of toy' successfully")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "softtoys_hover_error")
            self.logger.error(f"Failed to hover on 'Type of toy': {e}")
            raise

    def click_soft_toys(self):
        """
        Method Name: click_soft_toys
        Description: Clicks on 'Soft Toys' link
        Return Type: None
        """
        try:
            sleep(3)
            self.helper.click(SoftToysLocators.SOFT_TOYS_CATEGORY_LINK)
            self.logger.info("Clicked on 'Soft Toys' successfully")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "softtoys_click_error")
            self.logger.error(f"Failed to click 'Soft Toys': {e}")
            raise

    def verify_url(self):
        """
        Method Name: verify_url
        Description: Verifies that the current URL contains 'soft-toys'
        Return Type: None
        """
        try:
            sleep(3)
            self.helper.verify_url("soft-toys")
            self.logger.info("Verified URL contains 'soft-toys'")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "softtoys_url_error")
            self.logger.error(f"URL verification failed: {e}")
            raise

    def clicks(self):
        """
        Method Name: clicks
        Description: Performs clicks on 'Dolls' and 'Soft Toys'
        Return Type: None
        """
        try:
            sleep(3)
            self.helper.click(SoftToysLocators.DOLLS_FILTER_ITEM)
            self.logger.info("Clicked on 'Dolls'")
            sleep(2)
            self.helper.click(SoftToysLocators.SOFT_TOYS_FILTER_OPTION)
            self.logger.info("Clicked on 'Soft Toys'")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "softtoys_clicks_error")
            self.logger.error(f"Failed during clicks sequence: {e}")
            raise

    def verify_keyword_brand(self):
        """
        Method Name: verify_keyword_brand
        Description: Verifies 'Brands' keyword and clicks 'Stimulating senses'
        Return Type: None
        """
        try:
            sleep(3)
            self.helper.verify_text(SoftToysLocators.BRANDS_SECTION_HEADER, "Brands")
            self.logger.info("Verified 'Brands' keyword successfully")
            self.helper.click(SoftToysLocators.STIMULATING_SENSES_FILTER)
            self.logger.info("Clicked on 'Stimulating senses'")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "softtoys_brands_error")
            self.logger.error(f"Failed to verify 'Brands' keyword: {e}")
            raise

    def verify_relevant_content(self):
        """
        Method Name: verify_relevant_content
        Description: Verifies that relevant content heading is visible
        Return Type: None
        """
        try:
            assert self.helper.is_element_visible(SoftToysLocators.PAGE_HEADING_TEXT)
            self.logger.info("Relevant content verified successfully")
            Screenshot.capture_screenshot(self.driver, "softtoys_relevant_content")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "softtoys_relevant_content_error")
            self.logger.error(f"Failed to verify relevant content: {e}")
            raise

    def click_first_product_and_add_cart(self):
        """
        Method Name: click_first_product_and_add_cart
        Description: Clicks first product, verifies 'Home Delivery', adds to basket, verifies 'Home'
        Return Type: None
        """
        try:
            sleep(3)
            self.helper.click(SoftToysLocators.FIRST_PRODUCT_CARD)
            self.logger.info("Clicked on first product")
            sleep(3)
            self.helper.verify_text(SoftToysLocators.HOME_DELIVERY_STATUS_TEXT, "Home Delivery")
            self.logger.info("Verified 'Home Delivery'")
            self.helper.click(SoftToysLocators.ADD_TO_BASKET_BUTTON)
            self.logger.info("Clicked on 'Add to Basket'")
            self.helper.click(SoftToysLocators.CONTINUE_SHOPPING_LINK)
            self.logger.info("Clicked on 'Continue Shopping'")
            sleep(2)
            self.helper.verify_text(SoftToysLocators.HOME_DELIVERY_LABEL, "Home")
            self.logger.info("Verified 'Home' keyword successfully")
            Screenshot.capture_screenshot(self.driver, "softtoys_cart")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "softtoys_cart_error")
            self.logger.error(f"Failed to add product to cart: {e}")
            raise

    def clutter2(self):
        """
        Method Name: clutter2
        Description: Executes full test flow for Soft Toys page
        Return Type: None
        """
        try:
            self.verify_logo()
            self.close_popup()
            self.hover_on_type_of_toy()
            self.click_soft_toys()
            self.verify_url()
            self.clicks()
            self.verify_keyword_brand()
            self.verify_relevant_content()
            self.click_first_product_and_add_cart()
            self.logger.info("Soft Toys flow executed successfully")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "softtoys_flow_error")
            self.logger.error(f"Soft Toys flow execution failed: {e}")
            raise