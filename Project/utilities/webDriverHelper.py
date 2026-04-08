import traceback
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class WebDriverHelper:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    # def open_page(self, url):
    #     try:
    #         self.driver.get(url)
    #     except WebDriverException as e:
    #         traceback.print_exc()
    #         raise Exception("Error in open_page: " + str(e))

    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except WebDriverException as e:
            traceback.print_exc()
            raise Exception("Error in click: " + str(e))

    def send_keys(self, locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.send_keys(text)
        except WebDriverException as e:
            traceback.print_exc()
            raise Exception("Error in send_keys: " + str(e))

    def hover(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            ActionChains(self.driver).move_to_element(element).perform()
        except WebDriverException as e:
            traceback.print_exc()
            raise Exception("Error in hover: " + str(e))

    # def hover_two_elements(self, first_locator, second_locator):
    #     try:
    #         first = self.wait.until(EC.visibility_of_element_located(first_locator))
    #         second = self.wait.until(EC.visibility_of_element_located(second_locator))
    #         ActionChains(self.driver).move_to_element(first).move_to_element(second).perform()
    #     except WebDriverException as e:
    #         traceback.print_exc()
    #         raise Exception("Error in hover_two_elements: " + str(e))

    def js_scroll(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        except Exception as e:
            print(f"An error occurred in js_scroll: {e}")

    def js_click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            print(f"An error occurred in js_click: {e}")

    def switch_to_new_window(self, index):
        try:
            self.driver.switch_to.window(self.driver.window_handles[index])
        except Exception as e:
            print(f"An error occurred in switch_to_new_window: {e}")

    # def switch_to_frame(self, locator):
    #     try:
    #         element = self.wait.until(EC.visibility_of_element_located(locator))
    #         self.driver.switch_to.frame(element)
    #     except Exception as e:
    #         print(f"An error occurred in switch_to_frame: {e}")

    def send_keys_enter(self, locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.send_keys(text)
            element.send_keys(Keys.ENTER)
        except Exception as e:
            print(f"An error occurred in send_keys_enter: {e}")

    # def hover_and_click(self, hover_locator, click_locator):
    #     try:
    #         hover_element = self.wait.until(EC.visibility_of_element_located(hover_locator))
    #         ActionChains(self.driver).move_to_element(hover_element).perform()
    #         click_element = self.wait.until(EC.element_to_be_clickable(click_locator))
    #         click_element.click()
    #     except Exception as e:
    #         print(f"An error occurred in hover_and_click: {e}")

    # def hover_two_and_click(self, first_locator, second_locator, click_locator):
    #     try:
    #         first = self.wait.until(EC.visibility_of_element_located(first_locator))
    #         second = self.wait.until(EC.visibility_of_element_located(second_locator))
    #         ActionChains(self.driver).move_to_element(first).move_to_element(second).perform()
    #         third = self.wait.until(EC.element_to_be_clickable(click_locator))
    #         third.click()
    #     except Exception as e:
    #         print(f"An error occurred in hover_two_and_click: {e}")

    # ---------- Utility / Verification Methods ----------

    def get_elements_by_xpath(self, value):
        return self.driver.find_elements(By.XPATH, value)

    def verify_text(self, locator, expected):
        actual = self.driver.find_element(*locator).text
        assert expected in actual

    def verify_url(self, expected):
        actual=self.driver.current_url
        assert expected in actual

    def verify_title(self, expected):
        assert expected in self.driver.title

    def switch_window(self, index=None):
        try:
            if index is None:
                index = -1
            self.driver.switch_to.window(self.driver.window_handles[index])
        except Exception as e:
            print(f"An error occurred in switch_window: {e}")

    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    # Inside your WebDriverHelper class
    def is_footer_visible_by_tag(self, driver, tag_name, timeout=1):
        """
        Waits up to 'timeout' seconds for the tag to be visible.
        """
        try:
            # wait.until returns the element once it is visible on the DOM
            wait = WebDriverWait(driver, timeout)
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, tag_name)))
            return footer.is_displayed()
        except TimeoutException:
            # If the timeout is reached, it means the footer didn't appear
            return False

    def verify_attribute(self, locator, attr_name, expected):
        actual = self.driver.find_element(*locator).get_attribute(attr_name)
        assert expected in str(actual)