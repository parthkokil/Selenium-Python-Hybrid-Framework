from pages.base_page import BasePage
from uistore.first_product_locators import FirstProductPageLocators
from time import sleep

class FirstProductPage(BasePage):
    """
    # Class Name    : FirstProductPage
    # Author        : Karuna, Saptarshi, Ashutosh, Gitika, Parth
    # Description   : Page object for first/individual product page operations.
    #                 Inherits from BasePage and uses the unified match-case dispatcher.
    """

    def __init__(self, driver, logger):
        super().__init__(driver, logger)
        self.logger.info("FirstProductPage initialized successfully")


    # Test Case 1
    def new_born_product_page_clutter(self):
        self.perform_action("CLICK", FirstProductPageLocators.add_to_basket, "Add to Basket")
        self.perform_action("CLICK", FirstProductPageLocators.continue_shopping_button, "Continue Shopping")
        self.perform_action("VERIFY_TEXT", FirstProductPageLocators.home_delivery_radio_button, "Home Keyword", expected_text=self.excel_reader.get_cell_value("karunaexcel", 2, 1), capture_screenshot=True)
        
    # Test Case 2
    def soft_toy_product_page_clutter(self):
        self.perform_action("VERIFY_TEXT", FirstProductPageLocators.home_delivery_radio_button, "Home Delivery",expected_text=self.excel_reader.get_cell_value("karunaexcel", 4, 1))
        self.perform_action("CLICK", FirstProductPageLocators.add_to_basket, "Add to Basket")
        self.perform_action("CLICK", FirstProductPageLocators.continue_shopping_button, "Continue Shopping")
        self.perform_action("VERIFY_TEXT", FirstProductPageLocators.home_delivery_radio_button, "Home Keyword",expected_text=self.excel_reader.get_cell_value("karunaexcel", 2, 1),capture_screenshot=True)

    #  Test Case 3
    def outdoor_toys_first_product_page_clutter_flow(self):
        self.perform_action("VERIFY_ATTRIBUTE", FirstProductPageLocators.quantity_input_field, "Quantity",attribute_name="value", expected_text="1")
        self.perform_action("VERIFY_TEXT", FirstProductPageLocators.add_to_basket_button, "Add to Basket Button",expected_text=self.excel_reader.get_cell_value("saptarshiexcel", 4, 1))
        self.perform_action("CLICK", FirstProductPageLocators.add_to_basket, "Add to Basket")
        self.perform_action("VERIFY_TEXT", FirstProductPageLocators.checkout_button, "Check Out Text",expected_text=self.excel_reader.get_cell_value("saptarshiexcel", 5, 1))
        self.perform_action("SCROLL_AND_CLICK", FirstProductPageLocators.checkout_button, "Check Out Button")

    #  Test Case 4
    def creativity_first_product_page_clutter_flow(self):
        """
            Method Name   : outdoor_toys_first_product_page_clutter_flow
            Author        : Saptarshi
            Description   : Clutter function for the outdoor toys first product operations page
            Return Type   : None
            Parameters    : None
        """
        self.verify_the_add_basket_button()
        self.click_add_to_basket()
        self.click_check_out()
        self.verify_cart_page()
        #self.close_pop_up()
        self.verify_the_text_continue_shopping()


    # Test Case 5
    def verify_product_availability(self):
        """
            Method Name   : verify_product_availability
            Author        : Gitika Thakur
            Description   : Verifies whether the product is available for purchase
            Return Type   : None
            Parameters    : None
        """
        try:
            self.web_driver_helper.verify_text_contains(FirstProductPageLocators.store_availability_text,self.excel_reader.get_cell_value("gitikaexcel",2,1))
            self.logger.info("Product availability verified")
        except Exception as e:
            self.logger.exception("Availability verification failed")
            raise AssertionError("Product not available") from e
    def click_checkout(self):
        """
            Method Name   : click_checkout
            Author        : Gitika Thakur
            Description   : Clicks on Checkout button from basket page
            Return Type   : None
            Parameters    : None
        """
        try:
            self.web_driver_helper.click_element(FirstProductPageLocators.checkout_button)
            self.logger.info("Clicked Checkout")
        except Exception as e:
            self.logger.exception("Checkout click failed")
            raise AssertionError("Unable to click Checkout") from e
    def close_dynamic_popup_on_checkout(self):
        """
            # Method Name   : close_dynamic_popup_on_checkout
            # Author        : Gitika Thakur
            # Description   : Closes dynamic popup displayed on checkout page
            # Return Type   : None
            # Parameters    : None
        """
        try:
            self.web_driver_helper.click_element(FirstProductPageLocators.close_dynamic_popup_button)
            self.logger.info("Dynamic popup closed successfully")
            Screenshot.capture_browser_screenshot(self.web_driver,"basket_page")
        except Exception as e:
            self.logger.exception("Failed to close dynamic popup")
            raise AssertionError("Dynamic popup close failed") from e
    def paw_patrol_first_product_page_flow(self):
        """
            Method Name   : paw_patrol_first_product_page_flow
            Author        : Gitika Thakur
            Description   : Clutter function for the paw patrol first product page
            Return Type   : None
            Parameters    : None
        """
        self.verify_product_availability()
        self.click_add_to_basket()
        self.click_checkout()
        #self.close_dynamic_popup_on_checkout()

    #  Test Case 6
    def gift_cards_first_product_page_flow(self):
        self.perform_action("CLICK", FirstProductPageLocators.doll_add_to_basket_button, "Doll Add to Basket")
        self.perform_action("CLICK", FirstProductPageLocators.doll_checkout_button, "Doll Checkout")
        self.perform_action("CLOSE_POPUP", FirstProductPageLocators.close_dynamic_popup_button, "Dynamic Checkout Popup")
        self.perform_action("VERIFY_TEXT", FirstProductPageLocators.order_total_text, "Order Total",expected_text=self.excel_reader.get_cell_value("gitikaexcel", 6, 1),capture_screenshot=True)