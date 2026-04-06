from selenium.webdriver.common.by import By


class HomePageLocator:
    """
    Locator class for Home page
    Author: Saptarshi
    """

    accept_pop_up = (By.ID, "onetrust-accept-btn-handler")
    ELC_logo = (By.XPATH, "//img[@title='Early Learning Centre']")
    outdoor_toys = (By.XPATH, "//a[@title='Outdoor Toys']")
    bikes = (By.XPATH, "//a[@title='Bikes']")
    search = (By.XPATH, "//span[text()='Search by brand']")

    learning_skills = (By.XPATH, "//a[text()='Learning Skills']")
    creativity = (By.XPATH, "//a[contains(@title,'Creativity')]")