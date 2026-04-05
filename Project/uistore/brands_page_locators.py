from selenium.webdriver.common.by import By


class BrandsPageLocators:
    """Locators for Test Case 5 pages/flows.
        Author:Gitika
    """

    ELC_LOGO_IMAGE = (By.XPATH, "//img[@title='Early Learning Centre']")
    BRANDS_LINK = (By.XPATH, "//a[text()='Brands']")
    PAW_PATROL_LINK = (By.XPATH, "//a[@title='Paw Patrol']")
    PLAYSETS_FILTER = (By.XPATH, "//span[text()='Playsets']")
    SAVINGS_FILTER = (By.XPATH, "//span[text()='Savings']")

    FIRST_PRODUCT_THUMBNAIL = (By.CSS_SELECTOR, "a[class='thumb clickedObjectIDsAfterSearch']")
    STORE_AVAILABILITY_TEXT = (By.ID, "js-store-availability-text")

    ADD_TO_BASKET_BUTTON = (By.XPATH, "//span[text()='Add to Basket']")
    CHECK_OUT_BUTTON = (By.XPATH, "//a[contains(@class,'tn-pr')]")
    BASKET_LABEL = (By.XPATH, "//div[text()='My Basket']")

    ACCEPT_ALL_COOKIES_BUTTON = (By.XPATH, "//button[text()='Accept All Cookies']")
    # Kept as-is (even if not used now) — since you said do not change logic.
    CLOSE_DYNAMIC_POPUP_BUTTON = (By.XPATH, "//div[@class='dy-lb-close dy-close-btn']")