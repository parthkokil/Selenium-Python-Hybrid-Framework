import os
from datetime import datetime
from time import sleep
from configparser import ConfigParser


class AllureReporter:
    """
    Class Name    : AllureReporter
    Author        : Karuna
    Description   : Generates Allure HTML reports using Allure CLI
    Return Type   : None
    Parameters    : None
    """

    def __init__(self):
        # Small wait to ensure all result files are flushed
        sleep(2)

        # Resolve project root directory
        self.project_root = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")
        )

        # Load config.properties
        config = ConfigParser()
        config_path = os.path.join(
            self.project_root,
            "config",
            "config.properties"
        )

        if not os.path.exists(config_path):
            raise FileNotFoundError(
                f"config.properties not found at: {config_path}"
            )

        config.read(config_path)

        # Read paths from config
        self.base_dir = config.get("PATH", "base_dir")
        self.allure_results_dir = config.get("PATH", "allure_results")
        self.allure_report_dir = config.get("PATH", "allure_report")

        # Convert to absolute paths
        self.base_dir_path = os.path.join(self.project_root, self.base_dir)
        self.results_dir_path = os.path.join(self.project_root, self.allure_results_dir)
        self.report_dir_path = os.path.join(self.project_root, self.allure_report_dir)

        # Ensure required directories exist
        os.makedirs(self.base_dir_path, exist_ok=True)
        os.makedirs(self.results_dir_path, exist_ok=True)
        os.makedirs(self.report_dir_path, exist_ok=True)

    """
    Method Name   : generate_allure_report
    Author        : Parth
    Description   : Generates timestamped Allure HTML report
    Return Type   : None
    Parameters    : None
    """

    def generate_allure_report(self):
        sleep(2)

        # Timestamped report directory
        timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
        final_report_path = os.path.join(
            self.report_dir_path,
            f"AllureReport_{timestamp}"
        )

        # Allure CLI command
        allure_command = (
            f'allure generate "{self.results_dir_path}" '
            f'-o "{final_report_path}" --clean'
        )

        print("\nGenerating Allure Report...")
        print("Command:", allure_command)

        exit_code = os.system(allure_command)

        if exit_code == 0:
            print(f"\n Allure report generated successfully at:\n{final_report_path}")
        else:
            print("\n Failed to generate Allure report. Check Allure installation.")