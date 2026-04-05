from utilities.webDriverHelper import WebDriverHelper
from uistore.car_page_locator import CarPageLocators
from utilities.screenshot import Screenshot
from utilities.report import AllureReporter
from time import sleep


class CarPage:
    """
    Page Class Name: CarPage
    Author: Ashutosh
    Description:
        Handles actions and verifications for the Car page workflow.
    """

    def __init__(self, driver, logger):
        """
        Method Name: __init__
        Author: Ashutosh
        Description: Initializes CarPage with driver and logger
        Parameters: driver (WebDriver), logger (Logger)
        Return Type: None
        """
        try:
            self.driver = driver
            self.logger = logger
            self.reporter = AllureReporter()
            self.helper = WebDriverHelper(self.driver)
            self.logger.info("CarPage initialized successfully")
        except Exception as exc:
            self.logger.error(f"CarPage initialization failed: {exc}")
            raise

    def click_accept_cookies_popup(self):
        """
        Method Name: click_accept_cookies_popup
        Author: Ashutosh
        Description: Clicks the cookie consent popup accept button
        Return Type: None
        """
        try:
            self.helper.click(CarPageLocators.ACCEPT_COOKIES_BUTTON)
            self.logger.info("Cookies popup accepted successfully")
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "car_accept_cookies_popup_error")
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
            self.helper.is_element_visible(CarPageLocators.ELC_LOGO_IMAGE)
            self.logger.info("ELC logo is present on the page")
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "car_elc_logo_verification_error")
            self.logger.error(f"Failed to verify ELC logo: {exc}")
            raise

    def click_search_input_field(self):
        """
        Method Name: click_search_input_field
        Author: Ashutosh
        Description: Clicks on the search input field
        Return Type: None
        """
        try:
            self.helper.click(CarPageLocators.SEARCH_INPUT_FIELD)
            self.logger.info("Clicked on search input field")
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "car_click_search_input_error")
            self.logger.error(f"Failed to click search input field: {exc}")
            raise

    def enter_search_text_and_submit(self):
        """
        Method Name: enter_search_text_and_submit
        Author: Ashutosh
        Description: Enters 'Cars' in search field and submits
        Return Type: None
        """
        try:
            self.helper.send_keys(CarPageLocators.SEARCH_INPUT_FIELD, "Cars")
            sleep(2)
            self.helper.click(CarPageLocators.SEARCH_SUBMIT_BUTTON)
            self.logger.info("'Cars' entered and search submitted")
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "car_enter_text_submit_error")
            self.logger.error(f"Failed to enter search text and submit: {exc}")
            raise

    def verify_url_contains_cars(self):
        """
        Method Name: verify_url_contains_cars
        Author: Ashutosh
        Description: Verifies URL contains 'Cars'
        Return Type: None
        """
        try:
            self.helper.verify_url("Cars")
            self.logger.info("'Cars' is present in URL")
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "car_verify_url_cars_error")
            self.logger.error(f"URL verification failed: {exc}")
            raise

    def click_show_more_button(self):
        """
        Method Name: click_show_more_button
        Author: Ashutosh
        Description: Clicks on 'Show more' button
        Return Type: None
        """
        try:
            self.helper.click(CarPageLocators.SHOW_MORE_BUTTON)
            self.logger.info("'Show more' button clicked")
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "car_show_more_click_error")
            self.logger.error(f"Failed to click 'Show more' button: {exc}")
            raise

    def click_toy_cars_filter(self):
        """
        Method Name: click_toy_cars_filter
        Author: Ashutosh
        Description: Clicks on 'Toy Cars' filter
        Return Type: None
        """
        try:
            self.helper.click(CarPageLocators.TOY_CARS_FILTER)
            self.logger.info("'Toy Cars' filter clicked")
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "car_toy_cars_filter_error")
            self.logger.error(f"Failed to click 'Toy Cars' filter: {exc}")
            raise

    def hover_learning_skills_menu(self):
        """
        Method Name: hover_learning_skills_menu
        Author: Ashutosh
        Description: Hovers over 'Learning Skills' menu
        Return Type: None
        """
        try:
            self.helper.hover(CarPageLocators.LEARNING_SKILLS_MENU)
            self.logger.info("Hovered on 'Learning Skills'")
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "car_hover_learning_skills_error")
            self.logger.error(f"Failed to hover on Learning Skills: {exc}")
            raise

    def click_imaginative_play_option(self):
        """
        Method Name: click_imaginative_play_option
        Author: Ashutosh
        Description: Clicks on 'Imaginative Play' option
        Return Type: None
        """
        try:
            self.helper.click(CarPageLocators.IMAGINATIVE_PLAY_OPTION)
            self.logger.info("'Imaginative Play' option clicked")
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "car_imaginative_play_click_error")
            self.logger.error(f"Failed to click Imaginative Play: {exc}")
            raise

    def click_fine_motor_skills_filter(self):
        """
        Method Name: click_fine_motor_skills_filter
        Author: Ashutosh
        Description: Clicks on 'Fine Motor Skills' filter
        Return Type: None
        """
        try:
            self.helper.click(CarPageLocators.FINE_MOTOR_SKILLS_FILTER)
            self.logger.info("'Fine Motor Skills' filter clicked")
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "car_fine_motor_skills_click_error")
            self.logger.error(f"Failed to click Fine Motor Skills: {exc}")
            raise

    def wait_until_page_loaded(self):
        """
        Method Name: wait_until_page_loaded
        Author: Ashutosh
        Description: Verifies page load using URL and footer visibility
        Return Type: None
        """
        try:
            self.helper.verify_url("skills")
            self.logger.info("'skills' is present in the page URL")

            is_visible = self.helper.is_footer_visible_by_tag(self.driver, "footer")
            if is_visible:
                self.logger.info("Footer tag is present and visible on the page")
            else:
                self.logger.error("Footer tag was NOT found or is not visible")
                raise AssertionError("Page load failed: Footer tag not visible.")
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "car_page_load_error")
            self.logger.error(f"Page load verification failed: {exc}")
            raise

    def click_first_product(self):
        """
        Method Name: click_first_product
        Author: Ashutosh
        Description: Clicks on the first product
        Return Type: None
        """
        try:
            sleep(2)
            self.helper.click(CarPageLocators.FIRST_PRODUCT_LINK)
            self.logger.info("First product clicked")
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "car_first_product_click_error")
            self.logger.error(f"Failed to click first product: {exc}")
            raise

    def verify_heading_and_add_to_wishlist(self):
        """
        Method Name: verify_heading_and_add_to_wishlist
        Author: Ashutosh
        Description:
            Verifies 'Early' keyword on product heading, captures screenshot,
            and clicks 'Add to Wishlist'
        Return Type: None
        """
        try:
            sleep(2)
            self.helper.verify_text(CarPageLocators.PRODUCT_HEADING_TEXT, "Early")
            self.logger.info("'Early' keyword is present")

            Screenshot.capture_screenshot(self.driver, "early")
            self.logger.info("Screenshot captured with name: early")

            self.helper.click(CarPageLocators.ADD_TO_WISHLIST_BUTTON)
            self.logger.info("'Add to Wishlist' button clicked")
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "car_add_to_wishlist_error")
            self.logger.error(f"Failed to verify heading or add to wishlist: {exc}")
            raise

    def work_flow(self):
        """
        Method Name: work_flow
        Author: Ashutosh
        Description: Executes the complete Car page workflow
        Return Type: None
        """
        try:
            self.click_accept_cookies_popup()
            self.verify_elc_logo_visible()
            self.click_search_input_field()
            self.enter_search_text_and_submit()
            self.verify_url_contains_cars()
            self.click_show_more_button()
            self.click_toy_cars_filter()
            self.hover_learning_skills_menu()
            self.click_imaginative_play_option()
            self.click_fine_motor_skills_filter()
            self.wait_until_page_loaded()
            self.click_first_product()
            self.verify_heading_and_add_to_wishlist()
        except Exception as exc:
            Screenshot.capture_screenshot(self.driver, "car_workflow_error")
            self.logger.error(f"Car workflow execution failed: {exc}")
            raise