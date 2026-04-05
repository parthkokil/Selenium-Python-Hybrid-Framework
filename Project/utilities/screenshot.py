import os
from datetime import datetime
from utilities.config_reader import ConfigReader


class Screenshot:
    """
    Screenshot utility to capture browser screenshots
    Author Name : Ashutosh
    """

    @staticmethod
    def capture_screenshot(driver, name):
        try:
            config = ConfigReader()
            relative_path = config.get_data("PATH", "screenshot_path")

            project_root = os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            )

            screenshot_dir = os.path.join(project_root, relative_path)
            os.makedirs(screenshot_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
            file_name = f"{name}_{timestamp}.png"
            file_path = os.path.join(screenshot_dir, file_name)

            driver.save_screenshot(file_path)
            return file_path

        except Exception as e:
            raise Exception(
                f"Failed to capture screenshot '{name}': {e}"
            )