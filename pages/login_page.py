"""
Page Object Login con cursor visual y simulación.

"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.XPATH, "//h3[@data-test='error']")
        
        # Inyectar un cursor visual flotante en la página web
        self._crear_cursor_visual()

    def _crear_cursor_visual(self):
        """Crea un punto rojo brillante en la pantalla que simula el cursor del mouse."""
        script = """
        if (!document.getElementById('fake-cursor')) {
            var cursor = document.createElement('div');
            cursor.id = 'fake-cursor';
            cursor.style.position = 'absolute';
            cursor.style.width = '20px';
            cursor.style.height = '20px';
            cursor.style.borderRadius = '50%';
            cursor.style.backgroundColor = 'rgba(255, 0, 0, 0.7)';
            cursor.style.border = '2px solid white';
            cursor.style.boxShadow = '0px 0px 10px red';
            cursor.style.zIndex = '10000';
            cursor.style.pointerEvents = 'none';
            cursor.style.transition = 'all 0.3s ease';
            cursor.style.left = '0px';
            cursor.style.top = '0px';
            document.body.appendChild(cursor);
        }
        """
        self.driver.execute_script(script)

    def _mover_cursor_a_elemento(self, elemento):
        """Mueve el cursor visual hasta la posición exacta del elemento en pantalla."""
        ubicacion = elemento.location_once_scrolled_into_view
        x = elemento.location['x'] + 10
        y = elemento.location['y'] + 10
        script = f"""
        var cursor = document.getElementById('fake-cursor');
        if (cursor) {{
            cursor.style.left = '{x}px';
            cursor.style.top = '{y}px';
        }}
        """
        self.driver.execute_script(script)
        time.sleep(0.4) # Pausa para ver el movimiento del cursor

    def _escribir_como_humano(self, elemento, texto):
        """Escribe el texto letra por letra simulando tipeo real."""
        self._mover_cursor_a_elemento(elemento)
        elemento.clear()
        for letra in texto:
            elemento.send_keys(letra)
            time.sleep(0.15) # Pausa entre cada letra

    def login(self, username, password):
        # 1. Manejar campo usuario con cursor y tipeo visible
        campo_usuario = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        )
        self._escribir_como_humano(campo_usuario, username)

        # 2. Manejar campo contraseña
        campo_clave = self.driver.find_element(*self.password_input)
        self._escribir_como_humano(campo_clave, password)

        # 3. Mover cursor al botón y hacer clic
        boton = self.driver.find_element(*self.login_button)
        self._mover_cursor_a_elemento(boton)
        time.sleep(0.5)
        boton.click()
        time.sleep(1)

    def obtener_mensaje_error(self):
        error_elem = self.driver.find_element(*self.error_message)
        self._mover_cursor_a_elemento(error_elem)
        return error_elem.text