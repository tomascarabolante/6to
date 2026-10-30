from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class AuthPage(BasePage):
    def open_login(self):
        self.open("/login")
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "form input")))

    def register(self, name, email, password):
        self.open("/registro")
        fields = self.wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "form input"))
        )
        fields[0].send_keys(name)
        fields[1].send_keys(email)
        fields[2].send_keys(password)
        self.click_text("button", "Registrarme")
        self.visible_text("Cuenta creada")

    def login(self, email, password):
        self.open_login()
        fields = self.driver.find_elements(By.CSS_SELECTOR, "form input")
        fields[0].send_keys(email)
        fields[1].send_keys(password)
        self.click_text("button", "Entrar")
        self.wait.until(EC.url_contains("/turnos"))

    def login_error(self, email, password):
        self.open_login()
        fields = self.driver.find_elements(By.CSS_SELECTOR, "form input")
        fields[0].send_keys(email)
        fields[1].send_keys(password)
        self.click_text("button", "Entrar")
        return self.visible_text("Email o contraseña incorrectos")

    def logout(self):
        self.click_text("a", "Salir")
        self.wait.until(EC.url_contains("/login"))