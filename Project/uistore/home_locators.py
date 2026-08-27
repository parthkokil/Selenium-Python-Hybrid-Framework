from selenium.webdriver.common.by import By


class HomeLocators:
    """
    Page object locators for the ELC Home page.
    Centralized repository for all home page element selectors.
    """

    # ---------- Links ----------
    shop_by_age_link = (By.XPATH, "//a[text()='Shop by age']")
    newborn_gifts_link = (By.XPATH, "//a[@title='Newborn Gifts']")
    type_of_toy_link = (By.XPATH, "//a[@title='Type of toy']")
    soft_toys_link = (By.XPATH, "//a[@title='Soft Toys']")
    outdoor_toys_link = (By.XPATH, "//a[@title='Outdoor Toys']")
    bikes_link = (By.XPATH, "//a[@title='Bikes']")
    learning_skills_link = (By.XPATH, "//a[text()='Learning Skills']")
    creativity_link = (By.XPATH, "//a[contains(@title,'Creativity')]")
    brands_navigation_link = (By.XPATH, "//a[normalize-space()='Brands']")
    explore_navigation_link = (By.CSS_SELECTOR, "a[title*='Explore']")
    gift_cards_navigation_link = (By.XPATH, "//a[contains(@href, 'gift-cards')]")
    paw_patrol_brand_link = (By.XPATH, "//a[@title='Paw Patrol']")
    about_us_link = (By.XPATH, "(//a[@title='About us'])[last()]")
    footer_contact_us_link = (By.XPATH, "//ul[@id='footerNavList0']/li/a[text()='Contact Us']")

    # ---------- Buttons ----------
    pop_up_button = (By.ID, "onetrust-accept-btn-handler")
    # search_icon_button = (By.CSS_SELECTOR, "button[class*='S']")
    search_icon_button = (By.CSS_SELECTOR, "button.js_search_button")

    # ---------- Images ----------
    elc_logo = (By.XPATH, "//img[@alt='Early Learning Centre']")

    # ---------- Containers / Divs ----------
    footer_top = (By.CSS_SELECTOR, "div.footer__top")

    # ---------- Input Fields ----------
    search_input_field = (By.CSS_SELECTOR, "input[class*='aa']")