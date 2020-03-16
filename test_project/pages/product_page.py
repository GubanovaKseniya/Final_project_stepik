from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):    
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_have_product_name_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert self.is_element_present(*ProductPageLocators.alert_message_with_text(product_name)), \
               "Alert has incorrect product name"
        
    def should_have_product_price_in_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert self.is_element_present(*ProductPageLocators.alert_message_with_text(product_price)), \
               "The price of the basket does not match the price of the product"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.alert_message_with_text_contains('has been added to your basket')), \
               "Success message is presented, but should not be"

        
    def success_message_should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.alert_message_with_text_contains('has been added to your basket')), \
               "Success message does not disappeared, but should be"
