import pytest
from base import BaseTest
from selenium import webdriver

# from pages.bikes_page import BikesPage
# from pages.brands_page import BrandsPage
# from pages.car_page import CarPage
# from pages.cart_page import CartPage
# from pages.creativity_filter_page import CreativityFilterPage
# from pages.creativity_page import CreativityPage
# from pages.disney_page import DisneyPage
# from pages.explore_page import ExplorePage
from Project.base import BaseTest
from pages.footer_links_page import CaseTenPage
# from pages.home_page import HomePage
# from pages.huffy_page import HuffyPage
# from pages.newborn_gifts_page import NewbornGiftsPage
# from pages.product_page import ProductPage
# from pages.search_page import SearchPage
# from pages.soft_toys_page import SoftToysPage
# from pages.elc_footer_support_page import ElcFooterSupportPage
from utilities.logger import get_logger
from utilities.config_reader import ConfigReader
from utilities.screenshot import Screenshot


class TestCaseTenFooterLinks(BaseTest):
    """
    Test Suite Name: TestCaseTenFooterLinks
    Author: Parth
    Description:
        Smoke test suite covering footer links, search,
        category navigation, and product workflows.
    """

    logger = get_logger()

    def setup_method(self):
        """
        Method Name: setup_method
        Author: Parth
        Description:
            Initializes WebDriver and opens application URL.
        """
        try:
            self.driver = self.setUpDriver()
            self.config_reader = ConfigReader()
            application_url = self.config_reader.get_data("CASETEN", "url")
            self.driver.get(application_url)
            timeout_seconds = int(self.config_reader.get_data("CASETEN", "timeout"))
            self.driver.implicitly_wait(timeout_seconds)
            self.driver.maximize_window()

            self.logger.info(
                "Browser launched and application opened: %s", application_url
            )
        except Exception as exc:
            self.logger.exception("Setup failed.")
            raise RuntimeError(
                "Setup failed for TestCaseTenFooterLinks."
            ) from exc

    def teardown_method(self):
        """
        Method Name: teardown_method
        Author: Parth
        Description:
            Closes the browser instance.
        """
        try:
            if getattr(self, "driver", None):
                self.driver.quit()
            self.logger.info("Browser closed successfully.")
        except Exception as exc:
            self.logger.exception("Teardown failed.")
            raise RuntimeError(
                "Teardown failed for TestCaseTenFooterLinks."
            ) from exc

    @pytest.mark.smoke
    def test_case_ten_footer_links_navigation(self):
        """
        Author: Parth
        Description: Validates footer useful links navigation.
        """
        try:
            footer_links_page = CaseTenPage(self.driver, self.logger)
            footer_links_page.run_case_ten()
        except Exception as exc:
            Screenshot.capture_screenshot(
                self.driver, "test_case_ten_footer_links_navigation_failure"
            )
            self.logger.error(
                "Footer links navigation failed: %s", exc
            )
            raise
