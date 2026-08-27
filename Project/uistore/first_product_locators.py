from selenium.webdriver.common.by import By


class FirstProductPageLocators:
    """
    Page object locators for the Product Detail page.
    """

    # ---------- Links ----------
    continue_shopping_link = (By.XPATH, "//a[contains(@class,'ef')]")
    check_out_link = (By.XPATH, "//a[contains(@class,'tn-pr')]")

    # ---------- Buttons ----------
    add_to_basket = (By.XPATH, "//span[text()='Add to Basket']")
    add_to_basket_button = (By.XPATH, "//span[normalize-space()='Add to Basket']")
    continue_shopping_button = (By.XPATH, "//div[@class='col-xs-6']/a[contains(text(),'Co')]")
    # --- BACKUP (different strategy): newer site uses data-testid attribute ---
    # continue_shopping_button = (By.XPATH, "//button[@data-testid='cart-continue-shopping-button']")
    pop_up_button = (By.XPATH, "//div[@class='dy-lb-close dy-close-btn']")
    close_dynamic_popup_button = (By.XPATH, "//div[@Class='dy-lb-close dy-close-btn']")
    checkout_button = (By.XPATH, "//a[contains(@class, 'tn-pr')]")
    doll_add_to_basket_button = (By.XPATH, "//span[normalize-space()='Add to Basket']")
    doll_checkout_button = (By.XPATH, "//div[@id='addToCartLayer']/div/div/a[@href='/cart']")
    add_to_wishlist_button = (By.ID, "addToCartButton")
    home_delivery_radio_button = (By.ID, "labelHomeDeliverySelected")

    # ---------- Input Fields ----------
    quantity_input_field = (By.ID, "qty")

    # ---------- Texts / Labels ----------
    basket_page_label_text = (By.XPATH, "//div[@class='cart-subhead text-left']")
    product_availability_in_store_text = (By.ID, "js-store-availability-text")
    learning_description_text = (By.XPATH, "//span[@class='learningSkills__descriptor']")
    product_heading_text = (By.XPATH, "//div[@class='name']/h1")
    order_total_text = (By.XPATH, "//div[normalize-space()='Order Total']")