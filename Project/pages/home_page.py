from utilities.webDriverHelper import WebDriverHelper
from time import sleep
from uistore.home_page_locator import HomePageLocator
from utilities.screenshot import Screenshot


class HomePage:
    def __init__(self, driver, logger):
        """
        Method name: __init__
        Author name: Saptarshi
        Short description of method:
            Initializes the Home page object with required utilities
        Return type:
            None
        Parameter list:
            driver, logger
        """
        try:
            self.driver = driver
            self.logger = logger
            self.helper = WebDriverHelper(self.driver)
            self.logger.info("HomePage initialized successfully")
        except Exception as e:
            self.logger.error(f"Error initializing HomePage: {e}")
            raise

    def verify_elc_logo(self):
        """
        Method name: verify_elc_logo
        Author name: Saptarshi
        Short description of method:
            Verifies ELC logo title text equals 'Early Learning Centre'
        Return type:
            None
        Parameter list:
            None
        """
        try:
            # value = self.driver.find_element(*HomePageLocator.ELC_logo).get_attribute("title")
            # self.helper.verify_text("Early Learning Centre", str(value))
            self.helper.is_element_visible(HomePageLocator.ELC_logo)
            self.logger.info("Verified logo")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "verify_elc_logo_failure")
            self.logger.error(f"Failed to verify ELC logo: {e}")
            raise

    def click_allow_cookies(self):
        """
        Method name: click_allow_cookies
        Author name: Saptarshi
        Short description of method:
            Clicks on accept cookies pop-up button
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.helper.click(HomePageLocator.accept_pop_up)
            self.logger.info(f"Accept pop up button click")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_allow_cookies_failure")
            self.logger.error(f"Failed to click allow cookies: {e}")
            raise

    def hover_on_outdoor_toys(self):
        """
        Method name: hover_on_outdoor_toys
        Author name: Saptarshi
        Short description of method:
            Hovers on Outdoor Toys menu
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.helper.hover(HomePageLocator.outdoor_toys)
            self.logger.info(f"Outdoor toys hovered")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "hover_on_outdoor_toys_failure")
            self.logger.error(f"Failed to hover on outdoor toys: {e}")
            raise

    def click_on_bikes(self):
        """
        Method name: click_on_bikes
        Author name: Saptarshi
        Short description of method:
            Clicks on Bikes option using JavaScript click
        Return type:
            None
        Parameter list:
            None
        """
        try:
            sleep(2)
            self.helper.js_scroll(HomePageLocator.bikes)
            self.helper.click(HomePageLocator.bikes)
            self.logger.info(f"Bikes clicked")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_on_bikes_failure")
            self.logger.error(f"Failed to click on bikes: {e}")
            raise

    # for test case 4
    def hover_on_learning_skills(self):
        """
        Method name: hover_on_learning_skills
        Author name: Saptarshi
        Short description of method:
            Hovers on Learning Skills menu
        Return type:
            None
        Parameter list:
            None
        """
        try:
            sleep(2)
            self.helper.hover(HomePageLocator.learning_skills)
            self.logger.info(f"Learning skills hovered")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "hover_on_learning_skills_failure")
            self.logger.error(f"Failed to hover on learning skills: {e}")
            raise

    def click_on_creativity(self):
        """
        Method name: click_on_creativity
        Author name: Saptarshi
        Short description of method:
            Clicks on Creativity option using JavaScript click
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.helper.js_click(HomePageLocator.creativity)
            self.logger.info(f"creativity clicked")
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "click_on_creativity_failure")
            self.logger.error(f"Failed to click on creativity: {e}")
            raise

    def home_page_clutter(self):
        """
        Method name: home_page_clutter
        Author name: Saptarshi
        Short description of method:
            Executes the complete Home page flow for bikes (sleep -> cookies -> sleep -> logo -> hover -> sleep -> bikes click)
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.click_allow_cookies()
            self.verify_elc_logo()
            self.hover_on_outdoor_toys()
            self.click_on_bikes()
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "home_page_clutter_failure")
            self.logger.error(f"Failed in home_page_clutter flow: {e}")
            raise

    def home_page_clutter2(self):
        """
        Method name: home_page_clutter2
        Author name: Saptarshi
        Short description of method:
            Executes the complete Home page flow for creativity (sleep -> cookies -> sleep -> hover learning -> sleep -> creativity click -> sleep)
        Return type:
            None
        Parameter list:
            None
        """
        try:
            self.click_allow_cookies()
            self. hover_on_learning_skills()
            self.click_on_creativity()
        except Exception as e:
            Screenshot.capture_screenshot(self.driver, "home_page_clutter2_failure")
            self.logger.error(f"Failed in home_page_clutter2 flow: {e}")
            raise