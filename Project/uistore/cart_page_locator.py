from selenium.webdriver.common.by import By


class CartPageLocator:
    """
    Locator class for Cart page
    Author: Saptarshi
    """

    continue_button = (By.XPATH, "//button[@data-testid='cart-continue-shopping-button']")
    pop_up = (By.XPATH, "//div[@class='dy-lb-close dy-close-btn']")