from selenium.webdriver.common.by import By

class FirstProductPageLocators:

    # Common Locators
    # add_to_basket = (By.XPATH, "//span[text()='Add to Basket']")
    # continue_shopping_link = (By.XPATH, "//a[contains(@class,'ef')]")
    # home = (By.ID, "labelHomeDeliverySelected")

    # # Test Case 2
    # home_delivery = (By.ID, "labelHomeDeliverySelected")

    # TestCase 3
    # quantity_value = (By.ID, "qty")
    # check_out_link = (By.XPATH, "//a[contains(@class,'tn-pr')]")

    # TestCase 4
    # continue_shopping_button = (By.XPATH, "//button[@data-testid='cart-continue-shopping-button']")
    # pop_up_button = (By.XPATH, "//div[@class='dy-lb-close dy-close-btn']")

    # TestCase 5
    # ---------- Common / Generic Checkout Locators ----------
    # product_availability_in_store_text = (By.ID,"js-store-availability-text")
    # add_to_basket_button = (By.XPATH,"//span[normalize-space()='Add to Basket']")
    # checkout_button = (By.XPATH,"//a[contains(@class, 'tn-pr')]")

    # TestCase 6
    # ---------- Doll Product Page Locators ----------
    # doll_add_to_basket_button = (By.ID,"addToCartButton")
    # doll_checkout_button = (By.XPATH,"//div[@id='addToCartLayer']/div/div/a[@href='/cart']")

    # basket_page_label_text = (By.XPATH,"//div[normalize-space()='My Basket']")
    # close_dynamic_popup_button = (By.XPATH,"//div[@Class='dy-lb-close dy-close-btn']")
    # ---------- Order Summary Locators ----------
    # order_total_text = (By.XPATH,"//div[normalize-space()='Order Total']")

    # TestCase 7
    # add_to_wishlist_button = (By.ID, "addToCartButton")
    # learning_description_text = (By.XPATH, "//span[@class='learningSkills__descriptor']")

    # TestCase 8
    # product_heading_text = (By.XPATH, "//div[@class='name']/h1")


    #links
    continue_shopping_link = (By.XPATH, "//a[contains(@class,'ef')]")
    check_out_link = (By.XPATH, "//a[contains(@class,'tn-pr')]")
    checkout_button = (By.XPATH,"//a[contains(@class, 'tn-pr')]")

    #buttons
    add_to_basket = (By.XPATH, "//span[text()='Add to Basket']")
    continue_shopping_button = (By.XPATH, "//button[@data-testid='cart-continue-shopping-button']")
    pop_up_button = (By.XPATH, "//div[@class='dy-lb-close dy-close-btn']")
    add_to_basket_button = (By.XPATH,"//span[normalize-space()='Add to Basket']")
    checkout_button = (By.XPATH,"//a[contains(@class, 'tn-pr')]")
    doll_add_to_basket_button = (By.ID,"addToCartButton")
    doll_checkout_button = (By.XPATH,"//div[@id='addToCartLayer']/div/div/a[@href='/cart']")
    close_dynamic_popup_button = (By.XPATH,"//div[@Class='dy-lb-close dy-close-btn']")
    add_to_wishlist_button = (By.ID, "addToCartButton")
    home_delivery_radio_button = (By.ID, "labelHomeDeliverySelected")
    basket_page_label_text = (By.XPATH,"//div[normalize-space()='My Basket']")

    #input fields
    quantity_input_field = (By.ID, "qty")

    # texts/description locators
    product_availability_in_store_text = (By.ID,"js-store-availability-text")
    learning_description_text = (By.XPATH, "//span[@class='learningSkills__descriptor']")
    product_heading_text = (By.XPATH, "//div[@class='name']/h1")
    order_total_text = (By.XPATH,"//div[normalize-space()='Order Total']")





