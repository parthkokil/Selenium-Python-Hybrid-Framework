from time import sleep
from uistore.brands_page_locators import BrandsPageLocators
from utilities.webDriverHelper import WebDriverHelper
from utilities.screenshot import Screenshot


class BrandsPage:

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.helper = WebDriverHelper(driver)

    def verify_elc_logo_visible(self):
        try:
            self.helper.is_element_visible(BrandsPageLocators.ELC_LOGO_IMAGE)
            self.logger.info("ELC logo is visible")
        except Exception as e:
            self.logger.exception("ELC logo verification failed")
            raise AssertionError("ELC logo not visible") from e

    def accept_cookies(self):
        try:
            self.helper.click(BrandsPageLocators.ACCEPT_ALL_COOKIES_BUTTON)
            self.logger.info("Cookies accepted")
        except Exception as e:
            self.logger.exception("Accept cookies failed")
            raise AssertionError("Unable to accept cookies") from e

    def hover_on_brands(self):
        try:
            sleep(2)
            self.helper.hover(BrandsPageLocators.BRANDS_LINK)
            self.logger.info("Hovered on Brands")
        except Exception as e:
            self.logger.exception("Hover on Brands failed")
            raise AssertionError("Unable to hover on Brands") from e

    def click_paw_patrol(self):
        try:
            self.helper.click(BrandsPageLocators.PAW_PATROL_LINK)
            self.logger.info("Clicked Paw Patrol")
        except Exception as e:
            self.logger.exception("Click Paw Patrol failed")
            raise AssertionError("Unable to click Paw Patrol") from e

    def wait_for_page_load(self):
        try:
            self.helper.verify_url("paw-patrol")
            footer_visible = self.helper.is_footer_visible_by_tag(self.driver, "footer")
            if not footer_visible:
                raise AssertionError("Footer not visible")
            self.logger.info("Paw Patrol page loaded successfully")
        except Exception as e:
            self.logger.exception("Page load validation failed")
            raise AssertionError("Paw Patrol page did not load properly") from e

    def click_playsets(self):
        try:
            self.helper.click(BrandsPageLocators.PLAYSETS_FILTER)
            self.logger.info("Clicked Playsets")
        except Exception as e:
            self.logger.exception("Click Playsets failed")
            raise AssertionError("Unable to click Playsets") from e

    def click_savings(self):
        try:
            self.helper.click(BrandsPageLocators.SAVINGS_FILTER)
            self.logger.info("Clicked Savings")
        except Exception as e:
            self.logger.exception("Click Savings failed")
            raise AssertionError("Unable to click Savings") from e

    def click_first_product(self):
        try:
            sleep(2)
            self.helper.click(BrandsPageLocators.FIRST_PRODUCT_THUMBNAIL)
            self.logger.info("Clicked first product")
        except Exception as e:
            self.logger.exception("Click first product failed")
            raise AssertionError("Unable to click first product") from e

    def verify_product_available(self):
        try:
            self.helper.verify_text(BrandsPageLocators.STORE_AVAILABILITY_TEXT, "Available")
            self.logger.info("Product availability verified")
        except Exception as e:
            self.logger.exception("Availability verification failed")
            raise AssertionError("Product not available") from e

    def add_to_basket(self):
        try:
            self.helper.click(BrandsPageLocators.ADD_TO_BASKET_BUTTON)
            self.logger.info("Added product to basket")
        except Exception as e:
            self.logger.exception("Add to basket failed")
            raise AssertionError("Unable to add product to basket") from e

    def proceed_to_checkout(self):
        try:
            self.helper.click(BrandsPageLocators.CHECK_OUT_BUTTON)
            self.logger.info("Clicked Checkout")
        except Exception as e:
            self.logger.exception("Checkout click failed")
            raise AssertionError("Unable to click Checkout") from e

    def verify_basket_and_capture_screenshot(self):
        try:
            self.helper.verify_text(BrandsPageLocators.BASKET_LABEL, "Basket")
            Screenshot.capture_screenshot(self.driver, "basket")
            self.logger.info("Basket verified and screenshot captured")
        except Exception as e:
            self.logger.exception("Basket verification failed")
            raise AssertionError("Basket page verification failed") from e

    def run_test_case_5_flow(self):
        self.verify_elc_logo_visible()
        self.accept_cookies()
        self.hover_on_brands()
        self.click_paw_patrol()
        self.wait_for_page_load()
        self.click_playsets()
        self.click_savings()
        self.click_first_product()
        self.verify_product_available()
        self.add_to_basket()
        self.proceed_to_checkout()
        self.verify_basket_and_capture_screenshot()