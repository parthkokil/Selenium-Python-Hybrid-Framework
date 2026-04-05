from utilities.webDriverHelper import WebDriverHelper
from uistore.search_bar_locator import SearchBarLocators
from utilities.screenshot import Screenshot
from utilities.report import AllureReporter
from time import sleep


class SearchPage:
    """
    Page Class Name: SearchPage
    Author: Ashutosh
    Description:
        Handles actions and verifications for the Search workflow.
    """

    def __init__(self, driver, logger):
        """
        Method Name: __init__
        Author: Ashutosh
        Description: Initializes SearchPage with driver and logger
        Parameters: driver (WebDriver), logger (Logger)
        Return Type: None
        """
        try:
            self.driver = driver
            self.logger = logger
            self.reporter = AllureReporter()
            self.helper = WebDriverHelper(self.driver)
            self.logger.info("SearchPage initialized successfully")
        except Exception as exc:
            self.logger.error(f"SearchPage initialization failed: {exc}")
            raise

    def click_accept_cookies_popup(self):
        """
        Method Name: click_accept_cookies_popup
        Author: Ashutosh
        Description: Clicks the cookie consent popup accept button
        Return Type: None
        """
        try:
            self.helper.click(SearchBarLocators.ACCEPT_COOKIES_BUTTON)
            self.logger.info("Cookies popup accepted successfully")
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "search_accept_cookies_popup_error")
            self.logger.error(f"Failed to click cookies popup: {exc}")
            raise

    def verify_elc_logo_visible(self):
        """
        Method Name: verify_elc_logo_visible
        Author: Ashutosh
        Description: Verifies ELC logo is visible on the page
        Return Type: None
        """
        try:
            self.helper.is_element_visible(SearchBarLocators.ELC_LOGO_IMAGE)
            self.logger.info("ELC logo is visible on the page")
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "search_elc_logo_verification_error")
            self.logger.error(f"Failed to verify ELC logo visibility: {exc}")
            raise

    def click_search_input_field(self):
        """
        Method Name: click_search_input_field
        Author: Ashutosh
        Description: Clicks on the search input field
        Return Type: None
        """
        try:
            self.helper.click(SearchBarLocators.SEARCH_INPUT_FIELD)
            self.logger.info("Clicked on search input field")
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "search_click_input_error")
            self.logger.error(f"Failed to click search input field: {exc}")
            raise

    def enter_search_text_and_submit(self):
        """
        Method Name: enter_search_text_and_submit
        Author: Ashutosh
        Description: Enters 'Puzzles' in search field and clicks submit
        Return Type: None
        """
        try:
            self.helper.send_keys(SearchBarLocators.SEARCH_INPUT_FIELD, "Puzzles")
            sleep(2)
            self.helper.click(SearchBarLocators.SEARCH_SUBMIT_BUTTON)
            self.logger.info("Entered 'Puzzles' and submitted search")
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "search_enter_text_submit_error")
            self.logger.error(f"Failed to enter search text and submit: {exc}")
            raise

    def verify_url_contains_puzzles(self):
        """
        Method Name: verify_url_contains_puzzles
        Author: Ashutosh
        Description: Verifies URL contains 'Puzzles'
        Return Type: None
        """
        try:
            self.helper.verify_url("Puzzles")
            self.logger.info("'Puzzles' is present in the URL")
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "search_verify_url_puzzles_error")
            self.logger.error(f"URL verification for 'Puzzles' failed: {exc}")
            raise

    def click_show_more_button(self):
        """
        Method Name: click_show_more_button
        Author: Ashutosh
        Description: Clicks on the 'Show more' button
        Return Type: None
        """
        try:
            self.helper.click(SearchBarLocators.SHOW_MORE_BUTTON)
            self.logger.info("'Show more' button clicked")
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "search_show_more_error")
            self.logger.error(f"Failed to click 'Show more' button: {exc}")
            raise

    def click_jigsaw_puzzles_filter(self):
        """
        Method Name: click_jigsaw_puzzles_filter
        Author: Ashutosh
        Description: Clicks on the 'Jigsaw' puzzles filter
        Return Type: None
        """
        try:
            self.helper.click(SearchBarLocators.JIGSAW_PUZZLES_FILTER)
            self.logger.info("'Jigsaw Puzzles' filter clicked")
            sleep(2)
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "search_jigsaw_filter_error")
            self.logger.error(f"Failed to click 'Jigsaw Puzzles' filter: {exc}")
            raise

    def wait_until_page_loaded(self):
        """
        Method Name: wait_until_page_loaded
        Author: Ashutosh
        Description:
            Verifies page load by checking URL and footer visibility
        Return Type: None
        """
        try:
            self.helper.verify_url("Jigsaw%20Puzzles")
            self.logger.info("'Jigsaw%20Puzzles' is present in the URL")

            is_visible = self.helper.is_footer_visible_by_tag(self.driver, "footer")
            if is_visible:
                self.logger.info("Footer tag is present and visible on the page")
            else:
                self.logger.error("Footer tag was NOT found or is not visible")
                raise AssertionError("Page load failed: Footer tag not visible.")
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "search_page_load_error")
            self.logger.error(f"Page load verification failed: {exc}")
            raise

    def click_children_games_filter(self):
        """
        Method Name: click_children_games_filter
        Author: Ashutosh
        Description: Clicks on 'Children Games' filter
        Return Type: None
        """
        try:
            self.helper.click(SearchBarLocators.CHILDREN_GAMES_FILTER)
            self.logger.info("'Children Games' filter clicked")
            sleep(2)
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "search_children_games_error")
            self.logger.error(f"Failed to click 'Children Games' filter: {exc}")
            raise

    def click_discover_world_filter(self):
        """
        Method Name: click_discover_world_filter
        Author: Ashutosh
        Description: Clicks on 'Discover World' filter
        Return Type: None
        """
        try:
            self.helper.click(SearchBarLocators.DISCOVER_WORLD_FILTER)
            self.logger.info("'Discover World' filter clicked")
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "search_discover_world_error")
            self.logger.error(f"Failed to click 'Discover World' filter: {exc}")
            raise

    def click_first_product(self):
        """
        Method Name: click_first_product
        Author: Ashutosh
        Description: Clicks the first product in results
        Return Type: None
        """
        try:
            sleep(2)
            self.helper.click(SearchBarLocators.FIRST_PRODUCT_LINK)
            self.logger.info("First product clicked")
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "search_first_product_error")
            self.logger.error(f"Failed to click first product: {exc}")
            raise

    def add_product_to_wishlist_and_verify_learning(self):
        """
        Method Name: add_product_to_wishlist_and_verify_learning
        Author: Ashutosh
        Description:
            Clicks 'Add to Wishlist', verifies 'Learning' text, takes screenshot
        Return Type: None
        """
        try:
            self.helper.click(SearchBarLocators.ADD_TO_WISHLIST_BUTTON)
            self.logger.info("'Add to Wishlist' button clicked")

            self.helper.verify_text(SearchBarLocators.LEARNING_DESCRIPTOR_TEXT, "Learning")
            self.logger.info("'Learning' keyword is present")

            Screenshot.capture_screenshot(self.driver, "learn")
            self.logger.info("Screenshot captured with name: learn")
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "search_add_to_wishlist_error")
            self.logger.error(f"Failed to add to wishlist or verify learning text: {exc}")
            raise

    def work_flow(self):
        """
        Method Name: work_flow
        Author: Ashutosh
        Description: Executes the complete search workflow
        Return Type: None
        """
        try:
            self.click_accept_cookies_popup()
            self.verify_elc_logo_visible()
            self.click_search_input_field()
            self.enter_search_text_and_submit()
            self.verify_url_contains_puzzles()
            self.click_show_more_button()
            self.click_jigsaw_puzzles_filter()
            self.wait_until_page_loaded()
            self.click_children_games_filter()
            self.click_discover_world_filter()
            self.click_first_product()
            self.add_product_to_wishlist_and_verify_learning()
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "search_workflow_error")
            self.logger.error(f"Search workflow execution failed: {exc}")
            raise