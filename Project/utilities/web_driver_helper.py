import traceback
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (WebDriverException,TimeoutException)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebDriverHelper:
    """
    Class Name    : WebDriverHelper
    Author        : Parth
    Description   : Provides reusable Selenium WebDriver actions, waits, and verification utilities
    Return Type   : Object
    Parameters    : web_driver(object), timeout(int)
    """

    def __init__(self, web_driver, timeout=10):
        # Store WebDriver instance
        self.web_driver = web_driver

        # Initialize explicit wait
        self.web_driver_wait = WebDriverWait(self.web_driver, timeout)

    """
    Method Name   : click_element
    Author        : Parth
    Description   : Clicks on an element after it becomes clickable
    Return Type   : None
    Parameters    : element_locator(tuple)
    """

    def click_element(self, element_locator):
        try:
            clickable_element = self.web_driver_wait.until(EC.element_to_be_clickable(element_locator))
            clickable_element.click()
        except WebDriverException as exception:
            traceback.print_exc()
            raise Exception(f"Failed to click element {element_locator}: {exception}")

    """
    Method Name   : enter_text
    Author        : Parth
    Description   : Sends text to a visible input field
    Return Type   : None
    Parameters    : element_locator(tuple), input_text(str)
    """

    def enter_text(self, element_locator, input_text):
        try:
            visible_element = self.web_driver_wait.until(EC.visibility_of_element_located(element_locator))
            visible_element.send_keys(input_text)
        except WebDriverException as exception:
            traceback.print_exc()
            raise Exception(f"Failed to enter text in {element_locator}: {exception}")

    """
    Method Name   : hover_over_element
    Author        : Parth
    Description   : Performs mouse hover over an element
    Return Type   : None
    Parameters    : element_locator(tuple)
    """

    def hover_over_element(self, element_locator):
        try:
            target_element = self.web_driver_wait.until(EC.visibility_of_element_located(element_locator))
            ActionChains(self.web_driver).move_to_element(target_element).perform()
        except WebDriverException as exception:
            traceback.print_exc()
            raise Exception(f"Failed to hover over element {element_locator}: {exception}")

    """
    Method Name   : scroll_to_element_using_javascript
    Author        : Parth
    Description   : Scrolls the page until the element is visible
    Return Type   : None
    Parameters    : element_locator(tuple)
    """

    def scroll_to_element_using_javascript(self, element_locator):
        try:
            target_element = self.web_driver_wait.until(EC.visibility_of_element_located(element_locator))
            self.web_driver.execute_script("arguments[0].scrollIntoView(true);",target_element)
        except Exception as exception:
            traceback.print_exc()
            raise Exception(f"Failed to scroll to element {element_locator}: {exception}")

    """
    Method Name   : click_element_using_javascript
    Author        : Parth
    Description   : Clicks an element using JavaScript
    Return Type   : None
    Parameters    : element_locator(tuple)
    """

    def click_element_using_javascript(self, element_locator):
        try:
            clickable_element = self.web_driver_wait.until(EC.element_to_be_clickable(element_locator))
            self.web_driver.execute_script("arguments[0].click();",clickable_element)
        except Exception as exception:
            traceback.print_exc()
            raise Exception(f"Failed to click element using JS {element_locator}: {exception}")

    """
    Method Name   : switch_to_window_by_index
    Author        : Parth
    Description   : Switches browser control to a window using index
    Return Type   : None
    Parameters    : window_index(int)
    """

    def switch_to_window_by_index(self, window_index=-1):
        try:
            self.web_driver.switch_to.window(self.web_driver.window_handles[window_index])
        except Exception as exception:
            traceback.print_exc()
            raise Exception(f"Failed to switch window: {exception}")

    """
    Method Name   : send_text_and_press_enter
    Author        : Parth
    Description   : Sends text and presses ENTER key
    Return Type   : None
    Parameters    : element_locator(tuple), input_text(str)
    """

    def send_text_and_press_enter(self, element_locator, input_text):
        try:
            visible_element = self.web_driver_wait.until(EC.visibility_of_element_located(element_locator))
            visible_element.send_keys(input_text)
            visible_element.send_keys(Keys.ENTER)
        except Exception as exception:
            traceback.print_exc()
            raise Exception(f"Failed to send text and press ENTER: {exception}")

    # ---------- Verification Methods ----------

    """
    Method Name   : verify_text_contains
    Author        : Parth
    Description   : Verifies expected text is present in element text
    Return Type   : None
    Parameters    : element_locator(tuple), expected_text(str)
    """

    def verify_text_contains(self, element_locator, expected_text):
        try:
            actual_text = self.web_driver.find_element(*element_locator).text
            assert expected_text in actual_text
        except Exception as exception:
            traceback.print_exc()
            raise Exception(f"Text verification failed: {exception}")

    """
    Method Name   : verify_current_url_contains
    Author        : Parth
    Description   : Verifies expected value is present in current URL
    Return Type   : None
    Parameters    : expected_url_part(str)
    """

    def verify_current_url_contains(self, expected_url_part):
        try:
            current_url = self.web_driver.current_url
            assert expected_url_part in current_url
        except Exception as exception:
            traceback.print_exc()
            raise Exception(f"URL verification failed: {exception}")

    """
    Method Name   : verify_page_title_contains
    Author        : Parth
    Description   : Verifies expected value is present in page title
    Return Type   : None
    Parameters    : expected_title(str)
    """

    def verify_page_title_contains(self, expected_title):
        try:
            assert expected_title in self.web_driver.title
        except Exception as exception:
            traceback.print_exc()
            raise Exception(f"Title verification failed: {exception}")

    """
    Method Name   : is_element_visible
    Author        : Parth
    Description   : Checks whether an element is visible
    Return Type   : bool
    Parameters    : element_locator(tuple)
    """

    def is_element_visible(self, element_locator):
        try:
            self.web_driver_wait.until(EC.visibility_of_element_located(element_locator))
            return True
        except TimeoutException:
            return False

    """
    Method Name   : verify_attribute_contains
    Author        : Parth
    Description   : Verifies expected value is present in element attribute
    Return Type   : None
    Parameters    : element_locator(tuple), attribute_name(str), expected_value(str)
    """

    def verify_attribute_contains(self,element_locator,attribute_name,expected_value):
        try:
            actual_value = self.web_driver.find_element(*element_locator).get_attribute(attribute_name)
            assert expected_value in str(actual_value)
        except Exception as exception:
            traceback.print_exc()
            raise Exception(f"Attribute verification failed: {exception}")

    """
    Method Name   : is_footer_visible_by_tag_name
    Author        : Parth
    Description   : Checks whether a footer element is visible on the page using its HTML tag name within the given timeout
    Return Type   : bool
    Parameters    : web_driver(object), tag_name(str), timeout(int)
    """

    def is_footer_visible_by_tag_name(self, web_driver, tag_name, timeout=1):
        try:
            # Initialize explicit wait with provided timeout
            explicit_wait = WebDriverWait(web_driver, timeout)

            # Wait until the footer element with given tag name is visible
            footer_element = explicit_wait.until(EC.visibility_of_element_located((By.TAG_NAME, tag_name)))

            # Return visibility status of the footer element
            return footer_element.is_displayed()

        except TimeoutException:
            # Footer element did not become visible within timeout
            return False

        except Exception as exception:
            # Raise exception for any unexpected failure
            raise Exception(f"Error while checking footer visibility by tag "f"'{tag_name}': {exception}")

    """
    Method Name   : navigate_back
    Author        : Parth
    Description   : Navigates the browser to the previous page
    Return Type   : None
    Parameters    : None
    """

    def navigate_back(self):
        try:
            self.web_driver.back()
        except Exception as exception:
            raise Exception(f"Error while navigating back in browser: {exception}")

    """
    Method Name   : close_current_window
    Author        : Parth
    Description   : Closes the currently active browser window
    Return Type   : None
    Parameters    : None
    """

    def close_current_window(self):
        try:
            self.web_driver.close()
        except Exception as exception:
            raise Exception(f"Error while closing browser window: {exception}")


    """
    Method Name   : wait_for_element_visibility
    Author        : Parth
    Description   : Waits until an element is visible on the page
    Return Type   : None
    Parameters    : element_locator(tuple)
    """

    def wait_for_element_visibility(self, element_locator):
        try:
            self.web_driver_wait.until(
                EC.visibility_of_element_located(element_locator)
            )
        except Exception as exception:
            raise Exception(
                f"Element not visible: {element_locator} - {exception}"
            )

