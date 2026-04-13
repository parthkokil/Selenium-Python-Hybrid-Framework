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
        self.perform_action("VERIFY_TEXT", FirstProductPageLocators.add_to_basket_button, "Add to Basket Button",expected_text=self.excel_reader.get_cell_value("saptarshiexcel", 4, 1))
        self.perform_action("CLICK", FirstProductPageLocators.add_to_basket, "Add to Basket")
        self.perform_action("SCROLL_AND_CLICK", FirstProductPageLocators.checkout_button, "Check Out Button")
        self.perform_action("VERIFY_URL", expected_text=self.excel_reader.get_cell_value("saptarshiexcel", 3, 2), element_name="Cart")
        sleep(3)
        self.perform_action("CLOSE_POPUP", FirstProductPageLocators.close_dynamic_popup_button, "Cart Popup")
        
    #  Test Case 5
    def paw_patrol_first_product_page_flow(self):
        self.perform_action("VERIFY_TEXT", FirstProductPageLocators.store_availability_text, "Store Availability",expected_text=self.excel_reader.get_cell_value("gitikaexcel", 2, 1))
        self.perform_action("CLICK", FirstProductPageLocators.add_to_basket, "Add to Basket")
        self.perform_action("CLICK", FirstProductPageLocators.checkout_button, "Checkout")
        self.perform_action("CLOSE_POPUP", FirstProductPageLocators.close_dynamic_popup_button, "Dynamic Checkout Popup")

    #  Test Case 6
    def gift_cards_first_product_page_flow(self):
        self.perform_action("CLICK", FirstProductPageLocators.doll_add_to_basket_button, "Doll Add to Basket")
        self.perform_action("CLICK", FirstProductPageLocators.doll_checkout_button, "Doll Checkout")
        self.perform_action("CLOSE_POPUP", FirstProductPageLocators.close_dynamic_popup_button, "Dynamic Checkout Popup")
        self.perform_action("VERIFY_TEXT", FirstProductPageLocators.order_total_text, "Order Total",expected_text=self.excel_reader.get_cell_value("gitikaexcel", 6, 1),capture_screenshot=True)