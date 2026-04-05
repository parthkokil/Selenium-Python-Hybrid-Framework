import pytest
from base import BaseTest

from pages.bikes_page import BikesPage
from pages.brands_page import BrandsPage
from pages.car_page import CarPage
from pages.cart_page import CartPage
from pages.creativity_filter_page import CreativityFilterPage
from pages.creativity_page import CreativityPage
from pages.disney_page import DisneyPage
from pages.explore_page import ExplorePage
from base import BaseTest
from pages.footer_links_page import CaseTenPage
from pages.home_page import HomePage
from pages.huffy_page import HuffyPage
from pages.newborn_gifts_page import NewbornGiftsPage
from pages.product_page import ProductPage
from pages.search_page import SearchPage
from pages.soft_toys_page import SoftToysPage
from pages.elc_footer_support_page import ElcFooterSupportPage
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

    def setUp(self):
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

    def tearDown(self):
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

    # 1st testCase
    @pytest.mark.smoke
    def test_newborn_gifts_navigation(self):
        """
        Author: Karuna
        Description: Validates newborn gifts navigation.
        """
        try:
            newborn_gifts_page = NewbornGiftsPage(self.driver, self.logger)
            newborn_gifts_page.clutter()
        except Exception as exc:
            Screenshot.capture_screenshot(
                self.driver, "test_newborn_gifts_navigation_failure"
            )
            self.logger.error(
                "Newborn gifts navigation failed: %s", exc
            )
            raise

    # 2nd testCase
    @pytest.mark.smoke
    def test_soft_toys_navigation(self):
        """
        Author: Karuna
        Description: Validates soft toys navigation.
        """
        try:
            soft_toys_page = SoftToysPage(self.driver, self.logger)
            soft_toys_page.clutter2()
        except Exception as exc:
            Screenshot.capture_screenshot(
                self.driver, "test_soft_toys_navigation_failure"
            )
            self.logger.error(
                "Soft toys navigation failed: %s", exc
            )
            raise
 

    # 3rd TestCase
    @pytest.mark.smoke
    def test_bikes_huffy_disney_product_flow(self):
        """
        Author: Saptarshi
        Description:
            Home → Bikes → Huffy → Disney → Product flow.
        """
        try:
            home_page = HomePage(self.driver, self.logger)
            bikes_page = BikesPage(self.driver, self.logger)
            huffy_page = HuffyPage(self.driver, self.logger)
            disney_page = DisneyPage(self.driver, self.logger)
            product_page = ProductPage(self.driver, self.logger)
    
            home_page.home_page_clutter()
            bikes_page.bike_page_clutter()
            huffy_page.huffy_page_clutter()
            disney_page.disney_page_clutter()
            product_page.product_page_clutter()
    
        except Exception as exc:
            Screenshot.capture_screenshot(
                self.driver, "test_bikes_huffy_disney_product_flow_failure"
            )
            self.logger.error(
                "Bikes–Huffy–Disney product flow failed: %s", exc
            )
            raise
    
    # 4th TestCase
    @pytest.mark.smoke
    def test_creativity_product_cart_flow(self):
        """
        Author: Saptarshi
        Description:
            Home → Creativity → Filter → Product → Cart flow.
        """
        try:
             home_page = HomePage(self.driver, self.logger)
             creativity_page = CreativityPage(self.driver, self.logger)
             creativity_filter_page = CreativityFilterPage(self.driver, self.logger)
             product_page = ProductPage(self.driver, self.logger)
             cart_page = CartPage(self.driver, self.logger)

             home_page.home_page_clutter2()
             creativity_page.creativity_page_clutter()
             creativity_filter_page.creativity_filter_page_clutter()
             product_page.product_page_clutter2()
             cart_page.cart_page_clutter()

        except Exception as exc:
             Screenshot.capture_screenshot(
                 self.driver, "test_creativity_product_cart_flow_failure"
             )
             self.logger.error(
                 "Creativity product cart flow failed: %s", exc
             )
             raise

    # 5th TestCase
    @pytest.mark.smoke
    def test_paw_patrol_add_to_basket(self):
        """
        Test Name: test_paw_patrol_add_to_basket
        Author: Gitika
        Description:
            Verifies Paw Patrol product add-to-basket flow.
        Return Type: None
        Parameters: None
        """
        try:
            tc5 = BrandsPage(self.driver, self.logger)
            tc5.run_test_case_5_flow()
            self.logger.info("Paw Patrol add-to-basket test executed successfully")
        except Exception as exc:
            self.logger.error(f"test_paw_patrol_add_to_basket failed: {exc}")
            raise

    # 6th TestCase
    @pytest.mark.smoke
    def test_dolls_checkout(self):
        """
        Test Name: test_dolls_checkout
        Author: Gitika
        Description:
            Verifies Dolls category checkout flow.
        Return Type: None
        Parameters: None
        """
        try:
            tc6 = ExplorePage(self.driver, self.logger)
            tc6.run_test_case_6_flow()
            self.logger.info("Dolls checkout test executed successfully")
        except Exception as exc:
            self.logger.error(f"test_dolls_checkout failed: {exc}")
            raise

    # 7th Test Case
    @pytest.mark.smoke
    def test_search_functionality_flow(self):
        """
        Author: Ashutosh
        Description: Validates search workflow.
        """
        try:
            search_page = SearchPage(self.driver, self.logger)
            search_page.work_flow()
        except Exception as exc:
            Screenshot.capture_screenshot(
                self.driver, "test_search_functionality_flow_failure"
            )
            self.logger.error(
                "Search functionality flow failed: %s", exc
            )
            raise


    # 8th Test Case
    @pytest.mark.smoke
    def test_car_category_navigation(self):
        """
        Author: Ashutosh
        Description: Validates car category navigation.
        """
        try:
            car_page = CarPage(self.driver, self.logger)
            car_page.work_flow()
        except Exception as exc:
            Screenshot.capture_screenshot(
                self.driver, "test_car_category_navigation_failure"
            )
            self.logger.error(
                "Car category navigation failed: %s", exc
            )
            raise


    # 9th Test Case
    @pytest.mark.smoke
    def test_elc_support_footer_flow(self):
        """
        Author: Sasikumar
        Description: Executes Test Case 9 flow.
        """
        try:
            test_case_nine_page = ElcFooterSupportPage(self.driver, self.logger)
            test_case_nine_page.elc_footer_pages_flow()
        except Exception as exc:
            Screenshot.capture_screenshot(
                self.driver, "test_case_nine_flow_failure"
            )
            self.logger.error(
                "Test Case 9 flow failed: %s", exc
            )
            raise

    # 10th TestCase
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
    