"""
Pruebas de inicio de sesión con pausas para visualización.

"""
import time
import pytest
from pages.login_page import LoginPage
from utils.reader import read_users_csv

@pytest.mark.parametrize("data", read_users_csv())
def test_login(driver, data):
    login_page = LoginPage(driver)
    driver.get("https://www.saucedemo.com/")
    time.sleep(3)  # Pausa para ver la página de login abierta
    
    login_page.login(data["usuario"], data["password"])
    time.sleep(3)  # Pausa para ver el resultado del intento de inicio de sesión

    if data["tipo_usuario"] == "True":
        assert "/inventory.html" in driver.current_url
        time.sleep(2)
    elif data["tipo_usuario"] == "False":
        error = login_page.obtener_mensaje_error()
        time.sleep(2)
        assert "Epic sadface" in error