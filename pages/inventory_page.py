"""
Pantalla de catálogo de productos.

"""
from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_items = (By.CLASS_NAME, "inventory_item")
        self.item_name = (By.CLASS_NAME, "inventory_item_name")
        self.item_price = (By.CLASS_NAME, "inventory_item_price")
        self.menu_btn = (By.ID, "react-burger-menu-btn")
        self.filter_container = (By.CLASS_NAME, "product_sort_container")
        self.add_to_cart_btn = (By.XPATH, "//button[contains(@id, 'add-to-cart')]")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def obtener_productos(self):
        return self.driver.find_elements(*self.inventory_items)

    def obtener_nombre_primer_producto(self):
        return self.driver.find_elements(*self.item_name)[0].text

    def obtener_precio_primer_producto(self):
        return self.driver.find_elements(*self.item_price)[0].text

    def menu_visible(self):
        return self.driver.find_element(*self.menu_btn).is_displayed()

    def filtro_visible(self):
        return self.driver.find_element(*self.filter_container).is_displayed()

    def add_first_item_to_cart(self):
        self.driver.find_elements(*self.add_to_cart_btn)[0].click()

    def get_cart_badge_count(self):
        return self.driver.find_element(*self.cart_badge).text

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()