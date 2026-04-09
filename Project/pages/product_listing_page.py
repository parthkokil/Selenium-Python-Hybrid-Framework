from utilities.web_driver_helper import WebDriverHelper
from utilities.screenshot import Screenshot
from time import sleep
from utilities.excel_reader import ExcelReader
from uistore.product_listing_locators import ProductListingLocators

class ProductListingPage:

    def __init__(self, driver, logger):
        """
        Method Name   : __init__
        Author Name   : Karuna Narayankar
        Description   : Initializes NewbornPage with driver and logger
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

    def verify_url_of_new_born_baby_gifts_page(self):
        """
        Method Name   : verify_url
        Author Name   : Karuna Narayankar
        Description   : Verifies that the current URL contains 'new-born-baby-gift-ideas'
        Parameters    : None
        Return Type   : None
        """
        try:
            self.web_driver_helper.verify_current_url_contains(self.excel_reader.get_cell_value("karunaexcel",2,2))
            self.logger.info("Verified URL contains 'new-born-baby-gift-ideas'")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "verify_url_error")
            self.logger.error(f"URL verification failed: {e}")
            raise
    def click_on_show_more(self):
        """
        Method Name   : click_on_show_more
        Author Name   : Karuna Narayankar
        Description   : Clicks on 'Show more' filter option
        Parameters    : None
        Return Type   : None
        """
        try:
            self.web_driver_helper.click_element(ProductListingLocators.show_more)
            self.logger.info("Clicked on 'Show more'")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "show_more_error")
            self.logger.error(f"Failed to click 'Show more': {e}")
            raise
    def click_on_baby_activity_toys(self):
        """
        Method Name   : click_on_baby_activity_toys
        Author Name   : Karuna Narayankar
        Description   : Clicks on 'Baby Activity Toys' filter option
        Parameters    : None
        Return Type   : None
        """
        try:
            sleep(2)
            self.web_driver_helper.wait_for_element_visibility(ProductListingLocators.baby_activity_toys)
            self.web_driver_helper.click_element(ProductListingLocators.baby_activity_toys)
            self.logger.info("Clicked on 'Baby Activity Toys'")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "baby_activity_toys_error")
            self.logger.error(f"Failed to click 'Baby Activity Toys': {e}")
            raise
    def click_on_early_learning_centre(self):
        """
        Method Name   : click_on_early_learning_centre
        Author Name   : Karuna Narayankar
        Description   : Clicks on 'Early Learning Centre' filter option
        Parameters    : None
        Return Type   : None
        """
        try:
            sleep(2)
            self.web_driver_helper.wait_for_element_visibility(ProductListingLocators.early_learning_center)
            self.web_driver_helper.click_element(ProductListingLocators.early_learning_center)
            self.logger.info("Clicked on 'Early Learning Centre'")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "early_learning_centre_error")
            self.logger.error(f"Failed to click 'Early Learning Centre': {e}")
            raise
    def click_on_hand_eye_coordination(self):
        """
        Method Name   : click_on_hand_eye_coordination
        Author Name   : Karuna Narayankar
        Description   : Clicks on 'Hand Eye Coordination' filter option and captures screenshot
        Parameters    : None
        Return Type   : None
        """
        try:
            sleep(2)
            self.web_driver_helper.wait_for_element_visibility(ProductListingLocators.hand_eye_coordination)
            self.web_driver_helper.click_element(ProductListingLocators.hand_eye_coordination)
            self.logger.info("Clicked on 'Hand Eye Coordination'")
            Screenshot.capture_browser_screenshot(self.web_driver, "hand_eye_coordination_success")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "hand_eye_coordination_error")
            self.logger.error(f"Failed to click 'Hand Eye Coordination': {e}")
            raise
    def verify_relevant_content_on_new_born_baby_gifts_page(self):
        """
        Method Name   : verify_relevant_content
        Author Name   : Karuna Narayankar
        Description   : Verifies that relevant content heading is visible
        Parameters    : None
        Return Type   : None
        """
        try:
            assert self.web_driver_helper.is_element_visible(ProductListingLocators.relevant_content)
            self.logger.info("Relevant content verified successfully")
            Screenshot.capture_browser_screenshot(self.web_driver, "relevant_content_verified")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "relevant_content_error")
            self.logger.error(f"Failed to verify relevant content: {e}")
            raise
    def click_first_product_of_new_born_baby_gift(self):
        """
        Method Name   : click_first_product
        Author Name   : Karuna Narayankar
        Description   : Clicks on the first product in 'Shop by Age'
        Parameters    : None
        Return Type   : None
        """
        try:
            sleep(2)
            self.web_driver_helper.wait_for_element_visibility(ProductListingLocators.first_product_link)
            self.web_driver_helper.click_element(ProductListingLocators.first_product_link)
            self.logger.info("Clicked on first product")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "first_product_error")
            self.logger.error(f"Failed to click first product: {e}")
            raise
    def newborn_gift_page_clutter(self):
        """
        Method Name   : newborn_gift_page_clutter
        Author Name   : Karuna Narayankar
        Description   : Executes full test flow for Newborn Gifts page including filters and product click
        Parameters    : None
        Return Type   : None
        """
        try:
            self.verify_url_of_new_born_baby_gifts_page()
            self.click_on_show_more()
            self.click_on_baby_activity_toys()
            self.click_on_early_learning_centre()
            self.click_on_hand_eye_coordination()
            self.verify_relevant_content_on_new_born_baby_gifts_page()
            self.click_first_product_of_new_born_baby_gift()
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "clutter_flow_error")
            self.logger.error(f"Clutter flow execution failed: {e}")
            raise

# ==========================================================================================================

    # Test Case 2

    def verify_url_of_soft_toys_page(self):
        """
        Method Name   : click_on_dolls
        Author Name   : Karuna Narayankar
        Description   : Clicks on 'Dolls' filter option
        Parameters    : None
        Return Type   : None
        """
        try:
            sleep(2)
            self.web_driver_helper.verify_current_url_contains(self.excel_reader.get_cell_value("karunaexcel",3,2))
            self.logger.info("Verified URL contains 'soft-toys'")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "softtoys_url_error")
            self.logger.error(f"URL verification failed: {e}")
            raise
    def click_on_dolls(self):
        """
        Method Name: clicks
        Description: Performs clicks on 'Dolls' and 'Soft Toys'
        Return Type: None
        """
        try:
            sleep(2)
            self.web_driver_helper.wait_for_element_visibility(ProductListingLocators.dolls)
            self.web_driver_helper.click_element(ProductListingLocators.dolls)
            self.logger.info("Clicked on 'Dolls'")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "dolls_click_error")
            self.logger.error(f"Failed to click 'Dolls': {e}")
            raise
    def click_on_soft_toy(self):
        """
        Method Name   : click_on_soft_toy
        Author Name   : Karuna Narayankar
        Description   : Clicks on 'Soft Toys' filter option
        Parameters    : None
        Return Type   : None
        """
        try:
            self.web_driver_helper.click_element(ProductListingLocators.soft_toy)
            self.logger.info("Clicked on 'Soft Toys'")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "soft_toy_click_error")
            self.logger.error(f"Failed to click 'Soft Toys': {e}")
            raise
    def verify_keyword_brand(self):
        """
        Method Name   : verify_keyword_brand
        Author Name   : Karuna Narayankar
        Description   : Verifies 'Brands' keyword and clicks 'Stimulating senses'
        Parameters    : None
        Return Type   : None
        """
        try:
            sleep(2)
            self.web_driver_helper.wait_for_element_visibility(ProductListingLocators.brands_verify)
            self.web_driver_helper.verify_text_contains(ProductListingLocators.brands_verify, self.excel_reader.get_cell_value("karunaexcel",3,1))
            self.logger.info("Verified 'Brands' keyword successfully")
            self.web_driver_helper.click_element(ProductListingLocators.stimulating_senses)
            self.logger.info("Clicked on 'Stimulating senses'")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "softtoys_brands_error")
            self.logger.error(f"Failed to verify 'Brands' keyword: {e}")
            raise
    def verify_relevant_content_of_soft_toy_page(self):
        """
        Method Name   : verify_relevant_content
        Author Name   : Karuna Narayankar
        Description   : Verifies that relevant content heading is visible
        Parameters    : None
        Return Type   : None
        """
        try:
            assert self.web_driver_helper.is_element_visible(ProductListingLocators.relevant_text)
            self.logger.info("Relevant content verified successfully")
            Screenshot.capture_browser_screenshot(self.web_driver, "softtoys_relevant_content")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "softtoys_relevant_content_error")
            self.logger.error(f"Failed to verify relevant content: {e}")
            raise
    def click_first_product_of_soft_toy_page(self):
        """
        Method Name   : click_first_product
        Author Name   : Karuna Narayankar
        Description   : Clicks on the first product in 'Type of Toy'
        Parameters    : None
        Return Type   : None
        """
        try:
            self.web_driver_helper.wait_for_element_visibility(ProductListingLocators.first_product_link)
            self.web_driver_helper.click_element(ProductListingLocators.first_product_link)
            sleep(2)
            self.logger.info("Clicked on first product")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "first_product_error")
            self.logger.error(f"Failed to click first product: {e}")
            raise
    def soft_toys_page_clutter(self):
        """
        Method Name   : soft_toys_page_clutter
        Author Name   : Karuna Narayankar
        Description   : Executes full test flow for Soft Toys page including filters, keyword verification, and product click
        Parameters    : None
        Return Type   : None
        """
        try:
            self.verify_url_of_soft_toys_page()
            self.click_on_dolls()
            self.click_on_soft_toy()
            self.verify_keyword_brand()
            self.verify_relevant_content_of_soft_toy_page()
            self.click_first_product_of_soft_toy_page()
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "soft_toys_clutter_error")
            self.logger.error(f"Soft Toys page clutter flow failed: {e}")
            raise

# ==========================================================================================================

    # TestCase 3

    # functions to verify the page is loaded
    def verify_the_url_contain_bikes(self):
        """
        Method name: verify_the_url_contain_bikes
        Author name: Saptarshi
        Description : Verifies that the current URL contains 'bikes'
        Return type: None
        Parameters: None
        """
        try:
            self.web_driver_helper.verify_current_url_contains(self.excel_reader.get_cell_value("saptarshiexcel",2,2))
            self.logger.info("Bikes page url is verified")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "verify_the_url_contain_bikes_failure")
            self.logger.error(f"Failed to verify Bikes page URL contains bikes: {e}")
            raise

    def click_on_show_more_text(self):
        """
        Method name: click_on_show_more
        Author name: Saptarshi
        Description : Clicks on the 'Show more' option on bikes page
        Return type: None
        Parameters: None
        """
        try:
            self.web_driver_helper.scroll_to_element_using_javascript(ProductListingLocators.show_more_text)
            self.web_driver_helper.click_element(ProductListingLocators.show_more_text)
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "click_on_show_more_failure")
            self.logger.error(f"Failed to click on show more option: {e}")
            raise

    def click_on_huffy(self):
        """
        Method name: click_on_huffy
        Author name: Saptarshi
        Description: Clicks on the 'Huffy' option on bikes page
        Return type: None
        Parameters: None
        """
        try:
            self.web_driver_helper.scroll_to_element_using_javascript(ProductListingLocators.huffy_option)
            self.web_driver_helper.click_element(ProductListingLocators.huffy_option)
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "click_on_huffy_failure")
            self.logger.error(f"Failed to click on Huffy option: {e}")
            raise

    def click_toddler_bikes(self):
        """
        Method name: click_toddler_bikes
        Author name: Saptarshi
        Description : Clicks on Toddler Bikes using JavaScript click
        Return type: None
        Parameters: None
        """
        try:
            sleep(2)
            self.web_driver_helper.scroll_to_element_using_javascript(ProductListingLocators.toddler_bikes_text)
            self.web_driver_helper.click_element(ProductListingLocators.toddler_bikes_text)
            self.logger.info(f"Toddler bikes clicked")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "click_toddler_bikes_failure")
            self.logger.error(f"Failed to click toddler bikes: {e}")
            raise

    def verify_keyword_search(self):
        """
        Method name: verify_keyword_search
        Author name: Saptarshi
        Description: Verifies the 'Search' text is present in keyword search area
        Return type: None
        Parameters: None
        """
        try:
            self.web_driver_helper.verify_text_contains(ProductListingLocators.search_keyword,self.excel_reader.get_cell_value("saptarshiexcel",2,1))
            self.logger.info(f"Keyword search clicked")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "verify_keyword_search_failure")
            self.logger.error(f"Failed to verify keyword search text: {e}")
            raise

    def click_disney(self):
        """
        Method name: click_disney
        Author name: Saptarshi
        Description : Clicks on Disney option using JavaScript click
        Return type: None
        Parameters: None
        """
        try:
            self.web_driver_helper.scroll_to_element_using_javascript(ProductListingLocators.disney_checkbox)
            self.web_driver_helper.click_element(ProductListingLocators.disney_checkbox)
            sleep(2)
            self.logger.info(f"Disney page will appear")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "click_disney_failure")
            self.logger.error(f"Failed to click Disney option: {e}")
            raise


    def click_first_product(self):
        """
        Method name: click_first_product
        Author name: Saptarshi
        Description : Clicks on the first product on Disney page
        Return type: None
        Parameters: None
        """
        try:
            sleep(3)
            self.web_driver_helper.click_element(ProductListingLocators.first_product_link)
            self.logger.info("Verified First Product")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "click_first_product_failure")
            self.logger.error(f"Failed to click first product on Disney page: {e}")
            raise


    def outdoor_toys_product_listing_page_flow(self):
        """
            Method Name   : outdoor_toys_product_listing_page_flow
            Author        : Saptarshi Thakur
            Description   : Clutter function for the outdoor toys product listing page
            Return Type   : None
            Parameters    : None
        """
        self.verify_the_url_contain_bikes()
        self.click_on_show_more_text()
        self.click_on_huffy()
        self.click_toddler_bikes()
        self.verify_keyword_search()
        self.click_disney()
        self.click_first_product()

    # ============================================================================================================

    # TestCase 4

    def verify_creativity_page(self):
        """
        Method name: verify_creativity_page
        Author name: Saptarshi
        Description: Verifies that the current URL contains 'creativity'
        Return type: None
        Parameters: None
        """
        try:
            self.web_driver_helper.verify_current_url_contains(self.excel_reader.get_cell_value("saptarshiexcel",4,2))
            self.logger.info("Verified url of creativity page")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "verify_creativity_page_failure")
            self.logger.error(f"Failed to verify creativity page URL: {e}")
            raise

    def scroll_down_and_click_art_and_crafts(self):
        """
        Method name: scroll_down_and_click_art_and_crafts
        Author name: Saptarshi
        Description : Scrolls down to Arts and Crafts section and clicks it
        Return type: None
        Parameters: None
        """
        try:
            self.web_driver_helper.scroll_to_element_using_javascript(ProductListingLocators.arts_and_craft_text)
            self.web_driver_helper.click_element(ProductListingLocators.arts_and_craft_text)
            self.logger.info("Scroll down and clicked art and crafts")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "scroll_down_and_click_art_and_crafts_failure")
            self.logger.error(f"Failed to scroll/click arts and crafts: {e}")
            raise

    def click_creativity(self):
        """
        Method name: click_creativity
        Author name: Saptarshi
        Description: Clicks on the Creativity option using JavaScript click
        Return type: None
        Parameters: None
        """
        try:
            self.web_driver_helper.scroll_to_element_using_javascript(ProductListingLocators.creativity_checkbox)
            sleep(1)
            self.web_driver_helper.click_element(ProductListingLocators.creativity_checkbox)
            self.logger.info("creativity option clicked")
        except Exception as e:
            Screenshot.capture_browser_screenshot(self.web_driver, "click_creativity_failure")
            self.logger.error(f"Failed to click creativity option: {e}")
            raise

    def creativity_products_listing_page_flow(self):
        """
        Method Name   : creativity_products_listing_page_flow
        Author        : Saptarshi Thakur
        Description   : Clutter function for the creativity products listing page
        Return Type   : None
        Parameters    : None
        """
        self.verify_creativity_page()
        self.scroll_down_and_click_art_and_crafts()
        sleep(2)
        self.click_creativity()
        self.click_first_product()

    # =============================================================================================================
    # TestCase 5

    def verify_product_listing_page_loaded(self):
        """
        Method Name   : verify_product_listing_page_loaded
        Author        : Gitika Thakur
        Description   : Verifies Paw Patrol product listing page is loaded successfully
        Return Type   : None
        Parameters    : None
        """
        try:
            sleep(2)
            self.web_driver_helper.verify_current_url_contains(self.excel_reader.get_cell_value("gitikaexcel",2,2))
            self.logger.info("Paw Patrol is present in the URL")

            footer_visible = self.web_driver_helper.is_footer_visible_by_tag_name(self.web_driver, "footer")
            if not footer_visible:
                raise AssertionError("Footer not visible")

            self.logger.info("Paw Patrol product listing page loaded successfully")
        except Exception as e:
            self.logger.exception("Product listing page load validation failed")
            raise AssertionError(
                "Paw Patrol product listing page did not load properly"
            ) from e
    def click_playsets_filter(self):
        """
        Method Name   : click_playsets_filter
        Author        : Gitika Thakur
        Description   : Clicks on the Playsets filter option
        Return Type   : None
        Parameters    : None
        """
        try:
            self.web_driver_helper.click_element(ProductListingLocators.playsets_filter_option)
            self.logger.info("Clicked Playsets filter")
        except Exception as e:
            self.logger.exception("Click Playsets filter failed")
            raise AssertionError("Unable to click Playsets filter") from e
    def click_savings_filter(self):
        """
        Method Name   : click_savings_filter
        Author        : Gitika Thakur
        Description   : Clicks on the Savings filter option
        Return Type   : None
        Parameters    : None
        """
        try:
            self.web_driver_helper.click_element(ProductListingLocators.savings_filter_option)
            self.logger.info("Clicked Savings filter")
        except Exception as e:
            self.logger.exception("Click Savings filter failed")
            raise AssertionError("Unable to click Savings filter") from e
    def click_first_product_thumbnail(self):
        """
        Method Name   : click_first_product_thumbnail
        Author        : Gitika Thakur
        Description   : Clicks on the first product thumbnail from the listing page
        Return Type   : None
        Parameters    : None
        """
        try:
            sleep(2)
            self.web_driver_helper.click_element(ProductListingLocators.first_product_thumbnail_link)
            self.logger.info("Clicked first product thumbnail")
        except Exception as e:
            self.logger.exception("Click first product thumbnail failed")
            raise AssertionError("Unable to click first product thumbnail") from e
    def paw_patrol_product_listing_flow(self):
        """
        Method Name   : paw_patrol_product_listing_flow
        Author        : Gitika Thakur
        Description   : Clutter function for the paw patrol product listing page
        Return Type   : None
        Parameters    : None
        """
        self.verify_product_listing_page_loaded()
        self.click_playsets_filter()
        self.click_savings_filter()
        self.click_first_product_thumbnail()

# ================================================================================================================
    # Test Case 6

    def click_offers_and_verify_brands_section(self):
        """
        Method Name   : click_offers_and_verify_brands_section
        Author        : Gitika Thakur
        Description   : Clicks on Offers link and verifies Brands section is visible
        Return Type   : None
        Parameters    : None
        """
        try:
            self.web_driver_helper.click_element(ProductListingLocators.offers_navigation_link)
            self.web_driver_helper.verify_text_contains(ProductListingLocators.brands_navigation_link,self.excel_reader.get_cell_value("gitikaexcel",4,1))
            self.logger.info("Offers page verified and Brands section visible")
        except Exception as e:
            self.logger.exception("Offers page verification failed")
            raise AssertionError("Offers page validation failed") from e
    def click_dolls_category(self):
        """
        Method Name   : click_dolls_category
        Author        : Gitika Thakur
        Description   : Clicks on the Dolls category link from navigation
        Return Type   : None
        Parameters    : None
        """
        try:
            self.web_driver_helper.click_element(ProductListingLocators.dolls_category_link)
            self.logger.info("Clicked Dolls category")
        except Exception as e:
            self.logger.exception("Click Dolls category failed")
            raise AssertionError("Unable to click Dolls category") from e
    def click_first_doll_product_card(self):
        """
        Method Name   : click_first_doll_product_card
        Author        : Gitika Thakur
        Description   : Clicks on the first doll product card and verifies navigation
        Return Type   : None
        Parameters    : None
        """
        try:
            sleep(2)
            self.web_driver_helper.click_element(ProductListingLocators.first_product_card)
            self.web_driver_helper.verify_text_contains(ProductListingLocators.explore_navigation_link, self.excel_reader.get_cell_value("gitikaexcel",5,1))
            self.logger.info("First doll product opened successfully")
        except Exception as e:
            self.logger.exception("First doll product selection failed")
            raise AssertionError("Unable to open first doll product") from e

# ==========================================================================================================

    # Test Case 7

    def verify_url_contains_puzzles(self):
        """
        Method Name : verify_url_contains_puzzles
        Author      : Ashutosh
        Description : Verifies that the current URL contains the keyword 'Puzzles'
        Parameters  : None
        Return Type : None
        """
        try:
            self.web_driver_helper.verify_current_url_contains(self.excel_reader.get_cell_value("ashutoshExcel",2,2))
            self.logger.info("'Puzzles' keyword is present in the URL")
        except Exception as exc:
            Screenshot.capture_browser_screenshot(
                self.web_driver, "puzzles_verify_url_error"
            )
            self.logger.error(f"URL verification for Puzzles failed: {exc}")
            raise
    def click_show_more_button(self):
        """
        Method Name : click_show_more_button
        Author      : Ashutosh
        Description : Clicks on the 'Show More' button under Toy Type section
        Parameters  : None
        Return Type : None
        """
        try:
            self.web_driver_helper.click_element(
                ProductListingLocators.show_more_under_toy_type
            )
            self.logger.info("'Show More' button clicked")
        except Exception as exc:
            Screenshot.capture_browser_screenshot(
                self.web_driver, "puzzles_show_more_error"
            )
            self.logger.error(f"Failed to click Show More button: {exc}")
            raise
    def click_jigsaw_puzzles_filter(self):
        """
        Method Name : click_jigsaw_puzzles_filter
        Author      : Ashutosh
        Description : Clicks on the 'Jigsaw Puzzles' filter under Toy Type
        Parameters  : None
        Return Type : None
        """
        try:
            self.web_driver_helper.click_element(
                ProductListingLocators.jigsaw_puzzles_filter_under_toy_type
            )
            self.logger.info("'Jigsaw Puzzles' filter clicked")
            sleep(2)
        except Exception as exc:
            Screenshot.capture_browser_screenshot(
                self.web_driver, "puzzles_jigsaw_filter_error"
            )
            self.logger.error(f"Failed to click Jigsaw Puzzles filter: {exc}")
            raise
    def wait_until_page_loaded(self):
        """
        Method Name : wait_until_page_loaded
        Author      : Ashutosh
        Description : Verifies page load by checking URL keyword and footer visibility
        Parameters  : None
        Return Type : None
        """
        try:
            self.web_driver_helper.verify_current_url_contains("Jigsaw%20Puzzles")
            self.logger.info("'Jigsaw Puzzles' keyword is present in the URL")

            if self.web_driver_helper.is_footer_visible_by_tag_name(self.web_driver, "footer"):
                self.logger.info("Footer is visible on the page")
            else:
                raise AssertionError("Footer is not visible on the page")
        except Exception as exc:
            Screenshot.capture_browser_screenshot(
                self.web_driver, "puzzles_page_load_error"
            )
            self.logger.error(f"Page load verification failed: {exc}")
            raise
    def click_children_games_filter(self):
        """
        Method Name : click_children_games_filter
        Author      : Ashutosh
        Description : Clicks on the 'Children Games' filter under Toy Type
        Parameters  : None
        Return Type : None
        """
        try:
            self.web_driver_helper.click_element(
                ProductListingLocators.children_games_filter_under_toy_type
            )
            self.logger.info("'Children Games' filter clicked")
            sleep(2)
        except Exception as exc:
            Screenshot.capture_browser_screenshot(
                self.web_driver, "puzzles_children_games_filter_error"
            )
            self.logger.error(f"Failed to click Children Games filter: {exc}")
            raise
    def click_discover_world_filter(self):
        """
        Method Name : click_discover_world_filter
        Author      : Ashutosh
        Description : Clicks on the 'Discover World' filter under Learning Skills
        Parameters  : None
        Return Type : None
        """
        try:
            self.web_driver_helper.click_element(
                ProductListingLocators.discover_world_filter_under_learning_skills
            )
            self.logger.info("'Discover World' filter clicked")
        except Exception as exc:
            Screenshot.capture_browser_screenshot(
                self.web_driver, "puzzles_discover_world_filter_error"
            )
            self.logger.error(f"Failed to click Discover World filter: {exc}")
            raise
    def click_first_product_of_puzzles(self):
        """
        Method Name : click_first_product_of_puzzles
        Author      : Ashutosh
        Description : Clicks on the first product displayed in puzzles results
        Parameters  : None
        Return Type : None
        """
        try:
            sleep(2)
            self.web_driver_helper.click_element(
                ProductListingLocators.first_product_link
            )
            self.logger.info("First puzzles product clicked")
        except Exception as exc:
            Screenshot.capture_browser_screenshot(
                self.web_driver, "puzzles_first_product_error"
            )
            self.logger.error(f"Failed to click first puzzles product: {exc}")
            raise
    def work_flow_for_puzzles_product_page(self):
        """
        Method Name : work_flow
        Author      : Ashutosh
        Description : Executes the complete Puzzles product page workflow
        Parameters  : None
        Return Type : None
        """
        try:
            self.verify_url_contains_puzzles()
            self.click_show_more_button()
            self.click_jigsaw_puzzles_filter()
            self.wait_until_page_loaded()
            self.click_children_games_filter()
            self.click_discover_world_filter()
            self.click_first_product_of_puzzles()
        except Exception as exc:
            Screenshot.capture_browser_screenshot(
                self.web_driver, "puzzles_workflow_error"
            )
            self.logger.error(f"Puzzles workflow execution failed: {exc}")
            raise

# ==========================================================================================================
    # TestCase 8

    def verify_url_contains_cars(self):
        """
        Method Name : verify_url_contains_cars
        Author      : Ashutosh
        Description : Verifies that the current URL contains the keyword 'Cars'
        Parameters  : None
        Return Type : None
        """
        try:
            self.web_driver_helper.verify_current_url_contains(self.excel_reader.get_cell_value("ashutoshExcel",3,2))
            self.logger.info("'Cars' keyword is present in URL")
        except Exception as exc:
            Screenshot.capture_browser_screenshot(self.web_driver, "car_verify_url_cars_error")
            self.logger.error(f"URL verification failed: {exc}")
            raise
    def click_toy_cars_filter(self):
        """
        Method Name : click_toy_cars_filter
        Author      : Ashutosh
        Description : Clicks on the 'Toy Cars' filter option
        Parameters  : None
        Return Type : None
        """
        try:
            self.web_driver_helper.click_element(ProductListingLocators.toy_cars_filter_under_toy_type)
            self.logger.info("'Toy Cars' filter clicked")
        except Exception as exc:
            Screenshot.capture_browser_screenshot(self.web_driver, "car_toy_cars_filter_error")
            self.logger.error(f"Failed to click Toy Cars filter: {exc}")
            raise
    def hover_learning_skills_menu(self):
        """
        Method Name : hover_learning_skills_menu
        Author      : Ashutosh
        Description : Hovers over the 'Learning Skills' menu
        Parameters  : None
        Return Type : None
        """
        try:
            self.web_driver_helper.hover_over_element(ProductListingLocators.learning_skills_menu)
            self.logger.info("Hovered on Learning Skills menu")
        except Exception as exc:
            Screenshot.capture_browser_screenshot(self.web_driver, "car_hover_learning_skills_error")
            self.logger.error(f"Failed to hover on Learning Skills menu: {exc}")
            raise
    def click_imaginative_play_option(self):
        """
        Method Name : click_imaginative_play_option
        Author      : Ashutosh
        Description : Clicks on the 'Imaginative Play' option under Learning Skills
        Parameters  : None
        Return Type : None
        """
        try:
            self.web_driver_helper.click_element(ProductListingLocators.imaginative_play_filter_under_learning_skills)
            self.logger.info("'Imaginative Play' option clicked")
        except Exception as exc:
            Screenshot.capture_browser_screenshot(self.web_driver, "car_imaginative_play_click_error")
            self.logger.error(f"Failed to click Imaginative Play option: {exc}")
            raise
    def click_fine_motor_skills_filter(self):
        """
        Method Name : click_fine_motor_skills_filter
        Author      : Ashutosh
        Description : Clicks on the 'Fine Motor Skills' filter option
        Parameters  : None
        Return Type : None
        """
        try:
            self.web_driver_helper.click_element(ProductListingLocators.fine_motor_skills_filter_under_learning_skills)
            self.logger.info("'Fine Motor Skills' filter clicked")
        except Exception as exc:
            Screenshot.capture_browser_screenshot(self.web_driver, "car_fine_motor_skills_click_error")
            self.logger.error(f"Failed to click Fine Motor Skills filter: {exc}")
            raise
    def wait_until_page_loaded_and_verify_url(self):
        """
        Method Name : wait_until_page_loaded
        Author      : Ashutosh
        Description : Verifies page load by checking URL keyword and footer visibility
        Parameters  : None
        Return Type : None
        """
        try:
            sleep(2)
            self.web_driver_helper.verify_current_url_contains("skills")
            self.logger.info("'skills' keyword is present in the URL")

            if self.web_driver_helper.is_footer_visible_by_tag_name(self.web_driver, "footer"):
                self.logger.info("Footer is visible on the page")
            else:
                raise AssertionError("Footer is not visible on the page")
        except Exception as exc:
            Screenshot.capture_browser_screenshot(self.web_driver, "car_page_load_error")
            self.logger.error(f"Page load verification failed: {exc}")
            raise
    def click_first_product_of_cars(self):
        """
        Method Name : click_first_product_of_cars
        Author      : Ashutosh
        Description : Clicks on the first available car product
        Parameters  : None
        Return Type : None
        """
        try:
            sleep(2)
            self.web_driver_helper.click_element(ProductListingLocators.first_product_link)
            self.logger.info("First car product clicked")
        except Exception as exc:
            Screenshot.capture_browser_screenshot(self.web_driver, "car_first_product_click_error")
            self.logger.error(f"Failed to click first car product: {exc}")
            raise
    def work_flow(self):
        """
        Method Name : work_flow
        Author      : Ashutosh
        Description : Executes the complete Cars product page workflow
        Parameters  : None
        Return Type : None
        """
        try:
            self.verify_url_contains_cars()
            self.click_show_more_button()
            self.click_toy_cars_filter()
            self.hover_learning_skills_menu()
            self.click_imaginative_play_option()
            self.click_fine_motor_skills_filter()
            self.wait_until_page_loaded_and_verify_url()
            self.click_first_product_of_cars()
        except Exception as exc:
            Screenshot.capture_browser_screenshot(self.web_driver, "car_workflow_error")
            self.logger.error(f"Cars workflow execution failed: {exc}")
            raise