"""
conftest.py
-----------
Pytest hooks for the Hybrid Framework.
After all tests finish, automatically generate an Allure HTML report.
"""

import os
import shutil
import subprocess


def pytest_sessionfinish(session, exitstatus):
    """
    Called once after the entire test session finishes.
    Generates an Allure HTML report from the raw results in Report/Allure.
    """
    allure_results_dir = "Report/Allure"
    allure_report_dir = "Report/AllureReport"

    # Skip if no results were produced
    if not os.path.exists(allure_results_dir):
        print(f"[Allure] No results found at '{allure_results_dir}'. Skipping report generation.")
        return

    # Ensure the 'allure' CLI is available on PATH
    if shutil.which("allure") is None:
        print("[Allure] 'allure' command not found on PATH. Skipping report generation.")
        print("        Install Allure CLI: https://allurereport.org/docs/install/")
        return

    try:
        subprocess.run(
            ["allure", "generate", allure_results_dir, "-o", allure_report_dir, "--clean"],
            check=True,
            shell=True
        )
        print(f"[Allure] Report generated successfully at: {allure_report_dir}")
    except subprocess.CalledProcessError as e:
        print(f"[Allure] Report generation failed: {e}")
