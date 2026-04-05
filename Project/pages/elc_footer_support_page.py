from uistore.elc_footer_support_locators import ElcFooterSupportLocators
from utilities.webDriverHelper import WebDriverHelper
from utilities.screenshot import Screenshot


class ElcFooterSupportPage:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.helper = WebDriverHelper(self.driver)

    # ---------------- PAGE ACTION METHODS ----------------

    def open_contact_us_page(self):
        try:
            self.helper.click(ElcFooterSupportLocators.ACCEPT_COOKIES_BUTTON)
            self.helper.click(ElcFooterSupportLocators.FOOTER_CONTACT_US_LINK)
            self.logger.info("Contact Us page opened")
        except Exception as e:
            self.logger.error(f"Failed to open Contact Us page: {e}")
            raise
        # Method Name   : open_contact_us_page
        # Author        : sasi kumar
        # Description   : Opens the Contact Us page from ELC footer section
        # Return Type   : None
        # Parameters    : None

    def open_delivery_options_page(self):
        try:
            self.driver.back()
            self.helper.js_scroll(ElcFooterSupportLocators.FOOTER_DELIVERY_OPTIONS_LINK)
            self.helper.click(ElcFooterSupportLocators.FOOTER_DELIVERY_OPTIONS_LINK)
            self.logger.info("Delivery Options page opened")
        except Exception as e:
            self.logger.error(f"Failed to open Delivery Options page: {e}")
            raise
        # Method Name   : open_delivery_options_page
        # Author        : sasi kumar
        # Description   : Opens the Delivery Options page from footer links
        # Return Type   : None
        # Parameters    : None

    def open_product_safety_page(self):
        try:
            self.driver.back()
            self.helper.js_scroll(
                ElcFooterSupportLocators.FOOTER_PRODUCT_SAFETY_NOTICES_LINK
            )
            self.helper.click(
                ElcFooterSupportLocators.FOOTER_PRODUCT_SAFETY_NOTICES_LINK
            )
            self.logger.info("Product Safety page opened")
        except Exception as e:
            self.logger.error(f"Failed to open Product Safety page: {e}")
            raise
        # Method Name   : open_product_safety_page
        # Author        : sasi kumar
        # Description   : Opens the Product Safety Notices page from footer
        # Return Type   : None
        # Parameters    : None

    def open_returns_page(self):
        try:
            self.driver.back()
            self.helper.js_scroll(ElcFooterSupportLocators.FOOTER_RETURNS_LINK)
            self.helper.click(ElcFooterSupportLocators.FOOTER_RETURNS_LINK)
            self.logger.info("Returns page opened")
        except Exception as e:
            self.logger.error(f"Failed to open Returns page: {e}")
            raise
        # Method Name   : open_returns_page
        # Author        : sasi kumar
        # Description   : Opens the Returns policy page from footer
        # Return Type   : None
        # Parameters    : None

    def open_track_your_order_page(self):
        try:
            self.driver.back()
            self.helper.js_scroll(
                ElcFooterSupportLocators.FOOTER_TRACK_YOUR_ORDER_LINK
            )
            self.helper.click(
                ElcFooterSupportLocators.FOOTER_TRACK_YOUR_ORDER_LINK
            )
            self.logger.info("Track Your Order page opened")
        except Exception as e:
            self.logger.error(f"Failed to open Track Your Order page: {e}")
            raise
        # Method Name   : open_track_your_order_page
        # Author        : sasi kumar
        # Description   : Navigates to Track Your Order page via footer
        # Return Type   : None
        # Parameters    : None

    def open_help_center_page(self):
        try:
            self.driver.back()
            self.helper.js_scroll(ElcFooterSupportLocators.FOOTER_HELP_CENTRE_LINK)
            self.helper.click(ElcFooterSupportLocators.FOOTER_HELP_CENTRE_LINK)
            self.logger.info("Help Center page opened")
        except Exception as e:
            self.logger.error(f"Failed to open Help Center page: {e}")
            raise
        # Method Name   : open_help_center_page
        # Author        : sasi kumar
        # Description   : Opens the Help Centre page from footer
        # Return Type   : None
        # Parameters    : None

    def open_privacy_policy_page(self):
        try:
            self.driver.back()
            self.helper.js_scroll(
                ElcFooterSupportLocators.FOOTER_PRIVACY_POLICY_LINK
            )
            self.helper.click(
                ElcFooterSupportLocators.FOOTER_PRIVACY_POLICY_LINK
            )
            self.logger.info("Privacy Policy page opened")
        except Exception as e:
            self.logger.error(f"Failed to open Privacy Policy page: {e}")
            raise
        # Method Name   : open_privacy_policy_page
        # Author        : sasi kumar
        # Description   : Opens the Privacy Policy page from footer
        # Return Type   : None
        # Parameters    : None

    def open_how_to_complain_page(self):
        try:
            self.driver.back()
            self.helper.js_scroll(
                ElcFooterSupportLocators.FOOTER_HOW_TO_COMPLAIN_LINK
            )
            self.helper.click(
                ElcFooterSupportLocators.FOOTER_HOW_TO_COMPLAIN_LINK
            )
            self.logger.info("How To Complain page opened")
        except Exception as e:
            self.logger.error(f"Failed to open How To Complain page: {e}")
            raise
        # Method Name   : open_how_to_complain_page
        # Author        : sasi kumar
        # Description   : Opens the How To Complain page from footer
        # Return Type   : None
        # Parameters    : None

    # ---------------- SOFT VERIFICATION HELPERS ----------------

    def soft_verify_url(self, expected, page_name):
        try:
            if expected in self.driver.current_url:
                self.logger.info(f"{page_name} URL verified")
            else:
                raise AssertionError
        except AssertionError:
            self.logger.error(
                f"{page_name} URL mismatch. Current URL: {self.driver.current_url}"
            )
            Screenshot.capture_screenshot(self.driver, f"{page_name}_url_failed")
        # Method Name   : soft_verify_url
        # Author        : sasi kumar
        # Description   : Soft verifies current URL against expected value
        # Return Type   : None
        # Parameters    : expected(str), page_name(str)

    def soft_verify_title(self, expected, page_name):
        try:
            if expected in self.driver.title:
                self.logger.info(f"{page_name} title verified")
            else:
                raise AssertionError
        except AssertionError:
            self.logger.error(
                f"{page_name} title mismatch. Current title: {self.driver.title}"
            )
            Screenshot.capture_screenshot(self.driver, f"{page_name}_title_failed")
        # Method Name   : soft_verify_title
        # Author        : sasi kumar
        # Description   : Soft verifies page title against expected value
        # Return Type   : None
        # Parameters    : expected(str), page_name(str)

    # ---------------- TEST FLOW ----------------

    def elc_footer_pages_flow(self):
        self.open_contact_us_page()
        self.soft_verify_url(
            "theentertainer.zendesk.com/hc/en-gb/articles/6495305266833",
            "Contact_Us"
        )
        self.soft_verify_title("Contact Us", "Contact_Us")

        self.open_delivery_options_page()
        self.soft_verify_url(
            "theentertainer.zendesk.com/hc/en-gb/articles/6480509734289",
            "Delivery_Options"
        )
        self.soft_verify_title("Delivery options", "Delivery_Options")

        self.open_product_safety_page()
        self.soft_verify_url(
            "elc.co.uk/product-safety-notices",
            "Product_Safety"
        )
        self.soft_verify_title("Product Safety", "Product_Safety")

        self.open_returns_page()
        self.soft_verify_url(
            "theentertainer.zendesk.com/hc/en-gb/articles/4402417396241",
            "Returns"
        )
        self.soft_verify_title("Returns", "Returns")

        self.open_track_your_order_page()
        self.soft_verify_url(
            "elc.co.uk/login",
            "Track_Your_Order"
        )
        self.soft_verify_title("Login", "Track_Your_Order")

        self.open_help_center_page()
        self.soft_verify_url(
            "theentertainer.zendesk.com/hc/en-gb",
            "Help_Center"
        )
        self.soft_verify_title("The Entertainer", "Help_Center")

        self.open_privacy_policy_page()
        self.soft_verify_url(
            "elc.co.uk/privacy",
            "Your_Privacy"
        )
        self.soft_verify_title("Privacy", "Your_Privacy")

        self.open_how_to_complain_page()
        self.soft_verify_url(
            "theentertainer.zendesk.com/hc/en-gb/articles/32765165894801",
            "How_To_Complain"
        )
        self.soft_verify_title("How to complain", "How_To_Complain")
        # Method Name   : elc_footer_pages_flow
        # Author        : sasi kumar
        # Description   : Executes end-to-end navigation and validation of ELC footer pages
        # Return Type   : None
        # Parameters    : None