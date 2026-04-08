from utilities.web_driver_helper import WebDriverHelper
from uistore.home_locators import HomeLocators
from utilities.screenshot import Screenshot
from utilities.excel_reader import ExcelReader
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

class HomePage:
    """
    # Class Name    : HomePage
    # Author        : Parth
    # Description   : Page object representing Home page operations for Test Case 10
    # Return Type   : Object
    # Parameters    : web_driver(object), logger(object)
    """
    def __init__(self, web_driver, logger):
        self.excel_reader = ExcelReader()
        self.web_driver = web_driver
        self.logger = logger
        self.web_driver_helper = WebDriverHelper(self.web_driver)

    """
    # Method Name   : close_popup
    # Author        : Parth
    # Description   : Closes the initial popup displayed on the home page
    # Return Type   : None
    # Parameters    : None
    """
    def close_popup(self):
        try:
            self.web_driver_wait = WebDriverWait(self.web_driver, 1)
            self.web_driver_helper.click_element(HomeLocators.pop_up)
            self.logger.info("Clicked on the popup close button")

        except Exception as exception:
            self.logger.error("Error while closing popup on home page")
            raise Exception(f"close_popup failed: {exception}")

    def verify_logo(self):
        """
        Method Name   : verify_logo
        Author Name   : Karuna Narayankar
        Description   : Verifies that the ELC logo is visible on the homepage and captures a screenshot
        Return Type   : None
        Parameters    : None

        """
        try:
            assert self.web_driver_helper.is_element_visible(HomeLocators.elc_logo)
            self.logger.info("ELC logo verified successfully on homepage")
            Screenshot.capture_browser_screenshot(self.web_driver, "elc_logo_verified")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "elc_logo_verification_error")
            self.logger.error(f"Failed to verify ELC logo: {e}")
            raise


    #     TestCase 1
    def hover_on_shop_by_age(self):
        """
        Method Name   : hover_on_shop_by_age
        Author Name   : Karuna Narayankar
        Description   : Hovers over 'Shop by age' menu
        Return Type   : None
        Parameters    : None
        """
        try:
            self.web_driver_helper.wait_for_element_visibility(HomeLocators.shop_by_age)
            sleep(2)
            self.web_driver_helper.hover_over_element(HomeLocators.shop_by_age)
            self.logger.info("Hovered on 'Shop by age' successfully")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "hover_shop_by_age_error")
            self.logger.error(f"Failed to hover on 'Shop by age': {e}")
            raise

    def click_newborn_gifts(self):
        """
        Method Name   : click_newborn_gifts
        Author Name   : Karuna Narayankar
        Description   : Clicks on 'Newborn Gifts' link
        Return Type   : None
        Parameters    : None
        """
        try:
            sleep(2)
            self.web_driver_helper.wait_for_element_visibility(HomeLocators.newborn_gifts)
            self.web_driver_helper.click_element(HomeLocators.newborn_gifts)
            self.logger.info("Clicked on 'Newborn Gifts' successfully")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "click_newborn_gifts_error")
            self.logger.error(f"Failed to click 'Newborn Gifts': {e}")
            raise


    # Test Case 2

    def hover_on_type_of_toy(self):
        """
        Method Name   : hover_on_type_of_toy
        Author Name   : Karuna Narayankar
        Description   : Hovers over 'Type of toy' menu
        Return Type   : None
        Parameters    : None
        """
        try:
            sleep(2)
            self.web_driver_helper.wait_for_element_visibility(HomeLocators.type_of_toy)
            self.web_driver_helper.hover_over_element(HomeLocators.type_of_toy)
            self.logger.info("Hovered on 'Type of toy' successfully")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "softtoys_hover_error")
            self.logger.error(f"Failed to hover on 'Type of toy': {e}")
            raise

    def click_soft_toys_category(self):
        """
        Method Name   : click_soft_toys_category
        Author Name   : Karuna Narayankar
        Description   : Clicks on 'Soft Toys' category link
        Return Type   : None
        Parameters    : None
        """
        try:
            sleep(2)
            self.web_driver_helper.wait_for_element_visibility(HomeLocators.soft_toys)
            self.web_driver_helper.click_element(HomeLocators.soft_toys)
            self.logger.info("Clicked on 'Soft Toys' successfully")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "softtoys_click_error")
            self.logger.error(f"Failed to click 'Soft Toys': {e}")
            raise

    # ====================================================================================================================

    # TestCase 3

    def hover_on_outdoor_toys(self):
        """
        Method name: hover_on_outdoor_toys
        Author name: Saptarshi
        Description : Hovers on Outdoor Toys menu
        Return type: None
        Parameters: None
        """
        try:
            self.web_driver_helper.hover_over_element(HomeLocators.outdoor_toys_text)
            self.logger.info(f"Outdoor toys hovered")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "hover_on_outdoor_toys_failure")
            self.logger.error(f"Failed to hover on outdoor toys: {e}")
            raise

    def click_on_bikes(self):
        """
        Method name: click_on_bikes
        Author name: Saptarshi
        Description : Clicks on Bikes option using JavaScript click
        Return type: None
        Parameters: None
        """
        try:
            sleep(2)
            self.web_driver_helper.click_element(HomeLocators.bikes_text)
            self.logger.info(f"Bikes clicked")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "click_on_bikes_failure")
            self.logger.error(f"Failed to click on bikes: {e}")
            raise

    # =====================================================================================================================
    # TestCase 4

    def hover_on_learning_skills(self):
        """
        Method name: hover_on_learning_skills
        Author name: Saptarshi
        Description: Hovers on Learning Skills menu
        Return type: None
        Parameters: None
        """
        try:

            self.web_driver_helper.hover_over_element(HomeLocators.learning_skills_text)
            self.logger.info(f"Learning skills hovered")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "hover_on_learning_skills_failure")
            self.logger.error(f"Failed to hover on learning skills: {e}")
            raise

    def click_on_creativity(self):
        """
        Method name: click_on_creativity
        Author name: Saptarshi
        Description : Clicks on Creativity option using JavaScript click
        Return type: None
        Parameters: None
        """
        try:
            sleep(1)
            self.web_driver_helper.click_element(HomeLocators.creativity_text)
            self.logger.info(f"creativity clicked")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "click_on_creativity_failure")
            self.logger.error(f"Failed to click on creativity: {e}")
            raise


    # ====================================================================================================================
    # Test Case 7  and Test Case 8

    def click_search_input_field(self):
        """
        Method Name : click_search_input_field
        Author      : Ashutosh
        Description : Clicks on the search input field on the homepage
        Parameters  : None
        Return Type : None
        """
        try:
            self.web_driver_helper.click_element(HomeLocators.search_input_field)
            self.logger.info("Search input field clicked")
        except Exception as exc:
            Screenshot.capture_browser_screenshot(
                self.web_driver, "home_click_search_input_error"
            )
            self.logger.error(f"Failed to click search input field: {exc}")
            raise
    def enter_search_text_and_submit_for_cars(self):
        """
        Method Name : enter_search_text_and_submit_for_cars
        Author      : Ashutosh
        Description : Enters 'Cars' in the search field and submits the search
        Parameters  : None
        Return Type : None
        """
        try:
            self.web_driver_helper.enter_text(HomeLocators.search_input_field, self.excel_reader.get_cell_value("ashutoshExcel",3,3))
            sleep(2)
            self.web_driver_helper.click_element(HomeLocators.search_icon)
            self.logger.info("'Cars' search submitted successfully")
        except Exception as exc:
            Screenshot.capture_browser_screenshot(
                self.web_driver, "home_search_cars_error"
            )
            self.logger.error(f"Failed to search for Cars: {exc}")
            raise
    def enter_search_text_and_submit_for_puzzles(self):
        """
        Method Name : enter_search_text_and_submit_for_puzzles
        Author      : Ashutosh
        Description : Enters 'Puzzles' in the search field and submits the search
        Parameters  : None
        Return Type : None
        """
        try:
            self.web_driver_helper.enter_text(HomeLocators.search_input_field, self.excel_reader.get_cell_value("ashutoshExcel",2,3))
            sleep(2)
            self.web_driver_helper.click_element(HomeLocators.search_icon)
            self.logger.info("'Puzzles' search submitted successfully")
        except Exception as exc:
            Screenshot.capture_browser_screenshot(
                self.web_driver, "home_search_puzzles_error"
            )
            self.logger.error(f"Failed to search for Puzzles: {exc}")
            raise

    # ============================================================================================================

    # Test Case 5 and 6
    """
    # Method Name   : hover_on_brands_navigation
    # Author        : Gitika Thakur
    # Description   : Hovers over the Brands navigation menu
    # Return Type   : None
    # Parameters    : None
    """
    def hover_on_brands_navigation(self):
        try:
            sleep(2)
            self.web_driver_helper.hover_over_element(HomeLocators.brands_navigation_link)
            self.logger.info("Hovered on Brands")
        except Exception as e:
            self.logger.exception("Hover on Brands failed")
            raise AssertionError("Unable to hover on Brands") from e

    """
    Method Name   : click_paw_patrol_brand
    Author        : Gitika Thakur
    Description   : Clicks on the Paw Patrol brand link
    Return Type   : None
    Parameters    : None
    """
    def click_paw_patrol_brand(self):
        try:
            sleep(2)
            self.web_driver_helper.click_element(HomeLocators.paw_patrol_brand_link)
            self.logger.info("Clicked Paw Patrol")
        except Exception as e:
            self.logger.exception("Click Paw Patrol failed")
            raise AssertionError("Unable to click Paw Patrol") from e

    """
    Method Name   : hover_on_explore_navigation
    Author        : Gitika Thakur
    Description   : Hovers over the Explore navigation menu
    Return Type   : None
    Parameters    : None
    """
    def hover_on_explore_navigation(self):
        try:
            sleep(2)
            self.web_driver_helper.hover_over_element(HomeLocators.explore_navigation_link)
            self.logger.info("Hovered on Explore")
        except Exception as e:
            self.logger.exception("Hover on Explore failed")
            raise AssertionError("Unable to hover on Explore") from e

    """
    Method Name   : click_gift_cards_navigation
    Author        : Gitika Thakur
    Description   : Clicks on Gift Cards link and verifies navigation
    Return Type   : None
    Parameters    : None
    """
    def click_gift_cards_navigation(self):
        try:
            self.web_driver_helper.click_element(HomeLocators.gift_cards_navigation_link)
            self.web_driver_helper.verify_current_url_contains(self.excel_reader.get_cell_value("gitikaexcel",3,2))
            self.logger.info("Gift Cards page opened")
        except Exception as e:
            self.logger.exception("Gift Cards navigation failed")
            raise AssertionError("Unable to open Gift Cards") from e

    # =============================================================================================================

    """
    Method Name   : scroll_footer
    Author        : Parth
    Description   : Scrolls the page to the footer section (case-sensitive log requirement)
    Return Type   : None
    Parameters    : None
    """
    def scroll_footer(self):
        try:
            self.web_driver_helper.scroll_to_element_using_javascript(
                HomeLocators.footer_top
            )
            self.logger.info("scroll down")

        except Exception as exception:
            self.logger.error("Error while scrolling to footer")
            raise Exception(
                f"scroll_footer failed: {exception}"
            )

    # -------------------- About Us (Test Case 10) --------------------

    """
    Method Name   : click_on_about_us
    Author        : Parth
    Description   : Clicks on the About Us link from the home page footer
    Return Type   : None
    Parameters    : None
    """
    def click_on_about_us(self):
        try:
            self.web_driver_helper.click_element(
                HomeLocators.about_us
            )
            self.logger.info("Clicked on the About Us link")

        except Exception as exception:
            self.logger.error("Error while clicking About Us link")
            raise Exception(
                f"click_on_about_us failed: {exception}"
            )

    # -------------------- Contact Us (Test Case 9) --------------------
    def open_contact_us_page(self):
        """
        Method Name   : open_contact_us_page
        Author        : Sasi kumar
        Description   : Opens the Contact Us page from ELC footer section
        Return Type   : None
        Parameters    : None
        """
        try:
            self.web_driver_helper.click_element(HomeLocators.footer_contact_us_link)
            self.logger.info("Contact Us page opened")
        except Exception as e:
            self.logger.error(f"Failed to open Contact Us page: {e}")
            raise
 