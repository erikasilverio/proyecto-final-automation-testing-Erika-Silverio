"""
Prueba del carrito de compras con pausas paso a paso.

"""
import time
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_agregar_al_carrito(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    time.sleep(3)
    
    inventory_page = InventoryPage(driver)
    nombre_producto = inventory_page.obtener_nombre_primer_producto()
    
    inventory_page.add_first_item_to_cart()
    time.sleep(3)  # Pausa para ver cuando se añade el producto al carrito
    
    assert inventory_page.get_cart_badge_count() == "1"
    
    inventory_page.go_to_cart()
    time.sleep(3)  # Pausa dentro de la página del carrito
    
    cart_page = CartPage(driver)
    assert nombre_producto in cart_page.get_cart_items_names()
    time.sleep(3)  # Pausa final antes de cerrar para validar que si fuero hechas las pruebas necesarias.