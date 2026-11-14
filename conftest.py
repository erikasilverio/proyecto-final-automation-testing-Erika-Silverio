"""
Configuración global de Pytest y manejo del navegador Chrome.
Autora: Erika Silverio
"""

import os
import pytest
from datetime import datetime
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    # Preparamos Chrome para que se abra maximizado en cada prueba
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    
    # Esperamos hasta 10 segundos si algún botón o campo tarda en aparecer
    driver.implicitly_wait(10)
    
    yield driver  # Aquí se ejecuta el caso de prueba
    
    # Al terminar la prueba, cerramos el navegador para no consumir memoria
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Vigilamos el resultado del test; si llega a fallar, guardamos una captura
    outcome = yield
    reporte = outcome.get_result()
    
    if reporte.when == "call" and reporte.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("reports/screenshots", exist_ok=True)
            fecha_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            ruta_foto = f"reports/screenshots/{item.name}_{fecha_hora}.png"
            driver.save_screenshot(ruta_foto)