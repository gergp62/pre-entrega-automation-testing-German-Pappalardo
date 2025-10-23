
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.login_saucedemo import login_standard_user  # Importamos el login desde la carpeta utils

# --- Fixtures de Pytest (Setup y Teardown) ---

@pytest.fixture
def driver():
    """
    Fixture que crea y destruye la instancia del driver
    para cada prueba. Esto asegura que cada test sea
    independiente.
    """
    # Setup del driver
    driver_instance = webdriver.Chrome()
    driver_instance.maximize_window()
    
    # Ceder el control al test
    yield driver_instance
    
    # Teardown (se ejecuta después de cada test)
    driver_instance.quit()

@pytest.fixture
def logged_in_driver(driver):
    """
    Fixture que depende del 'driver' y entrega una sesión
    ya logueada para las pruebas que lo necesiten.
    """
    login_standard_user(driver)
    return driver

# --- Casos de Prueba (Tests) ---

def test_login_exitoso(driver):
    """
    Consigna 1: Automatización de Login
    Verifica el login y la redirección a la página de inventario.
    """
    login_standard_user(driver)
    wait = WebDriverWait(driver, 10)
    
    # Criterio 1: Validar redirección a /inventory.html
    assert "inventory.html" in driver.current_url, "La URL no es la de inventario"
    
    # Criterio 2: Validar título "Products"
    # "Swag Labs" es el logo, "Products" es el título de la página
    title_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
    assert title_element.text == "Products", "El título de la página no es 'Products'"

def test_navegacion_y_catalogo(logged_in_driver):
    """
    Consigna 2: Navegación y Verificación del Catálogo
    Usa el fixture 'logged_in_driver' para empezar ya logueado.
    """
    driver = logged_in_driver  # Renombramos para claridad
    wait = WebDriverWait(driver, 10)

    # Criterio 1: Valida título (ya cubierto en el test anterior, pero
    # la consigna lo pide y asegura independencia del test)
    title_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
    assert title_element.text == "Products"

    # Criterio 2: Valida presencia de productos (al menos uno)
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "No se encontraron productos en la página"

    # Criterio 3: Validar elementos de la interfaz (menú y filtros)
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    filtro_productos = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert menu_button.is_displayed(), "El botón de menú no está visible"
    assert filtro_productos.is_displayed(), "El filtro de productos no está visible"

    # Criterio 4: Lista nombre/precio del primero
    first_product_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    first_product_price = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    
    # Imprimimos en consola (se verá si se ejecuta con el parámetro -s)
    print(f"\n[Info] Primer producto: {first_product_name} | Precio: {first_product_price}")
    
    # Validamos que los datos sean los esperados
    assert first_product_name == "Sauce Labs Backpack"
    assert first_product_price == "$29.99"

def test_flujo_de_carrito(logged_in_driver):
    """
    Consigna 3: Caso de Prueba de Carrito
    Usa el fixture 'logged_in_driver' para empezar ya logueado.
    """
    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)

    # Criterio 1: Agrega primer producto
    add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_to_cart_button.click()

    # Criterio 2: Verifica ítem en carrito (contador)
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1", "El contador del carrito no se actualizó a 1"
    
    # Criterio 3: Navegar al carrito
    cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_link.click()
    
    # Esperar a que cargue la página del carrito
    wait.until(EC.url_contains("cart.html"))
    
    # Criterio 4: Comprobar que el producto añadido aparezca
    item_in_cart_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert item_in_cart_name == "Sauce Labs Backpack", "El producto en el carrito no es el correcto"