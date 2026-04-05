from selenium.webdriver.common.by import By


class CarPageLocators:
    """
    Locator Class Name: CarPageLocators
    Author: Ashutosh
    Description:
        Contains all locators related to the Car page workflow.
    """

    ACCEPT_COOKIES_BUTTON = (By.ID, "onetrust-accept-btn-handler")
    ELC_LOGO_IMAGE = (By.XPATH, "//img[@alt='Early Learning Centre']")

    SEARCH_SUBMIT_BUTTON = (By.XPATH, "//button[@Class='aa-SubmitButton btn btn-link js_search_button']")
    SEARCH_INPUT_FIELD = (By.ID, "autocomplete-0-input")

    SHOW_MORE_BUTTON = (By.XPATH, "//button[@class='ais-Menu-showMore facet__more']")
    TOY_CARS_FILTER = (By.XPATH, "(//span[@class='facet__text'])[28]")

    LEARNING_SKILLS_MENU = (By.CSS_SELECTOR, "a[title='Learning Skills']")
    IMAGINATIVE_PLAY_OPTION = (By.XPATH, "//img[@alt='Learning Skills - Imaginative Play']")
    FINE_MOTOR_SKILLS_FILTER = (By.XPATH, "(//span[@class='facet__list__text'])[3]")

    FIRST_PRODUCT_LINK = (By.XPATH, "//a[@class='thumb clickedObjectIDsAfterSearch']")
    PRODUCT_HEADING_TEXT = (By.XPATH, "//div[@class='name']/h1")

    ADD_TO_WISHLIST_BUTTON = (By.XPATH, "//span[text()='Add To Wishlist']")