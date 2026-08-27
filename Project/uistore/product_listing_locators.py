from selenium.webdriver.common.by import By


class ProductListingLocators:
    """
    Page object locators for the Product Listing / Category pages.
    """

    # ---------- Links ----------
    learning_skills_menu_link = (By.CSS_SELECTOR, "a[title='Learning Skills']")
    brands_navigation_link = (By.XPATH, "//a[@title='Brands']")
    dolls_category_link = (By.XPATH, "//a[contains(@href, 'Dolls')]")
    offers_navigation_link = (By.CSS_SELECTOR, "a[title='Offers']")
    explore_navigation_link = (By.CSS_SELECTOR, "a[title*='Explore']")
    first_product_link = (By.CSS_SELECTOR, "a[class*='th']")
    first_product_img = (By.XPATH, "//img[@title='Early Learning Centre Paintbrush Set']")
    first_product_thumbnail_link = (By.CSS_SELECTOR, "a.thumb.clickedObjectIDsAfterSearch")

    # ---------- Filters: Span / Inline Elements ----------
    jigsaw_puzzles_filter_under_toy_type = (By.XPATH, "//span[contains(text(),'Jigsaw')]")
    children_games_filter_under_toy_type = (By.XPATH, "//span[contains(text(),'Children')]")
    discover_world_filter_under_learning_skills = (By.XPATH, "//span[contains(text(),'Discover')]")
    toy_cars_filter_under_toy_type = (By.XPATH, "//span[text()='Toy Cars']")
    imaginative_play_filter_under_learning_skills = (By.XPATH, "//span[text()='Imaginative play']")
    fine_motor_skills_filter_under_learning_skills = (By.XPATH, "//span[text()='Fine motor skills']")
    playsets_filter_option = (By.XPATH, "//span[normalize-space()='Playsets']")
    savings_filter_option = (By.XPATH, "//span[normalize-space()='Savings']")
    huffy_option = (By.XPATH, "//span[text()='Huffy']")
    toddler_bikes_text = (By.XPATH, "//span[text()='Toddler Bikes']")
    search_keyword = (By.XPATH, "//span[text()='Search by brand']")
    disney_checkbox = (By.XPATH, "//span[@class='facet__list__label']/span[text()='Disney']")
    arts_and_craft_text = (By.XPATH, "//span[text()='Arts & Crafts']")
    creativity_checkbox = (By.XPATH, "//span[text()='Creativity']")
    soft_toy = (By.XPATH, "//span[text()='Soft Toys']")
    stimulating_senses = (By.XPATH, "//span[text()='Stimulating senses']")
    baby_activity_toys = (By.XPATH, "//span[text()='Baby Activity Toys']")
    early_learning_center = (By.XPATH, "//span[text()='Early Learning Centre']")
    # --- BACKUP (different strategy): generic class-based selector ---
    # early_learning_center = (By.CLASS_NAME, "facet__list__text")
    hand_eye_coordination = (By.XPATH, "//span[text()='Hand eye coordination']")

    # ---------- Containers / Divs ----------
    show_more_text = (By.XPATH, "//div[@class='ais-RefinementList facet__values']/button[text()='Show more']")
    brands_verify = (By.XPATH, "//div[text()=' Brands ']")
    dolls_list = (By.CLASS_NAME, "facet__item")

    # ---------- Buttons ----------
    # show_more_under_toy_type = (By.CSS_SELECTOR, "button[class*='-M']")
    show_more_under_toy_type = (By.XPATH, "//button[@class='ais-Menu-showMore facet__more']")
    show_more = (By.CSS_SELECTOR, "button[class='ais-Menu-showMore facet__more']")

    # ---------- Texts ----------
    relevant_text = (By.XPATH, "//h1[text()='Soft Toys']")
    relevant_content = (By.XPATH, "//h1[text()='Newborn Baby Gifts']")

    # ---------- Product Cards ----------
    # first_product_card = (By.XPATH, "//img[@title='Cupcake Doll and Stroller Pink']")
    first_product_card = (By.XPATH, "(//img[@title])[1]")