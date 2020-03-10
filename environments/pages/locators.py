from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form") 
class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    ALERT_MESSAGES_KEY_WORDS = (By.CSS_SELECTOR, "#messages .alertinner strong")
    
