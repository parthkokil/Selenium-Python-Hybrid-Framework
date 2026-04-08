import unittest
import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from utilities.eventhandler import EventHandler
import os

class BaseTest(unittest.TestCase):
    def setUpDriver(self):
        event_handler = EventHandler()
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        remote_url = "http://localhost:4444"
        driver = webdriver.Remote(command_executor=remote_url, options=options)

        event_driver = EventFiringWebDriver(driver, event_handler)
        return event_driver

    if __name__ == '__main__':
        exit_code = pytest.main(['-v', '--alluredir=Report/Allure'])