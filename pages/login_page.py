"""
Page Object de la pantalla de inicio de sesión.

"""
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

    def login(self, username, password):
        user_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        )
        user_field.clear()
        user_field.send_keys(username)

        pass_field = self.driver.find_element(*self.password_input)
        pass_field.clear()
        pass_field.send_keys(password)

        self.driver.find_element(*self.login_button).click()

    def obtener_mensaje_error(self):
        return self.driver.find_element(*self.error_message).text