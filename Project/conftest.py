import os
import subprocess

def pytest_sessionfinish(session, exitstatus):
    """
    Called once after ALL tests are executed
    """
    try:
        if os.path.exists("Report/Allure"):
            subprocess.run(
                ["allure", "generate", "Report/Allure", "-o", "Report/AllureReport", "--clean"],
                check=True
            )
    except Exception as e:
        print(f"Allure report generation failed: {e}")