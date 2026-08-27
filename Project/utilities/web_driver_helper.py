import traceback
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    WebDriverException,
    TimeoutException,
    StaleElementReferenceException
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class WebDriverHelper:
    """
    Class Name    : WebDriverHelper
    Author        : Parth
    Description   : Provides reusable Selenium WebDriver actions, waits, and verification utilities
    Return Type   : Object
    Parameters    : web_driver(object), timeout(int)
    """

    MAX_RETRIES = 3

    def __init__(self, web_driver, timeout=10):
        self.web_driver = web_driver
        self.web_driver_wait = WebDriverWait(self.web_driver, timeout)

    # -------------------------------------------------------------------------
    # Retry Helpers (No lambda, simple syntax)
    # -------------------------------------------------------------------------

    def retry_on_stale_click(self, element, delay_seconds=1):
        """
        Retries element.click() if StaleElementReferenceException occurs.
        """
        attempts = 0
        while attempts < self.MAX_RETRIES:
            try:
                element.click()
                return
            except StaleElementReferenceException as exception:
                attempts += 1
                if attempts == self.MAX_RETRIES:
                    raise RuntimeError(
                        f"Element became stale after {self.MAX_RETRIES} retries"
                    ) from exception
                sleep(delay_seconds)

    def retry_on_stale_send_keys(self, element, input_text, delay_seconds=0.3):
        """
        Retries element.send_keys(input_text) if StaleElementReferenceException occurs.
        """
        attempts = 0
        while attempts < self.MAX_RETRIES:
            try:
                element.send_keys(input_text)
                return
            except StaleElementReferenceException as exception:
                attempts += 1
                if attempts == self.MAX_RETRIES:
                    raise RuntimeError(
                        f"Element became stale after {self.MAX_RETRIES} retries"
                    ) from exception
                sleep(delay_seconds)

    def retry_on_stale_get_text(self, element, delay_seconds=0.3):
        """
        Retries reading element.text if StaleElementReferenceException occurs.
        Returns text when successful.
        """
        attempts = 0
        while attempts < self.MAX_RETRIES:
            try:
                return element.text
            except StaleElementReferenceException as exception:
                attempts += 1
                if attempts == self.MAX_RETRIES:
                    raise RuntimeError(
                        f"Element became stale after {self.MAX_RETRIES} retries"
                    ) from exception
                sleep(delay_seconds)

        raise RuntimeError("Max retries exceeded")

    # -------------------------------------------------------------------------
    # Element Actions
    # -------------------------------------------------------------------------

    def click_element(self, element_locator):
        """
        Method Name   : click_element
        Author        : Parth
        Description   : Clicks on an element after it becomes clickable.
                        Handles StaleElementReferenceException by RE-FINDING
                        the element on each retry attempt.
        Return Type   : None
        Parameters    : element_locator(tuple)
        """
        attempts = 0
        while attempts < self.MAX_RETRIES:
            try:
                # Re-find the element every retry (this is the key fix!)
                clickable_element = self.web_driver_wait.until(
                    EC.element_to_be_clickable(element_locator)
                )
                clickable_element.click()
                return
            except StaleElementReferenceException:
                attempts += 1
                sleep(1)  # Small pause to let DOM settle
                if attempts == self.MAX_RETRIES:
                    raise Exception(
                        f"Element {element_locator} remained stale after {self.MAX_RETRIES} retries"
                    )
            except (TimeoutException, WebDriverException) as exception:
                traceback.print_exc()
                raise Exception(f"Failed to click element {element_locator}: {exception}")


    def enter_text(self, element_locator, input_text):
        """
        Method Name   : enter_text
        Author        : Parth
        Description   : Sends text to a visible input field
        Return Type   : None
        Parameters    : element_locator(tuple), input_text(str)
        """
        try:
            visible_element = self.web_driver_wait.until(
                EC.visibility_of_element_located(element_locator)
            )
            self.retry_on_stale_send_keys(visible_element, input_text)
        except (TimeoutException, WebDriverException, RuntimeError) as exception:
            traceback.print_exc()
            raise Exception(f"Failed to enter text in {element_locator}: {exception}")

    def hover_over_element(self, element_locator):
        """
        Method Name   : hover_over_element
        Author        : Parth
        Description   : Performs mouse hover over an element
        Return Type   : None
        Parameters    : element_locator(tuple)
        """
        try:
            target_element = self.web_driver_wait.until(
                EC.visibility_of_element_located(element_locator)
            )
            ActionChains(self.web_driver).move_to_element(target_element).perform()
        except (TimeoutException, WebDriverException) as exception:
            traceback.print_exc()
            raise Exception(f"Failed to hover over element {element_locator}: {exception}")

    def scroll_to_element_using_javascript(self, element_locator):
        """
        Method Name   : scroll_to_element_using_javascript
        Author        : Parth
        Description   : Scrolls the page until the element is visible
        Return Type   : None
        Parameters    : element_locator(tuple)
        """
        try:
            target_element = self.web_driver_wait.until(
                EC.visibility_of_element_located(element_locator)
            )
            self.web_driver.execute_script(
                "arguments[0].scrollIntoView(true);",
                target_element
            )
        except Exception as exception:
            traceback.print_exc()
            raise Exception(f"Failed to scroll to element {element_locator}: {exception}")

    def click_element_using_javascript(self, element_locator):
        """
        Method Name   : click_element_using_javascript
        Author        : Parth
        Description   : Clicks an element using JavaScript
        Return Type   : None
        Parameters    : element_locator(tuple)
        """
        try:
            clickable_element = self.web_driver_wait.until(
                EC.element_to_be_clickable(element_locator)
            )
            self.web_driver.execute_script("arguments[0].click();", clickable_element)
        except Exception as exception:
            traceback.print_exc()
            raise Exception(f"Failed to click element using JS {element_locator}: {exception}")

    def switch_to_window_by_index(self, window_index=-1):
        """
        Method Name   : switch_to_window_by_index
        Author        : Parth
        Description   : Switches browser control to a window using index
        Return Type   : None
        Parameters    : window_index(int)
        """
        try:
            self.web_driver.switch_to.window(self.web_driver.window_handles[window_index])
        except Exception as exception:
            traceback.print_exc()
            raise Exception(f"Failed to switch window: {exception}")

    def send_text_and_press_enter(self, element_locator, input_text):
        """
        Method Name   : send_text_and_press_enter
        Author        : Parth
        Description   : Sends text and presses ENTER key
        Return Type   : None
        Parameters    : element_locator(tuple), input_text(str)
        """
        try:
            visible_element = self.web_driver_wait.until(
                EC.visibility_of_element_located(element_locator)
            )
            self.retry_on_stale_send_keys(visible_element, input_text)
            visible_element.send_keys(Keys.ENTER)
        except Exception as exception:
            traceback.print_exc()
            raise Exception(f"Failed to send text and press ENTER: {exception}")

    # -------------------------------------------------------------------------
    # Verification Methods
    # -------------------------------------------------------------------------

    def verify_text_contains(self, element_locator, expected_text):
        """
        Method Name   : verify_text_contains
        Author        : Parth
        Description   : Verifies expected text is present in element text
        Return Type   : None
        Parameters    : element_locator(tuple), expected_text(str)
        """
        try:
            element = self.web_driver.find_element(*element_locator)
            actual_text = self.retry_on_stale_get_text(element)
            assert expected_text in actual_text, (
                f"Expected '{expected_text}' to be in '{actual_text}'"
            )
        except Exception as exception:
            traceback.print_exc()
            raise Exception(f"Text verification failed: {exception}")

    def verify_current_url_contains(self, expected_url_part):
        """
        Method Name   : verify_current_url_contains
        Author        : Parth
        Description   : Verifies expected value is present in current URL
        Return Type   : None
        Parameters    : expected_url_part(str)
        """
        try:
            current_url = self.web_driver.current_url
            assert expected_url_part in current_url, (
                f"Expected '{expected_url_part}' to be in '{current_url}'"
            )
        except Exception as exception:
            traceback.print_exc()
            raise Exception(f"URL verification failed: {exception}")

    def verify_page_title_contains(self, expected_title):
        """
        Method Name   : verify_page_title_contains
        Author        : Parth
        Description   : Verifies expected value is present in page title
        Return Type   : None
        Parameters    : expected_title(str)
        """
        try:
            actual_title = self.web_driver.title
            assert expected_title in actual_title, (
                f"Expected '{expected_title}' to be in '{actual_title}'"
            )
        except Exception as exception:
            traceback.print_exc()
            raise Exception(f"Title verification failed: {exception}")

    def is_element_visible(self, element_locator):
        """
        Method Name   : is_element_visible
        Author        : Parth
        Description   : Checks whether an element is visible
        Return Type   : bool
        Parameters    : element_locator(tuple)
        """
        try:
            self.web_driver_wait.until(EC.visibility_of_element_located(element_locator))
            return True
        except TimeoutException:
            return False

    def verify_attribute_contains(self, element_locator, attribute_name, expected_value):
        """
        Method Name   : verify_attribute_contains
        Author        : Parth
        Description   : Verifies expected value is present in element attribute
        Return Type   : None
        Parameters    : element_locator(tuple), attribute_name(str), expected_value(str)
        """
        try:
            actual_value = self.web_driver.find_element(*element_locator).get_attribute(attribute_name)
            assert expected_value in str(actual_value), (
                f"Expected '{expected_value}' to be in '{actual_value}'"
            )
        except Exception as exception:
            traceback.print_exc()
            raise Exception(f"Attribute verification failed: {exception}")

    def is_footer_visible_by_tag_name(self, tag_name, timeout=4):
        """
        Method Name   : is_footer_visible_by_tag_name
        Author        : Parth
        Description   : Checks whether a footer element is visible on the page using its HTML tag name
        Return Type   : bool
        Parameters    : tag_name(str), timeout(int)
        """
        try:
            explicit_wait = WebDriverWait(self.web_driver, timeout)
            footer_element = explicit_wait.until(
                EC.visibility_of_element_located((By.TAG_NAME, tag_name))
            )
            return footer_element.is_displayed()
        except TimeoutException:
            return False
        except Exception as exception:
            raise Exception(f"Error while checking footer visibility by tag '{tag_name}': {exception}")

    # -------------------------------------------------------------------------
    # Navigation / Utility Methods
    # -------------------------------------------------------------------------

    def navigate_back(self):
        """
        Method Name   : navigate_back
        Author        : Parth
        Description   : Navigates the browser to the previous page
        Return Type   : None
        Parameters    : None
        """
        try:
            self.web_driver.back()
        except Exception as exception:
            raise Exception(f"Error while navigating back in browser: {exception}")

    def close_current_window(self):
        """
        Method Name   : close_current_window
        Author        : Parth
        Description   : Closes the currently active browser window
        Return Type   : None
        Parameters    : None
        """
        try:
            self.web_driver.close()
        except Exception as exception:
            raise Exception(f"Error while closing browser window: {exception}")

    def wait_for_element_visibility(self, element_locator):
        """
        Method Name   : wait_for_element_visibility
        Author        : Parth
        Description   : Waits until an element is visible on the page
        Return Type   : None
        Parameters    : element_locator(tuple)
        """
        try:
            self.web_driver_wait.until(EC.visibility_of_element_located(element_locator))
        except Exception as exception:
            raise Exception(f"Element not visible: {element_locator} - {exception}")