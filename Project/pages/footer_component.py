from utilities.web_driver_helper import WebDriverHelper
from utilities.screenshot import Screenshot
from uistore.footer_locators import FooterLocators
from utilities.excel_reader import ExcelReader
from time import sleep


class FooterComponentPage:
    def __init__(self, web_driver, logger):
        self.web_driver = web_driver
        self.logger = logger
        self.web_driver_helper = WebDriverHelper(self.web_driver)
        self.parent_window = self.web_driver.current_window_handle
        self.excel_reader = ExcelReader()
        self.logger.info("FooterComponentPage initialized")

        # ---------------- TestCase 9 ----------------

    def open_delivery_options_page(self):
        """
        # Method Name   : open_delivery_options_page
        # Author        : sasi kumar
        # Description   : Opens the Delivery Options page from footer links
        # Return Type   : None
        # Parameters    : None
        """
        try:
            self.web_driver.back()
            self.web_driver_helper.scroll_to_element_using_javascript(FooterLocators.footer_delivery_options_link)
            self.web_driver_helper.click_element(FooterLocators.footer_delivery_options_link)
            self.logger.info("Delivery Options page opened")
        except Exception as e:
            self.logger.error(f"Failed to open Delivery Options page: {e}")
            raise
    def open_product_safety_page(self):
        """
        # Method Name   : open_product_safety_page
        # Author        : sasi kumar
        # Description   : Opens the Product Safety Notices page from footer
        # Return Type   : None
        # Parameters    : None
        """
        try:
            self.web_driver.back()
            self.web_driver_helper.scroll_to_element_using_javascript(FooterLocators.footer_product_safety_notices_link)
            self.web_driver_helper.click_element(FooterLocators.footer_product_safety_notices_link)
            self.logger.info("Product Safety page opened")
        except Exception as e:
            self.logger.error(f"Failed to open Product Safety page: {e}")
            raise
    def open_returns_page(self):
        """
        # Method Name   : open_returns_page
        # Author        : sasi kumar
        # Description   : Opens the Returns policy page from footer
        # Return Type   : None
        # Parameters    : None
        """
        try:
            self.web_driver.back()
            self.web_driver_helper.scroll_to_element_using_javascript(FooterLocators.footer_returns_link)
            self.web_driver_helper.click_element(FooterLocators.footer_returns_link)
            self.logger.info("Returns page opened")
        except Exception as e:
            self.logger.error(f"Failed to open Returns page: {e}")
            raise
    def open_track_your_order_page(self):
        """
        # Method Name   : open_track_your_order_page
        # Author        : sasi kumar
        # Description   : Navigates to Track Your Order page via footer
        # Return Type   : None
        # Parameters    : None
        """
        try:
            self.web_driver.back()
            self.web_driver_helper.scroll_to_element_using_javascript(
                FooterLocators.footer_track_your_order_link
            )
            self.web_driver_helper.click_element(
                FooterLocators.footer_track_your_order_link
            )
            self.logger.info("Track Your Order page opened")
        except Exception as e:
            self.logger.error(f"Failed to open Track Your Order page: {e}")
            raise
    def open_help_center_page(self):
        """
        # Method Name   : open_help_center_page
        # Author        : sasi kumar
        # Description   : Opens the Help Centre page from footer
        # Return Type   : None
        # Parameters    : None
        """
        try:
            self.web_driver.back()
            self.web_driver_helper.scroll_to_element_using_javascript(FooterLocators.footer_help_center_link)
            self.web_driver_helper.click_element(FooterLocators.footer_help_center_link)
            self.logger.info("Help Center page opened")
        except Exception as e:
            self.logger.error(f"Failed to open Help Center page: {e}")
            raise
    def open_your_privacy_page(self):
        """
        # Method Name   : open_privacy_policy_page
        # Author        : sasi kumar
        # Description   : Opens the Privacy Policy page from footer
        # Return Type   : None
        # Parameters    : None
        """
        try:
            self.web_driver.back()
            self.web_driver_helper.scroll_to_element_using_javascript(FooterLocators.footer_your_privacy_link)
            self.web_driver_helper.click_element(FooterLocators.footer_your_privacy_link)
            self.logger.info("Privacy Policy page opened")
        except Exception as e:
            self.logger.error(f"Failed to open Privacy Policy page: {e}")
            raise
    def open_how_to_complain_page(self):
        """
        # Method Name   : open_how_to_complain_page
        # Author        : sasi kumar
        # Description   : Opens the How To Complain page from footer
        # Return Type   : None
        # Parameters    : None
        """
        try:
            self.web_driver.back()
            self.web_driver_helper.scroll_to_element_using_javascript(
                FooterLocators.footer_how_to_complain_link
            )
            self.web_driver_helper.click_element(
                FooterLocators.footer_how_to_complain_link
            )
            self.logger.info("How To Complain page opened")
        except Exception as e:
            self.logger.error(f"Failed to open How To Complain page: {e}")
            raise

    def soft_verify_url(self, expected, page_name):
        """
        # Method Name   : soft_verify_url
        # Author        : sasi kumar
        # Description   : Soft verifies current URL against expected value
        # Return Type   : None
        # Parameters    : expected(str), page_name(str)
        """
        try:
            if expected in self.web_driver.current_url:
                self.logger.info(f"{page_name} URL verified")
            else:
                raise AssertionError
        except AssertionError:
            self.logger.error(
                f"{page_name} URL mismatch. Current URL: {self.web_driver.current_url}"
            )
            Screenshot.capture_browser_screenshot(self.web_driver, f"{page_name}_url_failed")
    def soft_verify_title(self, expected, page_name):
        """
        # Method Name   : soft_verify_title
        # Author        : sasi kumar
        # Description   : Soft verifies page title against expected value
        # Return Type   : None
        # Parameters    : expected(str), page_name(str)
        """
        try:
            if expected in self.web_driver.title:
                self.logger.info(f"{page_name} title verified")
            else:
                raise AssertionError
        except AssertionError:
            self.logger.error(
                f"{page_name} title mismatch. Current title: {self.web_driver.title}")
            Screenshot.capture_browser_screenshot(self.web_driver, f"{page_name}_title_failed")

    # ---------------- TEST FLOW ----------------
    def elc_footer_help_links_flow(self):
        """
        # Method Name   : elc_footer_pages_flow
        # Author        : sasi kumar
        # Description   : Executes end-to-end navigation and validation of ELC footer pages
        # Return Type   : None
        # Parameters    : None
        """
        expected_contact_us_url = self.excel_reader.get_cell_value("sasiExcel",2,1)
        self.soft_verify_url(expected_contact_us_url,"Contact_Us")
        expected_contact_us_title = self.excel_reader.get_cell_value("sasiExcel",2,2)
        self.soft_verify_title(expected_contact_us_title, "Contact_Us")
        self.open_delivery_options_page()

        expected_delivery_options_url = self.excel_reader.get_cell_value("sasiExcel",3,1)
        self.soft_verify_url(expected_delivery_options_url,"Delivery_Options")
        expected_delivery_options_title = self.excel_reader.get_cell_value("sasiExcel", 3, 2)
        self.soft_verify_title(expected_delivery_options_title, "Delivery_Options")

        expected_product_safety_url = self.excel_reader.get_cell_value("sasiExcel",4,1)
        self.open_product_safety_page()
        self.soft_verify_url(expected_product_safety_url,"Product_Safety")
        expected_product_safety_title = self.excel_reader.get_cell_value("sasiExcel", 4, 2)
        self.soft_verify_title(expected_product_safety_title, "Product_Safety")

        expected_returns_url = self.excel_reader.get_cell_value("sasiExcel",5,1)
        self.open_returns_page()
        self.soft_verify_url(expected_returns_url,"Returns")
        expected_returns_title = self.excel_reader.get_cell_value("sasiExcel",5,2)
        self.soft_verify_title(expected_returns_title, "Returns")

        expected_track_your_order_url = self.excel_reader.get_cell_value("sasiExcel",6,1)
        self.open_track_your_order_page()
        self.soft_verify_url(expected_track_your_order_url,"Track_Your_Order")
        expected_track_your_order_title = self.excel_reader.get_cell_value("sasiExcel",6,2)
        self.soft_verify_title(expected_track_your_order_title, "Track_Your_Order")

        expected_help_center_url = self.excel_reader.get_cell_value("sasiExcel",7,1)
        self.open_help_center_page()
        self.soft_verify_url(expected_help_center_url,"Help_Center")
        expected_help_center_title = self.excel_reader.get_cell_value("sasiExcel", 7, 2)
        self.soft_verify_title(expected_help_center_title, "Help_Center")

        expected_your_privacy_url = self.excel_reader.get_cell_value("sasiExcel",8,1)
        self.open_your_privacy_page()
        self.soft_verify_url(expected_your_privacy_url,"Your_Privacy")
        expected_your_privacy_title = self.excel_reader.get_cell_value("sasiExcel", 8, 2)
        self.soft_verify_title(expected_your_privacy_title, "Your_Privacy")

        expected_how_to_complain_url = self.excel_reader.get_cell_value("sasiExcel",9,1)
        self.open_how_to_complain_page()
        self.soft_verify_url(expected_how_to_complain_url,"How_To_Complain")
        expected_how_to_complain_title = self.excel_reader.get_cell_value("sasiExcel", 9, 2)
        self.soft_verify_title(expected_how_to_complain_title, "How_To_Complain")


    # ---------------- TestCase 10 ----------------

    def verify_title_url(self):
        """
        Method Name   : verify_title_url
        Author        : Parth
        Description   : Verifies the About Us page title and URL and navigates back to the home page
        Return Type   : None
        Parameters    : None
        """
        try:
            self.logger.info("Verifying About Us page title")
            expected_about_us_page_title = self.excel_reader.get_cell_value("parthexcel", 2, 2)
            self.web_driver_helper.verify_page_title_contains(expected_about_us_page_title)

            self.logger.info("Verifying About Us page URL")
            expected_about_us_page_url = self.excel_reader.get_cell_value("parthexcel", 2, 1)
            self.web_driver_helper.verify_current_url_contains(expected_about_us_page_url)

            self.web_driver_helper.navigate_back()
            self.logger.info("Navigated back to home page from About Us")

        except Exception as exception:
            self.logger.error("Error while verifying About Us page")
            raise Exception(f"verify_title_url failed: {exception}")
    def click_on_store_finder_in_footer(self):
        """
        Method Name   : click_on_store_finder_in_footer
        Author        : Parth
        Description   : Clicks on Store Finder link from footer
        Return Type   : None
        Parameters    : None
        """
        try:
            self.logger.info("Clicking on Store Finder link in footer")
            self.web_driver_helper.click_element(FooterLocators.footer_store_finder_link)
        except Exception as exception:
            self.logger.error("Error while clicking Store Finder link")
            raise Exception(f"click_on_store_finder_in_footer failed: {exception}")
    def verify_page_title_url_store_finder(self):
        """
        Method Name   : verify_page_title_url_store_finder
        Author        : Parth
        Description   : Verifies Store Finder page title and URL and navigates back to home page
        Return Type   : None
        Parameters    : None
        """
        try:
            self.logger.info("Verifying Store Finder page title")

            expected_store_finder_page_title = self.excel_reader.get_cell_value("parthexcel", 3, 2)
            self.web_driver_helper.verify_page_title_contains(expected_store_finder_page_title)

            self.logger.info("Verifying Store Finder page URL")
            expected_store_finder_page_url = self.excel_reader.get_cell_value("parthexcel", 3, 1)
            self.web_driver_helper.verify_current_url_contains(expected_store_finder_page_url)

            self.web_driver_helper.navigate_back()
            self.logger.info("Navigated back to home page from Store Finder")

        except Exception as exception:
            self.logger.error("Error while verifying Store Finder page")
            raise Exception(f"verify_page_title_url_store_finder failed: {exception}")
    def click_on_wee_link(self):
        """
        Method Name   : click_on_wee_link
        Author        : Parth
        Description   : Clicks on WEEE Regulations link and switches to newly opened browser tab
        Return Type   : None
        Parameters    : None
        """
        try:
            self.logger.info("Clicking on WEEE Regulations link in footer")
            self.web_driver_helper.click_element(FooterLocators.footer_wee_regulations_link)

            self.logger.info("Waiting for new tab to open")
            sleep(1)

            self.web_driver_helper.switch_to_window_by_index(-1)
            self.logger.info("Switched to WEEE Regulations new tab")

        except Exception as exception:
            self.logger.error("Error while clicking WEEE Regulations link")
            raise Exception(f"click_on_wee_link failed: {exception}")
    def verify_wee_page(self):
        """
        Method Name   : verify_wee_page
        Author        : Parth
        Description   : Verifies WEEE page title and URL, closes the tab and switches back
        Return Type   : None
        Parameters    : None
        """
        try:
            self.logger.info("Verifying WEEE page title")
            expected_wee_page_title = self.excel_reader.get_cell_value("parthexcel", 4, 2)
            self.web_driver_helper.verify_page_title_contains(expected_wee_page_title)

            self.logger.info("Verifying WEEE page URL")
            expected_wee_page_url = self.excel_reader.get_cell_value("parthexcel", 4, 1)
            self.web_driver_helper.verify_current_url_contains(expected_wee_page_url)

            self.web_driver_helper.close_current_window()
            self.logger.info("Closed WEEE Regulations tab")

            self.web_driver.switch_to.window(self.parent_window)
            self.logger.info("Switched back to parent home page tab")

        except Exception as exception:
            self.logger.error("Error while verifying WEEE page")
            raise Exception(f"verify_wee_page failed: {exception}")
    def verify_useful_link(self):
        """
        Method Name   : verify_useful_link
        Author        : Parth
        Description   : Verifies presence of 'Useful links' text in the footer section
        Return Type   : None
        Parameters    : None
        """
        try:
            sleep(2)
            self.web_driver_helper.verify_text_contains(FooterLocators.useful_links_text,"Useful links")
            self.logger.info("Useful links keyword verified")

        except Exception as exception:
            self.logger.error("Error while verifying Useful links")
            raise Exception(f"verify_useful_link failed: {exception}")
    def click_on_press_link(self):
        """
        Method Name   : click_on_press_link
        Author        : Parth
        Description   : Clicks on the Press link present in the footer section
        Return Type   : None
        Parameters    : None
        """
        try:
            self.web_driver_helper.click_element(FooterLocators.footer_press_link)
            self.logger.info("Clicked on the Press link in footer")
        except Exception as exception:
            self.logger.error("Error while clicking Press link")
            raise Exception(f"click_on_press_link failed: {exception}")
    def verify_press_link(self):
        """
        Method Name   : verify_press_link
        Author        : Parth
        Description   : Verifies Press page title and URL and navigates back to home page
        Return Type   : None
        Parameters    : None
        """
        try:
            expected_press_page_title = self.excel_reader.get_cell_value("parthexcel", 5, 2)
            self.web_driver_helper.verify_page_title_contains(expected_press_page_title)
            self.logger.info("Press page title verified")
            expected_press_page_url = self.excel_reader.get_cell_value("parthexcel", 5, 1)
            self.web_driver_helper.verify_current_url_contains(expected_press_page_url)
            self.logger.info("Press page URL verified")

            self.web_driver_helper.navigate_back()
            self.logger.info("Navigated back to home page from Press")

        except Exception as exception:
            self.logger.error("Error while verifying Press page")
            raise Exception(f"verify_press_link failed: {exception}")
    def click_on_affiliates_link(self):
        """
        Method Name   : click_on_affiliates_link
        Author        : Parth
        Description   : Clicks on the Affiliates link present in the footer
        Return Type   : None
        Parameters    : None
        """
        try:
            self.web_driver_helper.click_element(FooterLocators.footer_affiliates_link)
            self.logger.info("Clicked on the Affiliates link in footer")
        except Exception as exception:
            self.logger.error("Error while clicking Affiliates link")
            raise Exception(f"click_on_affiliates_link failed: {exception}")
    def verify_affiliates_link(self):
        """
        Method Name   : verify_affiliates_link
        Author        : Parth
        Description   : Verifies Affiliates page title and URL and navigates back to home page
        Return Type   : None
        Parameters    : None
        """
        try:
            expected_affiliates_page_title = self.excel_reader.get_cell_value("parthexcel", 6, 2)
            self.web_driver_helper.verify_page_title_contains(expected_affiliates_page_title)
            self.logger.info("Affiliates page title verified")

            expected_affiliates_page_url = self.excel_reader.get_cell_value("parthexcel", 6, 1)
            self.web_driver_helper.verify_current_url_contains(expected_affiliates_page_url)
            self.logger.info("Affiliates page URL verified")

            self.web_driver_helper.navigate_back()
            self.logger.info("Navigated back to home page from Affiliates")

        except Exception as exception:
            self.logger.error("Error while verifying Affiliates page")
            raise Exception(f"verify_affiliates_link failed: {exception}")
    def click_on_careers_link(self):
        """
        Method Name   : click_on_careers_link
        Author        : Parth
        Description   : Clicks on the Careers link and switches to newly opened browser tab
        Return Type   : None
        Parameters    : None
        """
        try:
            self.web_driver_helper.click_element(FooterLocators.footer_careers_link)
            self.logger.info("Clicked on the Careers link in footer")

            self.web_driver_helper.switch_to_window_by_index(-1)
            self.logger.info("Switched to Careers new tab")

        except Exception as exception:
            self.logger.error("Error while clicking Careers link")
            raise Exception(f"click_on_careers_link failed: {exception}")
    def verify_careers_link(self):
        """
        Method Name   : verify_careers_link
        Author        : Parth
        Description   : Verifies Careers page title and URL, closes the tab and switches back
        Return Type   : None
        Parameters    : None
        """
        try:
            sleep(2)
            expected_careers_page_title = self.excel_reader.get_cell_value("parthexcel", 7, 2)
            self.web_driver_helper.verify_page_title_contains(expected_careers_page_title)
            self.logger.info("Careers page title verified")

            expected_careers_page_url = self.excel_reader.get_cell_value("parthexcel", 7, 1)
            self.web_driver_helper.verify_current_url_contains(expected_careers_page_url)
            self.logger.info("Careers page URL verified")

            self.web_driver_helper.close_current_window()
            self.web_driver.switch_to.window(self.parent_window)
            self.logger.info("Switched back to parent home page tab from Careers")

        except Exception as exception:
            self.logger.error("Error while verifying Careers page")
            raise Exception(f"verify_careers_link failed: {exception}")
    def click_on_gift_cards_link(self):
        """
        Method Name   : click_on_gift_cards_link
        Author        : Parth
        Description   : Clicks on the Gift Cards link present in the footer
        Return Type   : None
        Parameters    : None
        """
        try:
            sleep(2)
            self.web_driver_helper.click_element(FooterLocators.footer_gift_cards_link)
            self.logger.info("Clicked on the Gift Cards link in footer")
        except Exception as exception:
            self.logger.error("Error while clicking Gift Cards link")
            raise Exception(f"click_on_gift_cards_link failed: {exception}")
    def verify_gift_cards_link(self):
        """
        Method Name   : verify_gift_cards_link
        Author        : Parth
        Description   : Verifies Gift Cards page title and URL and navigates back to home page
        Return Type   : None
        Parameters    : None
        """
        try:
            expected_gift_cards_page_title = self.excel_reader.get_cell_value("parthexcel", 8, 2)
            self.web_driver_helper.verify_page_title_contains(expected_gift_cards_page_title)
            self.logger.info("Gift Cards page title verified")

            expected_gift_cards_page_url = self.excel_reader.get_cell_value("parthexcel", 8, 1)
            self.web_driver_helper.verify_current_url_contains(expected_gift_cards_page_url)
            self.logger.info("Gift Cards page URL verified")

            self.web_driver_helper.navigate_back()
            self.logger.info("Navigated back to home page from Gift Cards")

        except Exception as exception:
            self.logger.error("Error while verifying Gift Cards page")
            raise Exception(f"verify_gift_cards_link failed: {exception}")
    def click_on_klarna_link(self):
        """
        Method Name   : click_on_klarna_link
        Author        : Parth
        Description   : Clicks on the Klarna link present in the footer
        Return Type   : None
        Parameters    : None
        """
        try:
            self.web_driver_helper.click_element(FooterLocators.footer_klarna_link)
            self.logger.info("Clicked on the Klarna link in footer")
        except Exception as exception:
            self.logger.error("Error while clicking Klarna link")
            raise Exception(f"click_on_klarna_link failed: {exception}")
    def verify_klarna_link(self):
        """
        Method Name   : verify_klarna_link
        Author        : Parth
        Description   : Verifies Klarna page title and URL and navigates back to home page
        Return Type   : None
        Parameters    : None
        """
        try:
            expected_klarna_page_title = self.excel_reader.get_cell_value("parthexcel", 9, 2)
            self.web_driver_helper.verify_page_title_contains(expected_klarna_page_title)
            self.logger.info("Klarna page title verified")

            expected_klarna_page_url = self.excel_reader.get_cell_value("parthexcel", 9, 1)
            self.web_driver_helper.verify_current_url_contains(expected_klarna_page_url)
            self.logger.info("Klarna page URL verified")

            self.web_driver_helper.navigate_back()
            self.logger.info("Navigated back to home page from Klarna")

        except Exception as exception:
            self.logger.error("Error while verifying Klarna page")
            raise Exception(f"verify_klarna_link failed: {exception}")
    def capture_screenshot(self):
        """
        Method Name   : capture_screenshot
        Author        : Parth
        Description   : Captures screenshot for footer test case
        Return Type   : None
        Parameters    : None
        """
        try:
            self.logger.info("Capturing screenshot for footer test case")
            Screenshot.capture_browser_screenshot(self.web_driver, "case_10_footer")
            self.logger.info("Screenshot captured successfully")

        except Exception as exception:
            self.logger.error("Error while capturing screenshot")
            raise Exception(f"capture_screenshot failed: {exception}")
    def run_footer_links_flow(self):
        """
        Method Name   : run_footer_links_flow
        Author        : Parth
        Description   : Executes complete footer links validation flow in sequential order
        Return Type   : None
        Parameters    : None
        """
        try:
            self.verify_title_url()
            self.click_on_store_finder_in_footer()
            self.verify_page_title_url_store_finder()
            self.click_on_wee_link()
            self.verify_wee_page()
            self.click_on_press_link()
            self.verify_press_link()
            self.click_on_affiliates_link()
            self.verify_affiliates_link()
            self.click_on_careers_link()
            self.verify_careers_link()
            self.click_on_gift_cards_link()
            self.verify_gift_cards_link()
            self.click_on_klarna_link()
            self.verify_klarna_link()
            self.verify_useful_link()
            self.capture_screenshot()

            self.logger.info("Footer links flow executed successfully")

        except Exception as exception:
            self.logger.error("Footer links flow execution failed")
            raise Exception(f"run_footer_links_flow failed: {exception}")
 