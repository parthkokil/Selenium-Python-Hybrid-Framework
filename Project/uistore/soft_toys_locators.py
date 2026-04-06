from selenium.webdriver.common.by import By


class SoftToysLocators:
    """
    Locator Class Name: SoftToysLocators
    Author: Karuna Narayankar
    Description:
        Contains all locators related to the Soft Toys page.
    """

    ACCEPT_COOKIES_BUTTON = (By.ID, "onetrust-accept-btn-handler")

    ELC_LOGO_IMAGE = (By.XPATH, "//img[@alt='Early Learning Centre']")
    ELC_LOGO_IMAGE_TITLE = (By.XPATH, "//img[@title='Early Learning Centre']")

    TYPE_OF_TOY_MENU = (By.XPATH, "//a[@title='Type of toy']")
    SOFT_TOYS_CATEGORY_LINK = (By.XPATH, "//a[@title='Soft Toys']")

    DOLLS_FILTER_ITEM = (By.CLASS_NAME, "facet__item")
    SOFT_TOYS_FILTER_OPTION = (By.XPATH, "//span[text()='Soft Toys']")

    BRANDS_SECTION_HEADER = (By.XPATH, "//div[text()=' Brands ']")
    STIMULATING_SENSES_FILTER = (By.XPATH, "//span[text()='Stimulating senses']")

    FIRST_PRODUCT_CARD = (
        By.XPATH, "//li[@class='ais-Hits-item product-item']"
    )

    HOME_DELIVERY_STATUS_TEXT = (
        By.XPATH, "//span[text()='Home Delivery Selected']"
    )

    ADD_TO_BASKET_BUTTON = (By.XPATH, "//span[text()='Add to Basket']")
    CONTINUE_SHOPPING_LINK = (By.XPATH, "//a[contains(@class,'ef')]")

    HOME_DELIVERY_LABEL = (By.CSS_SELECTOR, "#labelHomeDeliverySelected")

    PAGE_HEADING_TEXT = (By.XPATH, "//h1[text()='Soft Toys']")