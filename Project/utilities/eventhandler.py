import os
import logging

from selenium.webdriver.support.abstract_event_listener import AbstractEventListener

class EventHandler(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print("Before navigating to:", url)

    def after_navigate_to(self, url, driver):
        print("After navigating to:", url)

    # Implement other methods as needed
