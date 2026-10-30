from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class TurnosPage(BasePage):
    def book(self, date, time, duration, reason):
        date_field = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='date']"))
        )
        time_field = self.driver.find_element(By.CSS_SELECTOR, "input[type='time']")
        self.driver.execute_script(
            "for (const [field, value] of [[arguments[0], arguments[2]], "
            "[arguments[1], arguments[3]]]) {"
            " const setter = Object.getOwnPropertyDescriptor("
            " window.HTMLInputElement.prototype, 'value').set;"
            " setter.call(field, value);"
            " field.dispatchEvent(new Event('input', { bubbles: true }));"
            " field.dispatchEvent(new Event('change', { bubbles: true }));"
            "}",
            date_field,
            time_field,
            date,
            time,
        )
        duration_field = self.driver.find_element(By.CSS_SELECTOR, "input[type='number']")
        duration_field.clear()
        duration_field.send_keys(str(duration))
        reason_field = self.driver.find_element(By.NAME, "motivo")
        reason_field.send_keys(reason)
        assert date_field.get_attribute("value") == date
        assert time_field.get_attribute("value") == time
        assert reason_field.get_attribute("value") == reason
        self.click_text("button", "Reservar")
        feedback = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//p[contains(., 'Turno reservado') or contains(., 'ocupado') or contains(., 'Elegí')]")
            )
        )
        return feedback.text

    def has_booking(self, reason):
        row = (
            By.XPATH,
            f"//table//tr[.//td[contains(normalize-space(.), {self._xpath_literal(reason)})]]",
        )
        try:
            self.wait.until(EC.visibility_of_element_located(row))
            return True
        except Exception:
            return False

    def table_text(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "table"))).text

    def search(self, query):
        search_field = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder*='Buscar']")
        search_field.clear()
        search_field.send_keys(query)
        self.click_text("button", "Buscar")
        self.wait.until(EC.url_contains("q="))
        return self.table_text()

    def cancel(self, reason):
        row = (
            By.XPATH,
            f"//table//tr[.//td[contains(normalize-space(.), {self._xpath_literal(reason)})]]",
        )
        booking_row = self.wait.until(EC.visibility_of_element_located(row))
        booking_row.find_element(By.XPATH, ".//button[normalize-space()='Cancelar']").click()
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()
        self.wait.until(
            EC.text_to_be_present_in_element(row, "cancelado")
        )
        return self.driver.find_element(*row).text