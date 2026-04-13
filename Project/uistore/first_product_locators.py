from selenium.webdriver.common.by import By

class FirstProductPageLocators:

    #links
    continue_shopping_link = (By.XPATH, "//a[contains(@class,'ef')]")
    check_out_link = (By.XPATH, "//a[contains(@class,'tn-pr')]")
 
    #buttons
    add_to_basket = (By.XPATH, "//span[text()='Add to Basket']")
    continue_shopping_button = (By.XPATH, "//div[@class='col-xs-6']/a[contains(text(),'Co')]")
    pop_up_button = (By.XPATH, "//div[@class='dy-lb-close dy-close-btn']")
    add_to_basket_button = (By.XPATH,"//span[normalize-space()='Add to Basket']")
    checkout_button = (By.XPATH,"//a[contains(@class, 'tn-pr')]")
    doll_add_to_basket_button = (By.ID,"addToCartButton")
    doll_checkout_button = (By.XPATH,"//div[@id='addToCartLayer']/div/div/a[@href='/cart']")
    close_dynamic_popup_button = (By.XPATH,"//div[@Class='dy-lb-close dy-close-btn']")
    add_to_wishlist_button = (By.ID, "addToCartButton")
    learning_description_text = (By.XPATH, "//span[@class='learningSkills__descriptor']")
    product_heading_text = (By.XPATH, "//div[@class='name']/h1")