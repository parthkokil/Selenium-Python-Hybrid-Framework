from pages.base_page import BasePage
from uistore.footer_locators import FooterLocators
from time import sleep

class FooterComponentPage(BasePage):
    """
    # Class Name    : FooterComponentPage
    # Author        : Sasi Kumar, Parth
    # Description   : Page object for footer section operations across the ELC website.
    #                 Inherits from BasePage and uses the unified match-case dispatcher.
    """

    def __init__(self, web_driver, logger):
        super().__init__(web_driver, logger)
        self.parent_window = self.web_driver.current_window_handle
        self.logger.info("FooterComponentPage initialized")

    def soft_verify_url(self, expected, page_name):
        try:
            if expected in self.web_driver.current_url:
                self.logger.info(f"{page_name} URL verified")
            else:
                raise AssertionError
        except AssertionError:
            self.logger.error(f"{page_name} URL mismatch")
            from utilities.screenshot import Screenshot
            Screenshot.capture_browser_screenshot(self.web_driver, f"{page_name}_url_failed")

    def soft_verify_title(self, expected, page_name):
        try:
            if expected in self.web_driver.title:
                self.logger.info(f"{page_name} title verified")
            else:
                raise AssertionError
        except AssertionError:
            self.logger.error(f"{page_name} title mismatch")
            from utilities.screenshot import Screenshot
            Screenshot.capture_browser_screenshot(self.web_driver, f"{page_name}_title_failed")

    def click_and_verify_footer_link(self, locator, expected_url, expected_title, page_name,
                                      navigate_back=True, opens_new_tab=False):
        """ Reusable utility specifically for footer link window routing """
        self.perform_action("CLICK", locator, page_name)
        
        if opens_new_tab:
            sleep(1)
            self.web_driver_helper.switch_to_window_by_index(-1)
            self.logger.info(f"Switched to '{page_name}' new tab")

        sleep(2)
        self.web_driver_helper.verify_page_title_contains(expected_title)
        self.perform_action("VERIFY_URL", expected_text=expected_url, element_name=page_name)

        if opens_new_tab:
            self.web_driver_helper.close_current_window()
            self.web_driver.switch_to.window(self.parent_window)
        elif navigate_back:
            self.web_driver.back()

    # ==========================================================================================
    # WORKFLOW FUNCTIONS
    # ==========================================================================================

    def elc_footer_help_links_flow(self):
        # Step 1: Contact Us 
        self.soft_verify_url(self.excel_reader.get_cell_value("sasiExcel", 2, 1), "Contact_Us")
        self.soft_verify_title(self.excel_reader.get_cell_value("sasiExcel", 2, 2), "Contact_Us")

        # Step 2: Delivery Options 
        self.web_driver.back()
        self.perform_action("SCROLL_AND_CLICK", FooterLocators.footer_delivery_options_link, "Delivery Options")
        self.soft_verify_url(self.excel_reader.get_cell_value("sasiExcel", 3, 1), "Delivery_Options")
        self.soft_verify_title(self.excel_reader.get_cell_value("sasiExcel", 3, 2), "Delivery_Options")

        # Step 3: Product Safety
        self.web_driver.back()
        self.perform_action("SCROLL_AND_CLICK", FooterLocators.footer_product_safety_notices_link, "Product Safety")
        self.soft_verify_url(self.excel_reader.get_cell_value("sasiExcel", 4, 1), "Product_Safety")

        # Step 4: Returns
        self.web_driver.back()
        self.perform_action("SCROLL_AND_CLICK", FooterLocators.footer_returns_link, "Returns")
        self.soft_verify_url(self.excel_reader.get_cell_value("sasiExcel", 5, 1), "Returns")

        # Step 5: Track Your Order
        self.web_driver.back()
        self.perform_action("SCROLL_AND_CLICK", FooterLocators.footer_track_your_order_link, "Track Your Order")
        self.soft_verify_url(self.excel_reader.get_cell_value("sasiExcel", 6, 1), "Track_Your_Order")

        # Step 6: Help Centre
        self.web_driver.back()
        self.perform_action("SCROLL_AND_CLICK", FooterLocators.footer_help_center_link, "Help Centre")
        self.soft_verify_url(self.excel_reader.get_cell_value("sasiExcel", 7, 1), "Help_Center")

        # Step 7: Your Privacy
        self.web_driver.back()
        self.perform_action("SCROLL_AND_CLICK", FooterLocators.footer_your_privacy_link, "Your Privacy")
        self.soft_verify_url(self.excel_reader.get_cell_value("sasiExcel", 8, 1), "Your_Privacy")

        # Step 8: How To Complain
        self.web_driver.back()
        self.perform_action("SCROLL_AND_CLICK", FooterLocators.footer_how_to_complain_link, "How To Complain")
        self.soft_verify_url(self.excel_reader.get_cell_value("sasiExcel", 9, 1), "How_To_Complain")

    def run_footer_links_flow(self):
        # About Us page verify
        self.web_driver_helper.verify_page_title_contains(self.excel_reader.get_cell_value("parthexcel", 2, 2))
        self.perform_action("VERIFY_URL", expected_text=self.excel_reader.get_cell_value("parthexcel", 2, 1), element_name="About Us")
        self.web_driver.back()

        # Footer links
        self.click_and_verify_footer_link(FooterLocators.footer_store_finder_link, self.excel_reader.get_cell_value("parthexcel", 3, 1), self.excel_reader.get_cell_value("parthexcel", 3, 2), "Store Finder")
        self.click_and_verify_footer_link(FooterLocators.footer_wee_regulations_link, self.excel_reader.get_cell_value("parthexcel", 4, 1), self.excel_reader.get_cell_value("parthexcel", 4, 2), "WEEE Regulations", opens_new_tab=True)
        self.click_and_verify_footer_link(FooterLocators.footer_press_link, self.excel_reader.get_cell_value("parthexcel", 5, 1), self.excel_reader.get_cell_value("parthexcel", 5, 2), "Press")
        self.click_and_verify_footer_link(FooterLocators.footer_affiliates_link, self.excel_reader.get_cell_value("parthexcel", 6, 1), self.excel_reader.get_cell_value("parthexcel", 6, 2), "Affiliates")
        self.click_and_verify_footer_link(FooterLocators.footer_careers_link, self.excel_reader.get_cell_value("parthexcel", 7, 1), self.excel_reader.get_cell_value("parthexcel", 7, 2), "Careers", opens_new_tab=True)
        self.click_and_verify_footer_link(FooterLocators.footer_gift_cards_link, self.excel_reader.get_cell_value("parthexcel", 8, 1), self.excel_reader.get_cell_value("parthexcel", 8, 2), "Gift Cards")
        self.click_and_verify_footer_link(FooterLocators.footer_klarna_link, self.excel_reader.get_cell_value("parthexcel", 9, 1), self.excel_reader.get_cell_value("parthexcel", 9, 2), "Klarna")

        # Verify "Useful links" text
        self.perform_action("VERIFY_TEXT", FooterLocators.useful_links_text, "Useful Links", expected_text="Useful links")
        
        from utilities.screenshot import Screenshot
        Screenshot.capture_browser_screenshot(self.web_driver, "case_10_footer")