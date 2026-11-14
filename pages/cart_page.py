"""
Pantalla del carrito de compras.

"""
from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.item_name = (By.CLASS_NAME, "inventory_item_name")

    def get_cart_items_names(self):
        items = self.driver.find_elements(*self.cart_items)
        return [item.find_element(*self.item_name).text for item in items]