from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLokators

class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLokators.BASKET_ITEM), \
                "Product in basket is presented, but should not be"


    def should_be_empty_basket_message(self):
        basket_empty_message = self.browser.find_element(*BasketPageLokators.BASKET_EMPTY_MESSAGE).text
        assert "Your basket is empty" in basket_empty_message, \
               "Message about empty basket dosen't present"
