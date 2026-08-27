"""
base.py
--------
Base test class for the Hybrid Selenium Framework.
Provides a reusable WebDriver setup using a LOCAL Chrome browser.
All test classes should inherit from BaseTest.
"""

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.events import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager

from utilities.eventhandler import EventHandler


class BaseTest(unittest.TestCase):
    """Base class for all test cases — handles WebDriver initialization."""

    def setUpDriver(self):
        """
        Initialize and return an EventFiringWebDriver wrapped around
        a LOCAL Chrome browser instance.
        """
        # Custom event listener for logging Selenium events
        event_handler = EventHandler()

        # Chrome browser options
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        # Uncomment the next line if you want headless execution
        # options.add_argument("--headless=new")

        # Auto-download & manage the correct ChromeDriver for your Chrome version
        service = Service(ChromeDriverManager().install())

        # Launch LOCAL Chrome (no Selenium Grid needed)
        driver = webdriver.Chrome(service=service, options=options)

        # Wrap driver with event listener for custom logging/screenshots
        event_driver = EventFiringWebDriver(driver, event_handler)
        return event_driver