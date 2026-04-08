import pytest
from base import BaseTest

from pages.first_product_page import FirstProductPage
from pages.home_page import HomePage
from pages.product_listing_page import ProductListingPage
from pages.footer_component import FooterComponentPage
from utilities.logger import get_framework_logger
from utilities.config_reader import ConfigReader

class TestCaseClass(BaseTest):
    logger = get_framework_logger()
    """
    Method Name   : setup_method
    Author        : Parth
    Description   : Sets up browser, loads application URL, applies timeout and maximizes window
    Return Type   : None
    Parameters    : None
    """
    def setUp(self):
        try:
            self.web_driver = self.setUpDriver()
            self.web_driver.maximize_window()
            self.config_reader = ConfigReader()
            application_url = self.config_reader.get_config_value("ELC","url")
            self.web_driver.get(application_url)
            timeout_seconds = int(self.config_reader.get_config_value("ELC","timeout"))
            self.web_driver.implicitly_wait(timeout_seconds)
            self.logger.info("Browser launched and application opened: %s",application_url)
        except Exception as e:
            self.logger.exception("Test setup failed.")
            pytest.fail(f"Setup failed: {e}")

    def tearDown(self):
        """
        Method Name   : teardown_method
        Author        : Parth
        Description   : Closes browser after test execution
        Return Type   : None
        Parameters    : None
        """
        try:
            if getattr(self, "web_driver", None):
                self.web_driver.quit()

            self.logger.info("Browser closed successfully.")

        except Exception as e:
            self.logger.exception("Test teardown failed.")


    @pytest.mark.smoke
    def test_newborn_gift_page(self):
        """
        Method Name :test_newborn_gift_page
        Author        : Karuna Narayankar
        Description   : Verifies newborn gifts page navigation and validates first product details.
        Return Type   : None
        Parameters    : None
        """
        try:
            home_page_obj = HomePage(self.web_driver, self.logger)
            home_page_obj.close_popup()
            home_page_obj.verify_logo()
            home_page_obj.hover_on_shop_by_age()
            home_page_obj.click_newborn_gifts()

            newborn_gift_page_object = ProductListingPage(self.web_driver, self.logger)
            newborn_gift_page_object.newborn_gift_page_clutter()

            newborn_product_object = FirstProductPage(self.web_driver, self.logger)
            newborn_product_object.new_born_product_page_clutter()

        except Exception as e:
            self.logger.error(f"Error in test_newborn_gift_page: {e}")
            pytest.fail(str(e))


    
    @pytest.mark.smoke
    def test_soft_toy_page(self):
        """
        Method Name   : test_soft_toy_page
        Author        : Karuna Narayankar
        Description   : Verifies soft toys category navigation and validates first soft toy product page.
        Return Type   : None
        Parameters    : None
        """
        try:
            home_page_obj = HomePage(self.web_driver, self.logger)
            home_page_obj.close_popup()
            home_page_obj.verify_logo()
            home_page_obj.hover_on_type_of_toy()
            home_page_obj.click_soft_toys_category()

            soft_toy_page_object = ProductListingPage(self.web_driver, self.logger)
            soft_toy_page_object.soft_toys_page_clutter()

            soft_toy_product_object = FirstProductPage(self.web_driver, self.logger)
            soft_toy_product_object.soft_toy_product_page_clutter()

        except Exception as e:
            self.logger.error(f"Error in test_soft_toy_page: {e}")
            pytest.fail(str(e))

   
    @pytest.mark.smoke
    def test_of_outdoor_toys(self):
        """
        Method name: test_of_outdoor_toys
        Author name: Saptarshi
        Description : Executes the complete flow for third test case
        Return type: None
        Parameter list: None
        """
        try:
            home_page_obj = HomePage(self.web_driver, self.logger)
            home_page_obj.close_popup()
            home_page_obj.verify_logo()
            home_page_obj.hover_on_outdoor_toys()
            home_page_obj.click_on_bikes()

            outdoor_toys_product_listing_obj = ProductListingPage(self.web_driver, self.logger)
            outdoor_toys_product_listing_obj.outdoor_toys_product_listing_page_flow()

            outdoor_toys_first_product_obj = FirstProductPage(self.web_driver, self.logger)
            outdoor_toys_first_product_obj.outdoor_toys_first_product_page_clutter_flow()

        except Exception as e:
            self.logger.error(f"Failed in test_of_third_test_case: {e}")
            pytest.fail(str(e))

    
    
    @pytest.mark.smoke
    def test_of_creativity_products(self):
        """
        Method name: test_of_creativity_products
        Author name: Saptarshi
        Description : Executes the complete flow for fourth test case.
        Return type: None
        Parameter list: None
        """
        try:
            home_page_obj = HomePage(self.web_driver, self.logger)
            home_page_obj.close_popup()
            home_page_obj.verify_logo()
            home_page_obj.hover_on_learning_skills()
            home_page_obj.click_on_creativity()

            creativity_page_obj = ProductListingPage(self.web_driver, self.logger)
            creativity_page_obj.creativity_products_listing_page_flow()

            cart_page_obj = FirstProductPage(self.web_driver, self.logger)
            cart_page_obj.creativity_first_product_page_clutter_flow()

        except Exception as e:
            self.logger.error(f"Failed in test_of_fourth_case: {e}")
            pytest.fail(str(e))

    
    @pytest.mark.smoke
    def test_paw_patrol_product_add_to_basket_flow(self):
        """
        Method Name   : test_paw_patrol_product_add_to_basket_flow
        Author        : Gitika Thakur
        Description   : Verifies Paw Patrol product add-to-basket and basket verification flow.
        Return Type   : None
        Parameters    : None
        """
        try:
            home_page_navigation_actions_obj = HomePage(self.web_driver, self.logger)
            home_page_navigation_actions_obj.close_popup()
            home_page_navigation_actions_obj.verify_logo()
            home_page_navigation_actions_obj.hover_on_brands_navigation()
            home_page_navigation_actions_obj.click_paw_patrol_brand()

            paw_patrol_product_listing_actions_obj = ProductListingPage(self.web_driver, self.logger)
            paw_patrol_product_listing_actions_obj.paw_patrol_product_listing_flow()

            add_to_basket_actions_obj = FirstProductPage(self.web_driver, self.logger)
            add_to_basket_actions_obj.paw_patrol_first_product_page_flow()

        except Exception as e:
            self.logger.error(f"Error in test_paw_patrol_product_add_to_basket_flow: {e}")
            pytest.fail(str(e))

    
    @pytest.mark.smoke
    def test_dolls_product_checkout_flow(self):
        """
        Method Name   : test_dolls_product_checkout_flow
        Author        : Gitika Thakur
        Description   : Verifies Dolls category product selection, add-to-basket, and order summary verification flow.
        Return Type   : None
        Parameters    : None
        """
        try:
            home_page_explore_navigation_actions_obj = HomePage(self.web_driver, self.logger)
            home_page_explore_navigation_actions_obj.close_popup()
            home_page_explore_navigation_actions_obj.verify_logo()
            home_page_explore_navigation_actions_obj.hover_on_explore_navigation()
            home_page_explore_navigation_actions_obj.click_gift_cards_navigation()

            dolls_product_selection_actions_obj = ProductListingPage(self.web_driver, self.logger)
            dolls_product_selection_actions_obj.click_offers_and_verify_brands_section()
            dolls_product_selection_actions_obj.click_dolls_category()
            dolls_product_selection_actions_obj.click_first_doll_product_card()

            dolls_first_product_click_actions_obj = FirstProductPage(self.web_driver, self.logger)
            dolls_first_product_click_actions_obj.gift_cards_first_product_page_flow()

        except Exception as e:
            self.logger.error(f"Error in test_dolls_product_checkout_flow: {e}")
            pytest.fail(str(e))


    
    @pytest.mark.smoke
    def test_puzzles_search_functionality_flow(self):
        """
        Method Name   : test_puzzles_search_functionality_flow
        Author        : Ashutosh
        Description   : Validates puzzles search flow and verifies wishlist + learning section on first product.
        Return Type   : None
        Parameters    : None
        """
        try:
            home_page_obj = HomePage(self.web_driver, self.logger)
            home_page_obj.close_popup()
            home_page_obj.verify_logo()
            home_page_obj.click_search_input_field()
            home_page_obj.enter_search_text_and_submit_for_puzzles()

            puzzle_product_page_obj = ProductListingPage(self.web_driver, self.logger)
            puzzle_product_page_obj.work_flow_for_puzzles_product_page()

            puzzle_first_product_page_obj = FirstProductPage(self.web_driver, self.logger)
            puzzle_first_product_page_obj.add_product_to_wishlist()
            puzzle_first_product_page_obj.verify_learning()

        except Exception as e:
            self.logger.error(f"Error in test_puzzles_search_functionality_flow: {e}")
            pytest.fail(str(e))

   
    @pytest.mark.smoke
    def test_cars_search_functionality_flow(self):
        """
        Method Name   : test_cars_search_functionality_flow
        Author        : Ashutosh
        Description   : Validates cars search functionality flow and verifies first product wishlist action.
        Return Type   : None
        Parameters    : None
        """
        try:
            home_page_obj = HomePage(self.web_driver, self.logger)
            home_page_obj.close_popup()
            home_page_obj.verify_logo()
            home_page_obj.click_search_input_field()
            home_page_obj.enter_search_text_and_submit_for_cars()

            car_product_page_obj = ProductListingPage(self.web_driver, self.logger)
            car_product_page_obj.work_flow()

            car_first_product_page_obj = FirstProductPage(self.web_driver, self.logger)
            car_first_product_page_obj.verify_heading()
            car_first_product_page_obj.click_on_add_to_wishlist()

        except Exception as e:
            self.logger.error(f"Error in test_cars_search_functionality_flow: {e}")
            pytest.fail(str(e))



    @pytest.mark.smoke
    def test_elc_footer_help_link_navigation(self):
        """
        Method Name   : test_elc_footer_help_link_navigation
        Author        : Sasi Kumar
        Description   : Verifies footer help link navigation flow.
        Return Type   : None
        Parameters    : None
        """
        try:
            home_page_obj = HomePage(self.web_driver, self.logger)
            home_page_obj.close_popup()
            home_page_obj.scroll_footer()
            home_page_obj.open_contact_us_page()

            footer_help_link_obj = FooterComponentPage(self.web_driver, self.logger)
            footer_help_link_obj.elc_footer_help_links_flow()

        except Exception as e:
            self.logger.error(f"Test Case 9 failed due to error: {e}")
            pytest.fail(str(e))

    @pytest.mark.smoke
    def test_footer_links_navigation(self):
        """
        Method Name   : test_footer_links_navigation
        Author        : Parth
        Description   : Verifies footer links navigation flow (About Us + footer links).
        Return Type   : None
        Parameters    : None
        """
        try:
            home_page_obj = HomePage(self.web_driver, self.logger)
            home_page_obj.close_popup()
            home_page_obj.scroll_footer()
            home_page_obj.click_on_about_us()

            footer_page = FooterComponentPage(self.web_driver, self.logger)
            footer_page.run_footer_links_flow()

        except Exception as e:
            self.logger.error(f"Test Case 10 failed due to error: {e}")
            pytest.fail(str(e))
