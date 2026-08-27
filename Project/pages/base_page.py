from utilities.web_driver_helper import WebDriverHelper
from utilities.screenshot import Screenshot
from utilities.excel_reader import ExcelReader
from time import sleep

class BasePage:
    """
    # Class Name    : BasePage
    # Author        : Parth
    # Description   : The ultimate parent class for all Page Objects.
    #                 Contains the match-case dispatcher (Keyword-Driven Approach).
    #                 Provides a unified interface for ALL interactions across the framework.
    # Return Type   : Object
    """
    def __init__(self, driver, logger):
        """
        Method Name   : __init__
        Description   : Initializes the BasePage with WebDriver and logger.
        """
        self.web_driver = driver
        self.logger = logger
        self.web_driver_helper = WebDriverHelper(self.web_driver)
        self.excel_reader = ExcelReader()

    def perform_action(self, action_type, locator=None, element_name=None, expected_text=None, **kwargs):
        """
        Method Name   : perform_action
        Description   : Centralized dispatch method using Python match-case (switch-case).
                        Replaces all separate click/hover/verify functions across all pages.
        Parameters    : action_type(str)  - The type of action (e.g., "CLICK", "HOVER", "VERIFY_TEXT")
                        locator(tuple)    - Selenium locator (e.g., By.CSS_SELECTOR, ".class")
                        element_name(str) - Human-readable name for dynamic logging and screenshots
                        expected_text(str)- Text for verifications or inputs
        Return Type   : None
        """
        try:
            match str(action_type).upper():
                
                # click action 
                case "CLICK":
                    if locator:
                        self.web_driver_helper.wait_for_element_visibility(locator)
                        self.web_driver_helper.click_element(locator)
                        self.logger.info(f"Clicked on '{element_name}' successfully")
                    else:
                        raise ValueError(f"Locator missing for action: {action_type}")

                # hover action
                case "HOVER":
                    if locator:
                        self.web_driver_helper.wait_for_element_visibility(locator)
                        self.web_driver_helper.hover_over_element(locator)
                        self.logger.info(f"Hovered on '{element_name}' successfully")
                    else:
                        raise ValueError(f"Locator missing for action: {action_type}")

                # scroll and click action
                case "SCROLL_AND_CLICK":
                    if locator:
                        self.web_driver_helper.wait_for_element_visibility(locator)
                        self.web_driver_helper.scroll_to_element_using_javascript(locator)
                        self.logger.info(f"Scrolled to '{element_name}'")
                        
                        click_flag = kwargs.get("click", True)
                        if click_flag:
                            self.web_driver_helper.click_element(locator)
                            self.logger.info(f"Clicked on '{element_name}' successfully")
                    else:
                        raise ValueError(f"Locator missing for action: {action_type}")

                # search action - types text and submits via JS form submit
                case "SEARCH_AND_SUBMIT":
                    if locator and expected_text:
                        # Wait for search field to be visible before interacting
                        self.web_driver_helper.wait_for_element_visibility(locator)
                        self.web_driver_helper.click_element(locator)
                        self.web_driver_helper.enter_text(locator, expected_text)

                        # Submit the search — use icon click OR fallback to JS form submit
                        search_icon = kwargs.get("search_icon_locator")
                        if search_icon:
                            sleep(1)  # Let autocomplete render
                            self.web_driver_helper.click_element_using_javascript(search_icon)
                        else:
                            # Fallback: submit form directly via JavaScript
                            self.web_driver.execute_script(
                                "document.querySelector('form[role=\"search\"]').submit();"
                            )

                        self.logger.info(f"Searched for '{expected_text}' successfully")
                    else:
                        raise ValueError(f"Locator or text missing for action: {action_type}")

                # verify_url action
                case "VERIFY_URL":
                    if expected_text:
                        self.web_driver_helper.verify_current_url_contains(expected_text)
                        self.logger.info(f"Verified URL contains '{expected_text}' for {element_name}")
                    else:
                        raise ValueError(f"Expected text missing for action: {action_type}")

                # verify_element_visible
                case "VERIFY_VISIBLE":
                    if locator:
                        assert self.web_driver_helper.is_element_visible(locator)
                        self.logger.info(f"Verified '{element_name}' is visible successfully")
                        Screenshot.capture_browser_screenshot(self.web_driver, f"{element_name.replace(' ', '_').lower()}_verified")
                    else:
                        raise ValueError(f"Locator missing for action: {action_type}")

                # verify_text
                case "VERIFY_TEXT":
                    if locator and expected_text:
                        self.web_driver_helper.wait_for_element_visibility(locator)
                        self.web_driver_helper.verify_text_contains(locator, expected_text)
                        self.logger.info(f"Verified '{element_name}' contains text '{expected_text}' successfully")
                        
                        capture = kwargs.get("capture_screenshot", False)
                        if capture:
                            Screenshot.capture_browser_screenshot(self.web_driver, f"{element_name.replace(' ', '_').lower()}_verified")
                    else:
                        raise ValueError(f"Locator or expected text missing for action: {action_type}")

                # verify_attribute
                case "VERIFY_ATTRIBUTE":
                    attribute_name = kwargs.get("attribute_name")
                    if locator and attribute_name and expected_text:
                        self.web_driver_helper.verify_attribute_contains(locator, attribute_name, expected_text)
                        self.logger.info(f"Verified '{element_name}' attribute '{attribute_name}' contains '{expected_text}'")
                    else:
                        raise ValueError(f"Missing parameters for action: {action_type}")

                # close popup method
                case "CLOSE_POPUP":
                    if locator:
                        self.web_driver_helper.wait_for_element_visibility(locator)
                        self.web_driver_helper.click_element(locator)
                        self.logger.info(f"Closed popup '{element_name}' successfully")
                    else:
                        raise ValueError(f"Locator missing for action: {action_type}")
                
                # defaul case
                case _:
                    self.logger.error(f"Invalid action type passed: {action_type}")
                    raise ValueError(f"Action '{action_type}' is not supported by the framework.")
                
        except Exception as e:
            # Dynamic screenshot naming based on action and element name
            err_name = element_name.replace(' ', '_').lower() if element_name else "unknown_element"
            Screenshot.capture_browser_screenshot(
                self.web_driver, f"{action_type.lower()}_{err_name}_error"
            )
            self.logger.error(f"Failed to perform {action_type} on '{element_name}': {e}")
            raise
