from pages.base_page import BasePage
from uistore.product_listing_locators import ProductListingLocators
from time import sleep

class ProductListingPage(BasePage):
    """
    # Class Name    : ProductListingPage
    # Author        : Karuna, Saptarshi, Ashutosh, Gitika, Parth
    # Description   : Page object for product listing page operations.
    #                 Inherits from BasePage and uses the unified perform_action dispatcher
    #                 for all its workflows.
    """

    def __init__(self, driver, logger):
        super().__init__(driver, logger)
        self.logger.info("ProductListingPage initialized successfully")

    def verify_page_loaded(self, url_keyword, page_name):
        """ Custom multi-step verifier for page loads """
        self.perform_action("VERIFY_URL", expected_text=url_keyword, element_name=page_name)
        if self.web_driver_helper.is_footer_visible_by_tag_name(self.web_driver, "footer"):
            self.logger.info(f"Footer is visible on {page_name} page")
        else:
            raise AssertionError(f"Footer is not visible on {page_name} page")

    # Test Case 1
    def newborn_gift_page_clutter(self):
        self.perform_action("VERIFY_URL", expected_text=self.excel_reader.get_cell_value("karunaexcel", 2, 2), element_name="Newborn Gifts")
        self.perform_action("CLICK", ProductListingLocators.show_more_under_toy_type, "Show More")
        self.perform_action("CLICK", ProductListingLocators.baby_activity_toys, "Baby Activity Toys")
        self.perform_action("SCROLL_AND_CLICK", ProductListingLocators.early_learning_center, "Early Learning Centre")
        self.perform_action("CLICK", ProductListingLocators.hand_eye_coordination, "Hand Eye Coordination")
        self.perform_action("VERIFY_VISIBLE", ProductListingLocators.relevant_content, "Relevant Content Newborn")
        self.perform_action("CLICK", ProductListingLocators.first_product_link, "First Product Newborn Gifts")

    #  Test Case 2
    def soft_toys_page_clutter(self):
        self.perform_action("VERIFY_URL", expected_text=self.excel_reader.get_cell_value("karunaexcel", 3, 2), element_name="Soft Toys")
        self.perform_action("CLICK", ProductListingLocators.dolls_category_link, "Dolls")
        self.perform_action("CLICK", ProductListingLocators.soft_toy, "Soft Toys")
        self.perform_action("VERIFY_TEXT", ProductListingLocators.brands_verify, "Brands Text", expected_text=self.excel_reader.get_cell_value("karunaexcel", 3, 1))
        self.perform_action("CLICK", ProductListingLocators.stimulating_senses, "Stimulating senses")
        self.perform_action("VERIFY_VISIBLE", ProductListingLocators.relevant_text, "Relevant Content Soft Toys")
        self.perform_action("CLICK", ProductListingLocators.first_product_link, "First Product Soft Toys")

    # Test Case 3
    def outdoor_toys_product_listing_page_flow(self):
        self.perform_action("VERIFY_URL", expected_text=self.excel_reader.get_cell_value("saptarshiexcel", 2, 2), element_name="Bikes")
        self.perform_action("SCROLL_AND_CLICK", ProductListingLocators.show_more_text, "Show More")
        self.perform_action("SCROLL_AND_CLICK", ProductListingLocators.huffy_option, "Huffy")
        self.perform_action("SCROLL_AND_CLICK", ProductListingLocators.toddler_bikes_text, "Toddler Bikes")
        self.perform_action("VERIFY_TEXT", ProductListingLocators.search_keyword, "Search Keyword", expected_text=self.excel_reader.get_cell_value("saptarshiexcel", 2, 1))
        self.perform_action("SCROLL_AND_CLICK", ProductListingLocators.disney_checkbox, "Disney")
        self.perform_action("CLICK", ProductListingLocators.first_product_link, "First Product Bikes")

    # Test Case 4
    def creativity_products_listing_page_flow(self):
        self.perform_action("VERIFY_URL", expected_text=self.excel_reader.get_cell_value("saptarshiexcel", 4, 2), element_name="Creativity")
        self.perform_action("SCROLL_AND_CLICK", ProductListingLocators.arts_and_craft_text, "Arts & Crafts")
        sleep(3)
        self.perform_action("SCROLL_AND_CLICK", ProductListingLocators.creativity_checkbox, "Creativity")
        sleep(2)
        self.perform_action("SCROLL_AND_CLICK", ProductListingLocators.first_product_img, "First Product Creativity")

    # Test Case 5
    def paw_patrol_product_listing_flow(self):
        self.verify_page_loaded(self.excel_reader.get_cell_value("gitikaexcel", 2, 2), "Paw Patrol")
        self.perform_action("CLICK", ProductListingLocators.playsets_filter_option, "Playsets")
        self.perform_action("CLICK", ProductListingLocators.savings_filter_option, "Savings")
        self.perform_action("CLICK", ProductListingLocators.first_product_thumbnail_link, "First Product Paw Patrol")

    # Test Case 6
    def click_offers_and_verify_brands_section(self):
        self.perform_action("CLICK", ProductListingLocators.offers_navigation_link, "Offers")
        self.perform_action("VERIFY_TEXT", ProductListingLocators.brands_navigation_link, "Brands Link", expected_text=self.excel_reader.get_cell_value("gitikaexcel", 4, 1))

    def click_dolls_category(self):
        self.perform_action("CLICK", ProductListingLocators.dolls_category_link, "Dolls Category")

    def click_first_doll_product_card(self):
        self.perform_action("CLICK", ProductListingLocators.first_product_card, "First Doll Product Card")
        self.perform_action("VERIFY_TEXT", ProductListingLocators.explore_navigation_link, "Explore Navigation Link", expected_text=self.excel_reader.get_cell_value("gitikaexcel", 5, 1))

    # Test Case 7
    def work_flow_for_puzzles_product_page(self):
        self.perform_action("VERIFY_URL", expected_text=self.excel_reader.get_cell_value("ashutoshExcel", 2, 2), element_name="Puzzles")
        self.perform_action("CLICK", ProductListingLocators.show_more_under_toy_type, "Show More Toy Type")
        self.perform_action("CLICK", ProductListingLocators.jigsaw_puzzles_filter_under_toy_type, "Jigsaw Puzzles")
        self.verify_page_loaded("Jigsaw%20Puzzles", "Jigsaw Puzzles")
        self.perform_action("CLICK", ProductListingLocators.children_games_filter_under_toy_type, "Children Games")
        self.perform_action("CLICK", ProductListingLocators.discover_world_filter_under_learning_skills, "Discover World")
        self.perform_action("CLICK", ProductListingLocators.first_product_link, "First Product Puzzles")

    # Test Case 8
    def work_flow(self):
        self.perform_action("VERIFY_URL", expected_text=self.excel_reader.get_cell_value("ashutoshExcel", 3, 2), element_name="Cars")
        self.perform_action("CLICK", ProductListingLocators.show_more_under_toy_type, "Show More Toy Type")
        self.perform_action("CLICK", ProductListingLocators.toy_cars_filter_under_toy_type, "Toy Cars")
        self.perform_action("HOVER", ProductListingLocators.learning_skills_menu, "Learning Skills")
        self.perform_action("CLICK", ProductListingLocators.imaginative_play_filter_under_learning_skills, "Imaginative Play")
        self.perform_action("CLICK", ProductListingLocators.fine_motor_skills_filter_under_learning_skills, "Fine Motor Skills")
        self.verify_page_loaded("skills", "Skills")
        self.perform_action("CLICK", ProductListingLocators.first_product_link, "First Product Cars")