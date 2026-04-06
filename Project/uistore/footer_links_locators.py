from selenium.webdriver.common.by import By


class CaseTenLocators:

    # Accept all cookies locator
    POP_UP = (By.ID, "onetrust-accept-btn-handler")

    # Footer anchor area to scroll into view
    FOOTER_TOP = (By.CSS_SELECTOR, "div.footer__top")

    # Useful Links keyword
    USEFUL_LINKS_TEXT = (By.XPATH, "//*[normalize-space()='Useful links']")

    # Footer Links
    ABOUT_US = (By.XPATH, "(//a[@title='About us'])[last()]")
    STORE_FINDER = (By.CSS_SELECTOR, "a[title='Store finder']")
    WEEE_REGULATIONS = (By.XPATH, "//a[contains(@href,'/weee')]")
    PRESS = (By.XPATH, "//a[contains(@href,'/press')]")
    AFFILIATES = (By.CSS_SELECTOR, "a[title='Affiliates']")
    CAREERS = (By.XPATH, "//a[normalize-space()='Careers']")
    GIFT_CARDS = (By.XPATH, "(//a[@title='Gift cards'])[2]")
    KLARNA = (By.XPATH, "//a[contains(@href,'/klarna')]")