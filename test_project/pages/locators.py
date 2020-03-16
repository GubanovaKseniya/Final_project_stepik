from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, ".content .basket-items")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, ".content  #content_inner p")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    INPUT_EMAIL_ADRESS = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form .btn")

class ProductPageLocators():    
    @staticmethod
    def alert_message_with_text_contains(text):
        resultSelector = "//*[@id = 'messages']//*[text()[contains(.,\""+text+"\")]]"      
        return (By.XPATH, resultSelector)
    
    @staticmethod
    def alert_message_with_text(text):
        resultSelector = "//*[@id = 'messages']//*[text()=\""+text+"\"]"      
        return (By.XPATH, resultSelector)        
    
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    
