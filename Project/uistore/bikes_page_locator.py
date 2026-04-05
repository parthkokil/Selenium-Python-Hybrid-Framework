from selenium.webdriver.common.by import By


class BikesPageLocator:
    """
    Locator class for Bikes page
    Author: Saptarshi
    """

    Toddler_bikes = (By.XPATH, "//h1[text()='Toddler Bikes']")
    price = (By.XPATH, "//div[contains(text(),'Price')]")
    show_more_option = (By.XPATH, "(//button[text()='Show more'])[2]")
    huffy = (By.XPATH, "//span[text()='Huffy']")