from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):    
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
     
    def should_have_product_name_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert self.is_element_with_text_present(*ProductPageLocators.ALERT_MESSAGES_KEY_WORDS, product_name), "Alert has incorrect product name"
        
    def should_have_product_price_in_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert self.is_element_with_text_present(*ProductPageLocators.ALERT_MESSAGES_KEY_WORDS, product_price), "The price of the basket does not match the price of the product."

    def is_element_with_text_present(self, how, what, text):
        elements = self.browser.find_elements(how, what)
        result=False
        for el in elements:
            if text == el.text:
                result = True
        return result

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCES_MESSAGE), \
               "Success message is presented, but should not be"
        
    def success_message_should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCES_MESSAGE), \
               "Success message does not disappeared, but should be"
