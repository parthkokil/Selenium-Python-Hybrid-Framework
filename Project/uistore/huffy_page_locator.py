from selenium.webdriver.common.by import By


class HuffyPageLocator:
    """
    Locator class for Huffy page
    Author: Saptarshi
    """

    toddler_bikes = (By.XPATH, "//span[text()='Toddler Bikes']")
    search = (By.XPATH, "//span[text()='Search by brand']")
    disney = (By.XPATH, "(//span[@class='facet__list__label'])[5]")