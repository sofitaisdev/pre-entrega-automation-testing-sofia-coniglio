from utils.helper import setup_driver, SauceDemoHelper

def test_flujo_completo_saucedemo():
    driver = setup_driver()
    helper = SauceDemoHelper(driver)
    
    try:
        helper.abrir_pagina()
        helper.iniciar_sesion("standard_user", "secret_sauce")
        helper.verificar_inventario()
        print("Título de sección OK - Products")

        helper.agregar_primer_producto_al_carrito()
        badge = helper.obtener_contador_carrito()
        assert badge == "1"
        print("Carrito OK -> 1")
        
        print("Test OK")

    finally:
        driver.quit()
