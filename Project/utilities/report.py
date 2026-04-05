import os
from datetime import datetime
from time import sleep
from configparser import ConfigParser


class AllureReporter:
    """
    Generates Allure HTML reports using project-local Allure CLI
    Author:Karuna Narayankar
    """

    def __init__(self):
        sleep(2)

        #  Resolve project root (Second/)
        project_root = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")
        )

        #  Read config.properties
        config = ConfigParser()
        config_path = os.path.join(project_root, "config", "config.properties")
        config.read(config_path)

        #  Read PATH values
        base_dir_rel = config.get("PATH", "base_dir")
        result_dir_rel = config.get("PATH", "result_directory")
        report_dir_rel = config.get("PATH", "report_directory")

        self.base_dir = os.path.join(project_root, base_dir_rel)
        self.result_dir = os.path.join(project_root, result_dir_rel)
        self.report_dir = os.path.join(project_root, report_dir_rel)

        os.makedirs(self.base_dir, exist_ok=True)
        os.makedirs(self.result_dir, exist_ok=True)
        os.makedirs(self.report_dir, exist_ok=True)

        #  DEFINE allure_bat HERE (THIS FIXES YOUR ERROR)
        self.allure_bat = os.path.join(
            project_root,
            "allure-2.38.1",
            "bin",
            "allure.bat"
        )

    def generate_report(self):
        sleep(2)

        timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
        output_path = os.path.join(
            self.report_dir,
            f"AllureReports_{timestamp}"
        )

        #  Windows-safe execution of .bat file
        command = (
            f'cmd /c ""{self.allure_bat}" generate "{self.result_dir}" '
            f'-o "{output_path}" --clean"'
        )

        print("Running Allure command:", command)
        os.system(command)
 