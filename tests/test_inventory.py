"""
Pruebas del catálogo de productos con pausas.

"""
import time
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_inventory(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    driver.get("https://www.saucedemo.com/")
    time.sleep(3)
    
    login_page.login("standard_user", "secret_sauce")
    time.sleep(3)  # Pausa al entrar a la vista de inventario

    productos = inventory_page.obtener_productos()
    assert len(productos) > 0
    time.sleep(2)
    
    assert inventory_page.obtener_nombre_primer_producto() == "Sauce Labs Backpack"
    assert inventory_page.obtener_precio_primer_producto() == "$29.99"
    assert inventory_page.menu_visible()
    assert inventory_page.filtro_visible()
    time.sleep(3)  # Pausa antes de cerrar la prueba de inventario para que se pueda mirar bien la prueba