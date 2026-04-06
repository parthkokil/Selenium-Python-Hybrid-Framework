from selenium.webdriver.common.by import By


class NewbornGiftsLocators:
    """
    Locator Class Name: NewbornGiftsLocators
    Author: Karuna Narayankar
    Description:
        Contains all locators related to the Newborn Gifts page.
    """

    ACCEPT_COOKIES_BUTTON = (By.ID, "onetrust-accept-btn-handler")

    ELC_LOGO_IMAGE = (By.XPATH, "//img[@alt='Early Learning Centre']")

    SHOP_BY_AGE_MENU = (By.XPATH, "//a[text()='Shop by age']")
    NEWBORN_GIFTS_LINK = (By.XPATH, "//a[@title='Newborn Gifts']")

    SHOW_MORE_BUTTON = (By.CSS_SELECTOR, "button[class='ais-Menu-showMore facet__more']")

    BABY_ACTIVITY_TOYS_FILTER = (By.XPATH, "//span[text()='Baby Activity Toys']")
    EARLY_LEARNING_CENTRE_FILTER = (By.CLASS_NAME, "facet__list__text")
    HAND_EYE_COORDINATION_FILTER = (By.XPATH, "//span[text()='Hand eye coordination']")

    FIRST_PRODUCT_CARD = (By.XPATH,"//a[@class='thumb clickedObjectIDsAfterSearch']")

    ADD_TO_BASKET_BUTTON = (By.ID, "addToCartButton")
    CONTINUE_SHOPPING_LINK = (By.XPATH, "//a[contains(@class,'ef')]")

    HOME_DELIVERY_RADIO = (By.ID, "labelHomeDeliverySelected")

    PAGE_HEADING_TEXT = (By.XPATH, "//h1[text()='Newborn Baby Gifts']")