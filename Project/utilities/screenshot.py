import os
from datetime import datetime
from utilities.config_reader import ConfigReader


class Screenshot:
    """
    Class Name    : Screenshot
    Author        : Ashutosh
    Description   : Utility class responsible for capturing browser screenshots and storing them in a configured screenshot directory
    Return Type   : Object
    Parameters    : None
    """

    @staticmethod
    def capture_browser_screenshot(web_driver, screenshot_name):
        """
            Method Name   : capture_browser_screenshot
            Author        : Ashutosh
            Description   : Captures a screenshot of the current browser state and saves it with a timestamped file name
            Return Type   : str
            Parameters    : web_driver(object), screenshot_name(str)
        """
        try:
            # Initialize ConfigReader to fetch screenshot path
            config_reader = ConfigReader()

            # Read relative screenshot directory path from config.properties
            screenshot_directory_relative_path = config_reader.get_config_value(
                "PATH",
                "screenshot_path"
            )

            # Resolve project root directory dynamically
            project_root_directory = os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            )

            # Construct absolute screenshot directory path
            screenshot_directory_path = os.path.join(
                project_root_directory,
                screenshot_directory_relative_path
            )

            # Create screenshot directory if it does not exist
            os.makedirs(screenshot_directory_path, exist_ok=True)

            # Generate timestamp for screenshot file naming
            screenshot_timestamp = datetime.now().strftime(
                "%Y_%m_%d_%H_%M_%S"
            )

            # Construct screenshot file name
            screenshot_file_name = (
                f"{screenshot_name}_{screenshot_timestamp}.png"
            )

            # Construct full screenshot file path
            screenshot_file_absolute_path = os.path.join(screenshot_directory_path,screenshot_file_name)

            # Capture and save browser screenshot
            web_driver.save_screenshot(
                screenshot_file_absolute_path
            )

            # Return saved screenshot file path
            return screenshot_file_absolute_path

        except Exception as exception:
            # Raise meaningful exception if screenshot capture fails
            raise Exception(
                f"Failed to capture screenshot '{screenshot_name}': "
                f"{exception}"
            )