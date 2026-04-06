from utilities.webDriverHelper import WebDriverHelper
from utilities.screenshot import Screenshot
from uistore.footer_links_locators import CaseTenLocators
from time import sleep

class CaseTenPage:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.helper = WebDriverHelper(self.driver)

        # Keep track of parent tab for new-tab cases
        self.parent_window = self.driver.current_window_handle

    # Step 2 + log requirement
    def scroll_footer(self):
        self.helper.click(CaseTenLocators.POP_UP)
        self.helper.js_scroll(CaseTenLocators.FOOTER_TOP)
        self.logger.info("scroll down")  # case sensitive requirement

    # -------------------- About us --------------------
    def click_on_about_us(self):
        self.scroll_footer()
        self.helper.click(CaseTenLocators.ABOUT_US)
        self.logger.info("click on the about us")

    def verify_title_url(self):
        self.helper.verify_title("About us | Early Learning Centre")
        self.logger.info("title verified")

        self.helper.verify_url("https://www.elc.co.uk/aboutus")
        self.logger.info("url verified")

        self.driver.back()
        self.logger.info("navigate back to home page done from about us")

    # -------------------- Store finder --------------------
    def click_on_store_finder_in_footer(self):
        self.helper.click(CaseTenLocators.STORE_FINDER)
        self.logger.info("click on the store finder in footer")

    def verify_page_title_url(self):
        self.helper.verify_title("Find A Store | The Entertainer")
        self.logger.info("title verified")

        self.helper.verify_url("https://www.thetoyshop.com/store-finder")
        self.logger.info("url verified")

        self.driver.back()
        self.logger.info("navigate back to home page done from store finder")

    # -------------------- WEEE Regulations (new tab) --------------------
    def click_on_link_footer(self):
        self.helper.click(CaseTenLocators.WEEE_REGULATIONS)
        self.logger.info("click on the wee regulations in footer")
        sleep(1)
        # Switch to newly opened tab
        self.helper.switch_to_new_window(-1)
        self.logger.info("switch to new tab done from wee regulations")

    def verify_page_title(self):
        sleep(1)
        self.helper.verify_title("WEEE, Batteries and Packaging")
        self.logger.info("title verified")

        self.helper.verify_url("https://www.thetoyshop.com/weee")
        self.logger.info("url verified")

        # Close new tab and go back to parent
        self.driver.close()
        self.driver.switch_to.window(self.parent_window)
        self.logger.info("back to home page tab from wee regulations")

    # -------------------- Press --------------------
    def click_on_press_link(self):
        self.helper.click(CaseTenLocators.PRESS)
        self.logger.info("click on the press in footer")

    def verify_press_link(self):
        self.helper.verify_title("Press Office | Early Learning Centre")
        self.logger.info("title verified")

        self.helper.verify_url("https://www.elc.co.uk/press")
        self.logger.info("url verified")

        self.driver.back()
        self.logger.info("navigate back to home page done from press")

    # -------------------- Affiliates --------------------
    def click_on_affiliates_link(self):
        self.helper.click(CaseTenLocators.AFFILIATES)
        self.logger.info("click on the affiliates in footer")

    def verify_affiliates_link(self):
        self.helper.verify_title("Affiliates | Early Learning Centre")
        self.logger.info("title verified")

        self.helper.verify_url("https://www.elc.co.uk/affiliates")
        self.logger.info("url verified")

        self.driver.back()
        self.logger.info("navigate back to home page done from affiliates")

    # -------------------- Careers (new tab) --------------------
    def click_on_careers_link(self):
        self.helper.click(CaseTenLocators.CAREERS)
        self.logger.info("click on the careers in footer")

        self.helper.switch_to_new_window(-1)
        self.logger.info("switch to new tab done from careers")

    def verify_careers_link(self):
        # Title can vary; we keep "Careers" keyword check by using contains in helper
        sleep(2)
        self.helper.verify_title("Careers - The Entertainer")
        self.logger.info("title verified")

        self.helper.verify_url("https://careers.thetoyshop.com/")
        self.logger.info("url verified")

        self.driver.close()
        self.driver.switch_to.window(self.parent_window)
        self.logger.info("back to home page tab from careers")

    # -------------------- Gift cards --------------------
    def click_on_gift_cards_link(self):
        sleep(2)
        self.helper.click(CaseTenLocators.GIFT_CARDS)
        self.logger.info("click on the gift cards in footer")

    def verify_gift_cards_link(self):
        # Title may differ based on product page; checking keyword is safer
        self.helper.verify_title("The Entertainer & Early Learning Centre Gift Card £10 | Early Learning Centre")
        self.logger.info("title verified")

        # Your expected URL is very long. Using contains match in helper.
        self.helper.verify_url("https://www.elc.co.uk/gift-cards/")
        self.logger.info("url verified")
        self.driver.back()
        self.logger.info("navigate back to home page done from gift cards")

    # -------------------- Klarna --------------------
    def click_on_klarna_link(self):
        self.helper.click(CaseTenLocators.KLARNA)
        self.logger.info("click on the klarna in footer")

    def verify_klarna_link(self):
        self.helper.verify_title("Buy Now ")
        self.logger.info("title verified")

        self.helper.verify_url("https://www.elc.co.uk/klarna")
        self.logger.info("url verified")

        self.driver.back()
        self.logger.info("navigate back to home page done from klarna")

    # -------------------- Step 19: Useful links --------------------
    def verify_useful_link(self):
        # Verifies keyword and record logs
        sleep(2)
        self.helper.verify_text(CaseTenLocators.USEFUL_LINKS_TEXT, "Useful links")
        self.logger.info("Useful links keyword verified")

    # -------------------- Step 20: Screenshot --------------------
    def capture_screenshot(self):
        Screenshot.capture_screenshot(self.driver, "case_10_footer")
        self.logger.info("screenshot captured for case 10")

    #  Clutter function (one-call execution)
    def run_case_ten(self):
        # About us
        self.click_on_about_us()
        self.verify_title_url()

        # Store finder
        self.click_on_store_finder_in_footer()
        self.verify_page_title_url()

        # WEEE (new tab)
        self.click_on_link_footer()
        self.verify_page_title()

        # Press
        self.click_on_press_link()
        self.verify_press_link()

        # Affiliates
        self.click_on_affiliates_link()
        self.verify_affiliates_link()

        # Careers (new tab)
        self.click_on_careers_link()
        self.verify_careers_link()

        # Gift cards
        self.click_on_gift_cards_link()
        self.verify_gift_cards_link()

        # Klarna
        self.click_on_klarna_link()
        self.verify_klarna_link()

        # Useful links
        self.verify_useful_link()

        # Screenshot
        self.capture_screenshot()
