"""
Configuración de Pytest, inicio de Chrome y capturas ante fallos.
Autora: Erika Silverio
"""
import os
import pytest
from datetime import datetime
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    reporte = outcome.get_result()
    if reporte.when == "call" and reporte.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("reports/screenshots", exist_ok=True)
            fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            driver.save_screenshot(f"reports/screenshots/{item.name}_{fecha}.png")