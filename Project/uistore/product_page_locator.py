from selenium.webdriver.common.by import By


class ProductPageLocator:
    """
    Locator class for Product page
    Author: Saptarshi
    """

    add_to_basket = (By.XPATH, "//span[text()='Add to Basket']")
    reviews = (By.XPATH, "//span[text()='Reviews']")
    one = (By.ID, "qty")
    check_out = (By.XPATH, "//a[contains(@class,'tn-pr')]")
    minutes = (By.XPATH, "//span[@class='bold']")