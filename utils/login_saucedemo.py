from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Credenciales 
LOGIN_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

def login_standard_user(driver):
    """
    Función auxiliar que navega a la URL de login,
    ingresa las credenciales de 'standard_user' y se loguea.
    Espera hasta que la página de inventario cargue.
    """
    driver.get(LOGIN_URL)
    wait = WebDriverWait(driver, 10)
    
    # Esperar a que los campos estén presentes y visibles
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()
    
    # Esperar a que cargue la página de inventario
    # Esperamos por un elemento clave de esa página, como el menú
    wait.until(EC.visibility_of_element_located((By.ID, "react-burger-menu-btn")))