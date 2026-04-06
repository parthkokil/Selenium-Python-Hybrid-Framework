from selenium.webdriver.common.by import By


class DisneyPageLocator:
    """
    Locator class for Disney page
    Author: Saptarshi
    """

    first_product = (By.CSS_SELECTOR, "a[class='thumb clickedObjectIDsAfterSearch']")
