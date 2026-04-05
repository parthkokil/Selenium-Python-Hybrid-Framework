from time import sleep
from uistore.explore_page_locators import ExplorePageLocators
from utilities.webDriverHelper import WebDriverHelper
from utilities.screenshot import Screenshot


class ExplorePage:

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.helper = WebDriverHelper(driver)

    def accept_cookies(self):
        try:
            self.helper.click(ExplorePageLocators.ACCEPT_ALL_COOKIES_BUTTON)
            self.logger.info("Cookies accepted")
        except Exception as e:
            self.logger.exception("Accept cookies failed")
            raise AssertionError("Unable to accept cookies") from e

    def verify_elc_logo_visible(self):
        try:
            self.helper.is_element_visible(ExplorePageLocators.ELC_LOGO_IMAGE)
            self.logger.info("ELC logo is visible")
        except Exception as e:
            self.logger.exception("ELC logo verification failed")
            raise AssertionError("ELC logo not visible") from e

    def hover_on_explore(self):
        try:
            sleep(2)
            self.helper.hover(ExplorePageLocators.EXPLORE_LINK)
            self.logger.info("Hovered on Explore")
        except Exception as e:
            self.logger.exception("Hover on Explore failed")
            raise AssertionError("Unable to hover on Explore") from e

    def click_gift_cards(self):
        try:
            self.helper.click(ExplorePageLocators.GIFT_CARDS_LINK)
            self.helper.verify_url("Gift")
            self.logger.info("Gift Cards page opened")
        except Exception as e:
            self.logger.exception("Gift Cards navigation failed")
            raise AssertionError("Unable to open Gift Cards") from e

    def click_offers_and_verify_brands(self):
        try:
            self.helper.click(ExplorePageLocators.OFFERS_LINK)
            self.helper.verify_text(ExplorePageLocators.BRANDS_LINK, "Brands")
            self.logger.info("Offers page verified")
        except Exception as e:
            self.logger.exception("Offers verification failed")
            raise AssertionError("Offers page validation failed") from e

    def click_dolls(self):
        try:
            self.helper.click(ExplorePageLocators.DOLLS_LINK)
            self.logger.info("Clicked Dolls category")
        except Exception as e:
            self.logger.exception("Click Dolls failed")
            raise AssertionError("Unable to click Dolls") from e

    def click_first_product(self):
        try:
            sleep(2)
            self.helper.click(ExplorePageLocators.FIRST_PRODUCT_CARD)
            self.helper.verify_text(ExplorePageLocators.EXPLORE_LINK, "Explore")
            self.logger.info("First doll product opened")
        except Exception as e:
            self.logger.exception("First product selection failed")
            raise AssertionError("Unable to open first doll product") from e

    def add_to_basket(self):
        try:
            self.helper.click(ExplorePageLocators.ADD_TO_BASKET_BUTTON)
            self.logger.info("Product added to basket")
        except Exception as e:
            self.logger.exception("Add to basket failed")
            raise AssertionError("Unable to add product to basket") from e

    def checkout_and_verify_order_total(self):
        try:
            self.helper.click(ExplorePageLocators.CHECK_OUT_BUTTON)
            self.helper.verify_text(ExplorePageLocators.ORDER_TOTAL_TEXT, "Order Total")
            Screenshot.capture_screenshot(self.driver, "order_total")
            self.logger.info("Checkout successful")
        except Exception as e:
            self.logger.exception("Checkout failed")
            raise AssertionError("Checkout validation failed") from e

    def run_test_case_6_flow(self):
        self.accept_cookies()
        self.verify_elc_logo_visible()
        self.hover_on_explore()
        self.click_gift_cards()
        self.click_offers_and_verify_brands()
        self.click_dolls()
        self.click_first_product()
        self.add_to_basket()
        self.checkout_and_verify_order_total()