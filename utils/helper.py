from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    return driver

class SauceDemoHelper:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir_pagina(self):
        self.driver.get("https://www.saucedemo.com/")

    def iniciar_sesion(self, usuario, password):
        self.driver.find_element(By.ID, "user-name").send_keys(usuario)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    def verificar_inventario(self):
        assert "/inventory.html" in self.driver.current_url
        titulo = self.driver.find_element(By.CSS_SELECTOR, "div.header_secondary_container .title").text
        assert titulo == "Products"

    def agregar_primer_producto_al_carrito(self):
        btn_agregar = self.driver.find_element(By.XPATH, "(//button[contains(@id, 'add-to-cart')])[1]")
        btn_agregar.click()

    def obtener_contador_carrito(self):
        badge = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        return badge.text
