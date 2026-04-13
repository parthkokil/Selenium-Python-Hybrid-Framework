from selenium.webdriver.common.by import By


class FooterLocators:
    # testcase 10 locators
    # Useful Links keyword
    useful_links_text = (By.XPATH, "//*[normalize-space()='Useful links']")

    

    # Footer Links
    footer_store_finder_link = (By.CSS_SELECTOR, "a[title='Store finder']")
    footer_wee_regulations_link = (By.XPATH, "//a[contains(@href,'/weee')]")
    footer_press_link = (By.XPATH, "//a[contains(@href,'/press')]")
    footer_affiliates_link = (By.CSS_SELECTOR, "a[title='Affiliates']")
    footer_careers_link = (By.XPATH, "//a[normalize-space()='Careers']")
    footer_gift_cards_link = (By.XPATH, "//ul[@id='footerNavList2']/li/a[@title='Gift cards']")
    footer_klarna_link = (By.XPATH, "//a[contains(@href,'/klarna')]")


    # footer help section links
    
    footer_delivery_options_link = (By.XPATH,"//ul[@class='footer__nav--links collapse']//a[text()='Delivery Options']")
    footer_product_safety_notices_link = (By.XPATH, "//a[contains(@href,'/product-safety-notices')]")
    footer_returns_link = (By.XPATH, "//ul[@id='footerNavList0']/li/a[text()='Returns']")
    footer_track_your_order_link = (By.XPATH, "//ul[@id='footerNavList0']/li/a[@title='Track your order']")
    footer_help_center_link = (By.CSS_SELECTOR, "a[title='Help Centre']")
    footer_your_privacy_link = (By.XPATH, "//ul[@id='footerNavList0']/li/a[@title=' Your Privacy']")
    footer_how_to_complain_link = (By.CSS_SELECTOR, "a[title='How To Complain']")
 