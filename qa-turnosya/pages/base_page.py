from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, base_url, timeout=8):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, timeout)

    def open(self, path):
        self.driver.get(f"{self.base_url}{path}")

    def click_text(self, tag, text):
        locator = (By.XPATH, f"//{tag}[normalize-space()={self._xpath_literal(text)}]")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def visible_text(self, text):
        locator = (By.XPATH, f"//*[contains(normalize-space(.), {self._xpath_literal(text)})]")
        return self.wait.until(EC.visibility_of_element_located(locator))

    def _xpath_literal(self, value):
        if "'" not in value:
            return f"'{value}'"
        if '"' not in value:
            return f'"{value}"'
        parts = value.split("'")
        return "concat(" + ", \"'\", ".join(f"'{part}'" for part in parts) + ")"