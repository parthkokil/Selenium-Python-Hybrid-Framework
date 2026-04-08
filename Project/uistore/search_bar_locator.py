from selenium.webdriver.common.by import By


class SearchBarLocators:
    
    ACCEPT_COOKIES_BUTTON = (By.ID, "onetrust-accept-btn-handler")
    ELC_LOGO_IMAGE = (By.XPATH, "//img[@alt='Early Learning Centre']")

    SEARCH_SUBMIT_BUTTON = (By.XPATH, "//button[@Class='aa-SubmitButton btn btn-link js_search_button']")
    SEARCH_INPUT_FIELD = (By.XPATH, "//input[contains(@id,'put')]")

    SHOW_MORE_BUTTON = (By.XPATH, "//button[text()='Show more']")
    JIGSAW_PUZZLES_FILTER = (By.XPATH, "//span[contains(text(),'Jigsaw')]")
    CHILDREN_GAMES_FILTER = (By.XPATH, "//span[contains(text(),'Children')]")
    DISCOVER_WORLD_FILTER = (By.XPATH, "//span[contains(text(),'Discover')]")

    FIRST_PRODUCT_LINK = (By.XPATH, "//a[@class='thumb clickedObjectIDsAfterSearch']")
    ADD_TO_WISHLIST_BUTTON = (By.XPATH, "//span[text()='Add To Wishlist']")
    LEARNING_DESCRIPTOR_TEXT = (By.XPATH, "//span[@class='learningSkills__descriptor']")