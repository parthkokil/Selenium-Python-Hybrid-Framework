from selenium.webdriver.common.by import By

class HomeLocators:


    # Accept all cookies locator
    pop_up = (By.ID, "onetrust-accept-btn-handler")
    elc_logo = (By.XPATH, "//img[@alt='Early Learning Centre']")


    # TestCase 1
    # newborn locators for home page
    shop_by_age=(By.XPATH,"//a[text()='Shop by age']")
    newborn_gifts = (By.XPATH, "//a[@title='Newborn Gifts']")

    # TestCase 2
    # soft toys locators for home page
    type_of_toy = (By.XPATH, "//a[@title='Type of toy']")
    soft_toys = (By.XPATH, "//a[@title='Soft Toys']")

    # TestCase 3
    outdoor_toys_text = (By.XPATH, "//a[@title='Outdoor Toys']")
    bikes_text = (By.XPATH, "//a[@title='Bikes']")

    # TestCase 4

    learning_skills_text = (By.XPATH, "//a[text()='Learning Skills']")
    creativity_text = (By.XPATH, "//a[contains(@title,'Creativity')]")

    # TestCase 7 and 8
    search_input_field = (By.CSS_SELECTOR, "input[class*='aa']")
    search_icon = (By.CSS_SELECTOR, "button[class*='S']")


    # TestCase 10 Locators for handling homepage functionalities
    # Footer anchor area to scroll into view
    footer_top = (By.CSS_SELECTOR, "div.footer__top")
    about_us = (By.XPATH, "(//a[@title='About us'])[last()]")


    # TestCase 5 and 6
    # ---------- Primary Navigation Locators ----------
    brands_navigation_link = (By.XPATH,"//a[normalize-space()='Brands']")
    explore_navigation_link = (By.CSS_SELECTOR,"a[title*='Explore']")
    gift_cards_navigation_link = (By.XPATH,"//a[contains(@href, 'gift-cards')]")
    # ---------- Brand Category Locators ----------
    paw_patrol_brand_link = (By.XPATH,"//a[@title='Paw Patrol']")


    # Testcase 9
    footer_contact_us_link = (By.XPATH, "//ul[@id='footerNavList0']/li/a[text()='Contact Us']")

 