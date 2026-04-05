from selenium.webdriver.common.by import By


class ExplorePageLocators:
    """Locators for Test Case 6 pages/flows.
    Author:Gitika
    """

    ACCEPT_ALL_COOKIES_BUTTON = (By.XPATH, "//button[text()='Accept All Cookies']")
    ELC_LOGO_IMAGE = (By.XPATH, "//img[@title='Early Learning Centre']")

    EXPLORE_LINK = (By.XPATH, "//a[text()='Explore']")
    GIFT_CARDS_LINK = (By.XPATH, "//a[contains(@href,'gift-cards')]")
    OFFERS_LINK = (By.CSS_SELECTOR, "a[title='Offers']")
    BRANDS_LINK = (By.XPATH, "//a[@title='Brands']")
    DOLLS_LINK = (By.XPATH, "//a[contains(@href,'Dolls')]")

    FIRST_PRODUCT_CARD = (By.XPATH, "(//div[@class='product-item-inner'])[1]")
    ADD_TO_BASKET_BUTTON = (By.ID, "addToCartButton")
    CHECK_OUT_BUTTON = (By.XPATH, "(//a[contains(text(),'Check out')])[2]")
    ORDER_TOTAL_TEXT = (By.XPATH, "//div[text()='Order Total']")