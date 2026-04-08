from utilities.web_driver_helper import WebDriverHelper
from utilities.screenshot import Screenshot
from uistore.first_product_locators import FirstProductPageLocators
from utilities.excel_reader import ExcelReader
from time import sleep

class FirstProductPage:

    def __init__(self, driver, logger):
        """
        Method Name   : __init__
        Author Name   : Karuna Narayankar
        Description   : Initializes NewbornProductPage with driver and logger
        Parameters    : driver (WebDriver), logger (Logger)
        Return Type   : None
        """
        try:
            self.web_driver= driver
            self.logger = logger
            self.excel_reader = ExcelReader()
            self.web_driver_helper = WebDriverHelper(self.web_driver)
            self.logger.info("NewbornGiftsPage initialized successfully")
        except Exception as e:
            self.logger.error(f"NewbornGiftsPage initialization failed: {e}")
            raise

    # Test Case 1
    def click_add_to_basket(self):
        """
        Method Name   : click_add_to_basket
        Author Name   : Karuna Narayankar
        Description   : Clicks on 'Add to Basket' button for a product
        Parameters    : None
        Return Type   : None
        """
        try:
            # sleep(3)
            self.web_driver_helper.wait_for_element_visibility(FirstProductPageLocators.add_to_basket)
            self.web_driver_helper.click_element(FirstProductPageLocators.add_to_basket)
            self.logger.info("Clicked on 'Add to Basket'")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "add_to_basket_error")
            self.logger.error(f"Failed to click 'Add to Basket': {e}")
            raise
    def click_continue_shopping(self):
        """
        Method Name   : click_continue_shopping
        Author Name   : Karuna Narayankar
        Description   : Clicks on 'Continue Shopping' button after adding a product to basket
        Parameters    : None
        Return Type   : None
        """
        try:
            # sleep(2)
            self.web_driver_helper.wait_for_element_visibility(FirstProductPageLocators.continue_shopping)
            self.web_driver_helper.click_element(FirstProductPageLocators.continue_shopping)
            self.logger.info("Clicked on 'Continue Shopping'")
            # sleep(2)
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "continue_shopping_error")
            self.logger.error(f"Failed to click 'Continue Shopping': {e}")
            raise
    def verify_keyword_home(self):
        """
        Method Name   : verify_keyword_home
        Author Name   : Karuna Narayankar
        Description   : Verifies that the 'Home' keyword is displayed on the product page
        Parameters    : None
        Return Type   : None
        """
        try:
            self.web_driver_helper.wait_for_element_visibility(FirstProductPageLocators.home)
            self.web_driver_helper.verify_text_contains(FirstProductPageLocators.home, self.excel_reader.get_cell_value("karunaexcel",2,1))
            self.logger.info("Verified 'Home' keyword successfully")
            Screenshot.capture_browser_screenshot(self.web_driver, "gift_added_to_cart")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "verify_home_error")
            self.logger.error(f"Failed to verify 'Home' keyword: {e}")
            raise
    def new_born_product_page_clutter(self):
        """
        Method Name   : new_born_product_page_clutter
        Author Name   : Karuna Narayankar
        Description   : Executes full test flow for Newborn Product page including add to basket, continue shopping, and keyword verification
        Parameters    : None
        Return Type   : None
        """
        try:
            self.click_add_to_basket()
            self.click_continue_shopping()
            self.verify_keyword_home()
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "clutter_flow_error")
            self.logger.error(f"Clutter flow execution failed: {e}")
            raise

    # Test Case 2
    def verify_home_delivery(self):
        """
        Method Name   : verify_home_delivery
        Author Name   : Karuna Narayankar
        Description   : Verifies that the 'Home Delivery' text is displayed on the product page
        Parameters    : None
        Return Type   : None
        """
        try:
            # sleep(3)
            self.web_driver_helper.verify_text_contains(FirstProductPageLocators.home_delivery, self.excel_reader.get_cell_value("karunaexcel",4,1))
            self.logger.info("Verified 'Home Delivery'")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "home_delivery_error")
            self.logger.error(f"Failed to verify 'Home Delivery': {e}")
            raise
    def soft_toy_product_page_clutter(self):
        """
        Method Name   : soft_toy_product_page_clutter
        Author Name   : Karuna Narayankar
        Description   : Executes full test flow for Soft Toy product page including verification, add to cart, continue shopping, and keyword check
        Parameters    : None
        Return Type   : None
        """
        try:
            self.verify_home_delivery()
            self.click_add_to_basket()
            self.click_continue_shopping()
            self.verify_keyword_home()
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "soft_toy_product_clutter_error")
            self.logger.error(f"Soft Toy product page clutter flow failed: {e}")
            raise

    # TestCase 3

    def verify_the_add_basket_button(self):
        """
        Method name: verify_the_add_basket_button
        Author name: Saptarshi
        Description : Verifies 'Add to Basket' button exists on product page
        Return type: None
        Parameters: None
        """
        try:
            self.web_driver_helper.verify_text_contains(FirstProductPageLocators.add_to_basket_button,self.excel_reader.get_cell_value("saptarshiexcel",4,1))
            self.logger.info("Add To Basket exist means it is in product page")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "verify_the_add_basket_button_failure")
            self.logger.error(f"Failed to verify Add to Basket button: {e}")
            raise


    def verify_the_quantity_as_one(self):
        """
        Method name: verify_the_quantity_as_one
        Author name: Saptarshi
        Description: Verifies that the quantity value is '1'
        Return type: None
        Parameters: None
        """
        try:
            self.web_driver_helper.verify_attribute_contains(FirstProductPageLocators.quantity_value, "value", "1")
            self.logger.info("Quantity value is 1 checked")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "verify_the_quantity_as_one_failure")
            self.logger.error(f"Failed to verify quantity as one: {e}")
            raise

    def verify_check_out(self):
        """
        Method name: verify_check_out
        Author name: Saptarshi
        Description: Verifies 'Check out' text is present
        Return type: None
        Parameters: None
        """
        try:
            self.web_driver_helper.verify_text_contains(FirstProductPageLocators.check_out_text,self.excel_reader.get_cell_value("saptarshiexcel",5,1))
            self.logger.info("Check Out exist")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "verify_check_out_failure")
            self.logger.error(f"Failed to verify Check out text: {e}")
            raise

    def click_check_out(self):
        """
        Method name: click_check_out
        Author name: Saptarshi
        Description : Clicks on Check out using JavaScript click
        Return type: None
        Parameters: None
        """
        try:
            self.web_driver_helper.scroll_to_element_using_javascript(FirstProductPageLocators.check_out_text)
            self.web_driver_helper.click_element(FirstProductPageLocators.check_out_text)
            self.logger.info("Check Out clicked")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "click_check_out_failure")
            self.logger.error(f"Failed to click Check out: {e}")
            raise

    def outdoor_toys_first_product_page_clutter_flow(self):
        """
            Method Name   : outdoor_toys_first_product_page_clutter_flow
            Author        : Saptarshi Thakur
            Description   : Clutter function for the outdoor toys first product operations page
            Return Type   : None
            Parameters    : None
        """
        self.verify_the_quantity_as_one()
        self.verify_the_add_basket_button()
        self.click_add_to_basket()
        self.verify_check_out()
        self.click_check_out()

    # Test Case 4

    def verify_cart_page(self):
        """
        Method Name   : verify_cart_page
        Author        : Saptarshi
        Description   : Verifies that current URL contains 'cart'
        Return Type   : None
        Parameters    : None
        """
        try:
            self.web_driver_helper.verify_current_url_contains(self.excel_reader.get_cell_value("saptarshiexcel",3,2))
            self.logger.info("Verified url of cart page")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "verify_cart_page_failure")
            self.logger.error(f"Failed to verify cart page URL: {e}")
            raise

    def close_pop_up(self):
        """
        Method Name   : close_the_pop_up
        Author        : Saptarshi
        Description   : Closes the cart popup
        Return Type   : None
        Parameters    : None
        """
        try:
            self.web_driver_helper.click_element(FirstProductPageLocators.pop_up)
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "close_the_pop_up_failure")
            self.logger.error(f"Failed to close the pop-up: {e}")
            raise

    def verify_the_text_continue_shopping(self):
        """
        Method Name   : verify_the_text_continue_shopping
        Author        : Saptarshi
        Description   : Verifies Continue Shopping text is present
        Return Type   : None
        Parameters    : None
        """
        try:
            self.web_driver_helper.verify_attribute_contains(FirstProductPageLocators.continue_shopping_button,"innerText",self.excel_reader.get_cell_value("saptarshiexcel",6,1))
            self.logger.info("Continue shopping text present")
            Screenshot.capture_browser_screenshot(self.web_driver, "cart")
        except Exception as e:
            Screenshot.capture_browser_screenshot(
                self.web_driver, "verify_the_text_continue_shopping_failure"
            )
            self.logger.error(f"Failed to verify Continue Shopping text: {e}")
            raise

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
        self.close_pop_up()
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
        self.close_dynamic_popup_on_checkout()

    # Test Case 6
    def click_doll_add_to_basket(self):
        """
        Method Name   : click_doll_add_to_basket
        Author        : Gitika Thakur
        Description   : Clicks Add to Basket button for doll product
        Return Type   : None
        Parameters    : None
        """
        try:
            self.web_driver_helper.click_element(FirstProductPageLocators.doll_add_to_basket_button)
            self.logger.info("Doll product added to basket")
        except Exception as e:
            self.logger.exception("Add to basket failed")
            raise AssertionError("Unable to add doll product to basket") from e
    def click_doll_checkout(self):
        """
        Method Name   : click_doll_checkout
        Author        : Gitika Thakur
        Description   : Clicks Checkout button for doll product flow
        Return Type   : None
        Parameters    : None
        """
        try:
            self.web_driver_helper.click_element(FirstProductPageLocators.doll_checkout_button)
            self.logger.info("Clicked Checkout for doll product")
        except Exception as e:
            self.logger.exception("Checkout failed")
            raise AssertionError("Checkout validation failed") from e
    def verify_order_total_and_capture_screenshot(self):
        """
        Method Name   : verify_order_total_and_capture_screenshot
        Author        : Gitika Thakur
        Description   : Verifies order total section and captures screenshot
        Return Type   : None
        Parameters    : None
        """
        try:
            self.web_driver_helper.verify_text_contains(FirstProductPageLocators.order_total_text,self.excel_reader.get_cell_value("gitikaexcel",6,1))
            Screenshot.capture_browser_screenshot(self.web_driver,"order_total")
            self.logger.info("Order total verified successfully")
        except Exception as e:
            self.logger.exception("Order total verification failed")
            raise AssertionError("Order total validation failed") from e
    def gift_cards_first_product_page_flow(self):
        """
            Method Name   : gift_cards_first_product_page_flow
            Author        : Gitika Thakur
            Description   : Clutter function for the gift cards first product page
            Return Type   : None
            Parameters    : None
        """
        self.click_doll_add_to_basket()
        self.click_doll_checkout()
        self.close_dynamic_popup_on_checkout()
        self.verify_order_total_and_capture_screenshot()

    # Test Case 7
    def add_product_to_wishlist(self):
        """
        Method Name : add_product_to_wishlist
        Author      : Ashutosh
        Description : Adds the product to wishlist
        Parameters  : None
        Return Type : None
        """
        try:
            self.web_driver_helper.click_element(FirstProductPageLocators.add_to_wishlist_button)
            self.logger.info("'Add to Wishlist' button clicked")

        except Exception as exc:
            Screenshot.capture_browser_screenshot(self.web_driver, "puzzles_add_to_wishlist_error")
            self.logger.error(f"Failed to add product: {exc}")
            raise
    def verify_learning(self):
        """
        Method Name : verify_learning
        Author      : Ashutosh
        Description :verifies the 'Learning' text on the product page, and captures a screenshot
        Parameters  : None
        Return Type : None
        """
        try:
            self.web_driver_helper.verify_text_contains(FirstProductPageLocators.learning_description_text,self.excel_reader.get_cell_value("ashutoshExcel",2,1))
            self.logger.info("'Learning' keyword verified on product description")

            Screenshot.capture_browser_screenshot(self.web_driver, "puzzles_learning_text_verified")
            self.logger.info("Screenshot captured for learning verification")
        except Exception as exc:
            Screenshot.capture_browser_screenshot(self.web_driver, "verification error")
            self.logger.error(f"Failed  verify learning text: {exc}")
            raise

    # Test Case 8
    def verify_heading(self):
        """
        Method Name: verify_heading
        Author: Ashutosh
        Description: Verifies expected keyword on product heading, captures screenshot
        Parameters    : expected(str), page_name(str)
        Return Type: None
        """
        try:
            sleep(2)
            self.web_driver_helper.verify_text_contains(FirstProductPageLocators.product_heading_text,self.excel_reader.get_cell_value("ashutoshExcel",3,1))
            self.logger.info(f"'Early' keyword is present in product heading")

            Screenshot.capture_browser_screenshot(self.web_driver,"Early learning text verified")
            self.logger.info(f"Screenshot captured with Early")

        except Exception as exc:
            Screenshot.capture_browser_screenshot( self.web_driver, "verify_heading_error")
            self.logger.error(f"Failed to verify heading : {exc}")
            raise
    def click_on_add_to_wishlist(self):
        """
        Method Name: click_on_add_to_wishlist
        Author: Ashutosh
        Description: clicks on 'Add to Wishlist'
        Parameters : expected(str), page_name(str)
        Return Type: None
        """
        try:
            self.web_driver_helper.click_element(FirstProductPageLocators.add_to_wishlist_button)
            self.logger.info("'Add to Wishlist' button clicked")

        except Exception as exc:
            Screenshot.capture_browser_screenshot( self.web_driver, "Cars_add_to_wishlist_error")
            self.logger.error(f"Failed add to wishlist: {exc}")
            raise

 