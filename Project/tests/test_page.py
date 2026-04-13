import pytest
from base import BaseTest

from pages.first_product_page import FirstProductPage
from pages.home_page import HomePage
from pages.product_listing_page import ProductListingPage
from pages.footer_component import FooterComponentPage
from utilities.logger import get_framework_logger
from utilities.config_reader import ConfigReader
from utilities.excel_reader import ExcelReader
from uistore.home_locators import HomeLocators
from uistore.first_product_locators import FirstProductPageLocators

class TestCaseClass(BaseTest):
    logger = get_framework_logger()
    
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
        try:
            if getattr(self, "web_driver", None):
                self.web_driver.quit()
            self.logger.info("Browser closed successfully.")
        except Exception as e:
            self.logger.exception("Test teardown failed.")

# # TestCase 1
#     @pytest.mark.smoke
#     def test_newborn_gift_page(self):
#         try:
#             home_page_obj = HomePage(self.web_driver, self.logger)
#             home_page_obj.perform_action("CLOSE_POPUP", locator=HomeLocators.pop_up_button, element_name="Welcome Popup")
#             home_page_obj.verify_logo()
#             home_page_obj.perform_action("HOVER", locator=HomeLocators.shop_by_age_link, element_name="Shop by age")
#             home_page_obj.perform_action("CLICK", locator=HomeLocators.newborn_gifts_link, element_name="Newborn Gifts")

#             newborn_gift_page_object = ProductListingPage(self.web_driver, self.logger)
#             newborn_gift_page_object.newborn_gift_page_clutter()

#             newborn_product_object = FirstProductPage(self.web_driver, self.logger)
#             newborn_product_object.new_born_product_page_clutter()

#         except Exception as e:
#             self.logger.error(f"Error in test_newborn_gift_page: {e}")
#             pytest.fail(str(e))

# # TestCase 2
#     @pytest.mark.smoke
#     def test_soft_toy_page(self):
#         try:
#             home_page_obj = HomePage(self.web_driver, self.logger)
#             home_page_obj.perform_action("CLOSE_POPUP", locator=HomeLocators.pop_up_button, element_name="Welcome Popup")
#             home_page_obj.verify_logo()
#             home_page_obj.perform_action("HOVER", locator=HomeLocators.type_of_toy_link, element_name="Type of toy")
#             home_page_obj.perform_action("CLICK", locator=HomeLocators.soft_toys_link, element_name="Soft Toys")

#             soft_toy_page_object = ProductListingPage(self.web_driver, self.logger)
#             soft_toy_page_object.soft_toys_page_clutter()

#             soft_toy_product_object = FirstProductPage(self.web_driver, self.logger)
#             soft_toy_product_object.soft_toy_product_page_clutter()

#         except Exception as e:
#             self.logger.error(f"Error in test_soft_toy_page: {e}")
#             pytest.fail(str(e))

# # TestCase 3
#     @pytest.mark.smoke
#     def test_of_outdoor_toys(self):
#         try:
#             home_page_obj = HomePage(self.web_driver, self.logger)
#             home_page_obj.perform_action("CLOSE_POPUP", locator=HomeLocators.pop_up_button, element_name="Welcome Popup")
#             home_page_obj.verify_logo()
#             home_page_obj.perform_action("HOVER", locator=HomeLocators.outdoor_toys_link, element_name="Outdoor Toys")
#             home_page_obj.perform_action("CLICK", locator=HomeLocators.bikes_link, element_name="Bikes")

#             outdoor_toys_product_listing_obj = ProductListingPage(self.web_driver, self.logger)
#             outdoor_toys_product_listing_obj.outdoor_toys_product_listing_page_flow()

#             outdoor_toys_first_product_obj = FirstProductPage(self.web_driver, self.logger)
#             outdoor_toys_first_product_obj.outdoor_toys_first_product_page_clutter_flow()

#         except Exception as e:
#             self.logger.error(f"Failed in test_of_third_test_case: {e}")
#             pytest.fail(str(e))

# # TestCase 4
#     @pytest.mark.smoke
#     def test_of_creativity_products(self):
#         try:
#             home_page_obj = HomePage(self.web_driver, self.logger)
#             home_page_obj.perform_action("CLOSE_POPUP", locator=HomeLocators.pop_up_button, element_name="Welcome Popup")
#             home_page_obj.verify_logo()
#             home_page_obj.perform_action("HOVER", locator=HomeLocators.learning_skills_link, element_name="Learning Skills")
#             home_page_obj.perform_action("CLICK", locator=HomeLocators.creativity_link, element_name="Creativity")

#             creativity_page_obj = ProductListingPage(self.web_driver, self.logger)
#             creativity_page_obj.creativity_products_listing_page_flow()

#             cart_page_obj = FirstProductPage(self.web_driver, self.logger)
#             cart_page_obj.creativity_first_product_page_clutter_flow()

#         except Exception as e:
#             self.logger.error(f"Failed in test_of_fourth_case: {e}")
#             pytest.fail(str(e))

# TestCase 5
    @pytest.mark.smoke
    def test_paw_patrol_product_add_to_basket_flow(self):
        try:
            home_page_navigation_actions_obj = HomePage(self.web_driver, self.logger)
            home_page_navigation_actions_obj.perform_action("CLOSE_POPUP", locator=HomeLocators.pop_up_button, element_name="Welcome Popup")
            home_page_navigation_actions_obj.verify_logo()
            home_page_navigation_actions_obj.perform_action("HOVER", locator=HomeLocators.brands_navigation_link, element_name="Brands")
            home_page_navigation_actions_obj.perform_action("CLICK", locator=HomeLocators.paw_patrol_brand_link, element_name="Paw Patrol")

            paw_patrol_product_listing_actions_obj = ProductListingPage(self.web_driver, self.logger)
            paw_patrol_product_listing_actions_obj.paw_patrol_product_listing_flow()

            add_to_basket_actions_obj = FirstProductPage(self.web_driver, self.logger)
            add_to_basket_actions_obj.paw_patrol_first_product_page_flow()

        except Exception as e:
            self.logger.error(f"Error in test_paw_patrol_product_add_to_basket_flow: {e}")
            pytest.fail(str(e))

# # TestCase 6
#     @pytest.mark.smoke
#     def test_dolls_product_checkout_flow(self):
#         try:
#             home_page_explore_navigation_actions_obj = HomePage(self.web_driver, self.logger)
#             home_page_explore_navigation_actions_obj.perform_action("CLOSE_POPUP", locator=HomeLocators.pop_up_button, element_name="Welcome Popup")
#             home_page_explore_navigation_actions_obj.verify_logo()
#             home_page_explore_navigation_actions_obj.perform_action("HOVER", locator=HomeLocators.explore_navigation_link, element_name="Explore")
#             home_page_explore_navigation_actions_obj.perform_action("CLICK", locator=HomeLocators.gift_cards_navigation_link, element_name="Gift Cards")

#             dolls_product_selection_actions_obj = ProductListingPage(self.web_driver, self.logger)
#             dolls_product_selection_actions_obj.click_offers_and_verify_brands_section()
#             dolls_product_selection_actions_obj.click_dolls_category()
#             dolls_product_selection_actions_obj.click_first_doll_product_card()

#             dolls_first_product_click_actions_obj = FirstProductPage(self.web_driver, self.logger)
#             dolls_first_product_click_actions_obj.gift_cards_first_product_page_flow()

#         except Exception as e:
#             self.logger.error(f"Error in test_dolls_product_checkout_flow: {e}")
#             pytest.fail(str(e))

# # TestCase 7
#     @pytest.mark.smoke
#     def test_puzzles_search_functionality_flow(self):
#         try:
#             home_page_obj = HomePage(self.web_driver, self.logger)
#             home_page_obj.perform_action("CLOSE_POPUP", locator=HomeLocators.pop_up_button, element_name="Welcome Popup")
#             home_page_obj.verify_logo()
            
#             excel = ExcelReader()
#             home_page_obj.perform_action(
#                 "SEARCH_AND_SUBMIT", 
#                 locator=HomeLocators.search_input_field, 
#                 element_name="Search", 
#                 expected_text=excel.get_cell_value("ashutoshExcel", 2, 3),
#                 search_icon_locator=HomeLocators.search_icon
#             )

#             puzzle_product_page_obj = ProductListingPage(self.web_driver, self.logger)
#             puzzle_product_page_obj.work_flow_for_puzzles_product_page()

#             puzzle_first_product_page_obj = FirstProductPage(self.web_driver, self.logger)
#             puzzle_first_product_page_obj.perform_action("CLICK", locator=FirstProductPageLocators.add_to_wishlist_button, element_name="Add to Wishlist")
#             puzzle_first_product_page_obj.perform_action("VERIFY_TEXT", 
#                 locator=FirstProductPageLocators.learning_description_text, 
#                 element_name="Learning Description", 
#                 expected_text=excel.get_cell_value("ashutoshExcel", 2, 1),
#                 capture_screenshot=True
#             )

#         except Exception as e:
#             self.logger.error(f"Error in test_puzzles_search_functionality_flow: {e}")
#             pytest.fail(str(e))

# # TestCase 8
#     @pytest.mark.smoke
#     def test_cars_search_functionality_flow(self):
#         try:
#             home_page_obj = HomePage(self.web_driver, self.logger)
#             home_page_obj.perform_action("CLOSE_POPUP", locator=HomeLocators.pop_up_button, element_name="Welcome Popup")
#             home_page_obj.verify_logo()
            
#             excel = ExcelReader()
#             home_page_obj.perform_action(
#                 "SEARCH_AND_SUBMIT", 
#                 locator=HomeLocators.search_input_field, 
#                 element_name="Search", 
#                 expected_text=excel.get_cell_value("ashutoshExcel", 3, 3),
#                 search_icon_locator=HomeLocators.search_icon_button
#             )

#             car_product_page_obj = ProductListingPage(self.web_driver, self.logger)
#             car_product_page_obj.work_flow()

#             car_first_product_page_obj = FirstProductPage(self.web_driver, self.logger)
#             car_first_product_page_obj.perform_action("VERIFY_TEXT", 
#                 locator=FirstProductPageLocators.product_heading_text, 
#                 element_name="Product Heading", 
#                 expected_text=excel.get_cell_value("ashutoshExcel", 3, 1),
#                 capture_screenshot=True
#             )
#             car_first_product_page_obj.perform_action("CLICK", locator=FirstProductPageLocators.add_to_wishlist_button, element_name="Add to Wishlist")

#         except Exception as e:
#             self.logger.error(f"Error in test_cars_search_functionality_flow: {e}")
#             pytest.fail(str(e))

# # TestCase 9
#     @pytest.mark.smoke
#     def test_elc_footer_help_link_navigation(self):
#         try:
#             home_page_obj = HomePage(self.web_driver, self.logger)
#             home_page_obj.perform_action("CLOSE_POPUP", locator=HomeLocators.pop_up_button, element_name="Welcome Popup")
#             home_page_obj.perform_action("SCROLL_AND_CLICK", locator=HomeLocators.footer_top, element_name="Footer", click=False)
#             home_page_obj.perform_action("SCROLL_AND_CLICK", locator=HomeLocators.footer_contact_us_link, element_name="Contact Us")

#             footer_help_link_obj = FooterComponentPage(self.web_driver, self.logger)
#             footer_help_link_obj.elc_footer_help_links_flow()

#         except Exception as e:
#             self.logger.error(f"Test Case 9 failed due to error: {e}")
#             pytest.fail(str(e))

# # TestCase 10
#     @pytest.mark.smoke
#     def test_footer_links_navigation(self):
#         try:
#             home_page_obj = HomePage(self.web_driver, self.logger)
#             home_page_obj.perform_action("CLOSE_POPUP", locator=HomeLocators.pop_up_button, element_name="Welcome Popup")
#             home_page_obj.perform_action("SCROLL_AND_CLICK", locator=HomeLocators.footer_top, element_name="Footer", click=False)
#             home_page_obj.perform_action("SCROLL_AND_CLICK", locator=HomeLocators.about_us_link, element_name="About Us")

#             footer_page = FooterComponentPage(self.web_driver, self.logger)
#             footer_page.run_footer_links_flow()

#         except Exception as e:
#             self.logger.error(f"Test Case 10 failed due to error: {e}")
#             pytest.fail(str(e))
