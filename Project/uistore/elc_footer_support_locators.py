from selenium.webdriver.common.by import By


class ElcFooterSupportLocators:
    """
    Locator Class Name: ElcFooterSupportPageLocators
    Author: Sasi Kumar
    Description:
        Contains all locators related to the Elc Footer Support page workflow.
    """
    # Cookie / Consent
    ACCEPT_COOKIES_BUTTON = (By.ID, "onetrust-accept-btn-handler")

    # Footer - Help & Support Links
    FOOTER_CONTACT_US_LINK = (By.XPATH, "(//a[@title='Contact Us'])[2]")

    FOOTER_DELIVERY_OPTIONS_LINK = (By.XPATH, "(//a[text()='Delivery Options'])[2]")

    FOOTER_PRODUCT_SAFETY_NOTICES_LINK = (By.XPATH, "//a[contains(@href,'/product-safety-notices')]")

    FOOTER_RETURNS_LINK = (By.XPATH, "(//a[@title='Returns'])[2]")

    FOOTER_TRACK_YOUR_ORDER_LINK = (By.XPATH, "(//a[text()='Track your order'])[4]")

    FOOTER_HELP_CENTRE_LINK = (By.XPATH, "//a[@title='Help Centre']")

    FOOTER_PRIVACY_POLICY_LINK = (By.XPATH, "//a[@title=' Your Privacy']")

    FOOTER_HOW_TO_COMPLAIN_LINK = (By.XPATH, "//a[@title='How To Complain']")
