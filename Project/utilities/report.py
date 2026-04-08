import os
from datetime import datetime
from time import sleep
from configparser import ConfigParser


class AllureReporter:
    """
    Class Name    : AllureReporter
    Author        : Karuna
    Description   : Utility class responsible for generating Allure HTML reports using the locally available Allure CLI
    Return Type   : Object
    Parameters    : None
    """

    def __init__(self):
        # Pause execution briefly to ensure all test results are written
        sleep(2)

        # Resolve the project root directory dynamically
        project_root_directory = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")
        )

        # Initialize ConfigParser to read config.properties
        config_parser = ConfigParser()

        # Construct absolute path of config.properties file
        config_file_path = os.path.join(
            project_root_directory,
            "config",
            "config.properties"
        )

        # Read configuration values from config.properties
        config_parser.read(config_file_path)

        # Read relative directory paths from PATH section
        base_directory_relative = config_parser.get("PATH", "base_dir")
        result_directory_relative = config_parser.get("PATH", "result_directory")
        report_directory_relative = config_parser.get("PATH", "report_directory")

        # Construct absolute paths using project root
        self.base_directory_path = os.path.join(
            project_root_directory,
            base_directory_relative
        )
        self.result_directory_path = os.path.join(
            project_root_directory,
            result_directory_relative
        )
        self.report_directory_path = os.path.join(
            project_root_directory,
            report_directory_relative
        )

        # Create required directories if they do not already exist
        os.makedirs(self.base_directory_path, exist_ok=True)
        os.makedirs(self.result_directory_path, exist_ok=True)
        os.makedirs(self.report_directory_path, exist_ok=True)

        # Define the absolute path of allure.bat executable
        self.allure_batch_file_path = os.path.join(
            project_root_directory,
            "allure-2.38.1",
            "bin",
            "allure.bat"
        )

    """
    Method Name   : generate_allure_report
    Author        : Karuna
    Description   : Generates Allure HTML report from the result directory and stores it in a timestamped report folder
    Return Type   : None
    Parameters    : None
    """

    def generate_allure_report(self):
        # Pause execution to ensure result files are stable
        sleep(2)

        # Generate timestamp for unique report folder naming
        report_timestamp = datetime.now().strftime(
            "%Y_%m_%d-%H_%M_%S"
        )

        # Construct output directory path for Allure report
        report_output_path = os.path.join(
            self.report_directory_path,
            f"AllureReports_{report_timestamp}"
        )

        # Build Windows-safe command to execute allure.bat
        allure_command = (
            f'cmd /c ""{self.allure_batch_file_path}" '
            f'generate "{self.result_directory_path}" '
            f'-o "{report_output_path}" --clean"'
        )

        # Print command for debugging and traceability
        print("Running Allure command:", allure_command)

        # Execute the Allure report generation command
        os.system(allure_command)