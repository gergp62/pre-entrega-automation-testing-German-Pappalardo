# Proyecto de Automatización (Pre-entrega) - Saucedemo

Este proyecto es una pre-entrega para el curso de automatización, enfocado en probar la funcionalidad clave del sitio web [saucedemo.com](https://www.saucedemo.com/).

---

## 🎯 Propósito del Proyecto

El objetivo principal es crear una suite de pruebas automatizadas que cubra el flujo E2E (End-to-End) más crítico de la aplicación, incluyendo:

* **Automatización de Login:**
    * Navegar a la página de login.
    * Ingresar credenciales válidas (usuario: `standard_user`, contraseña: `secret_sauce`).
    * Validar un login exitoso verificando la redirección a la página de inventario.

* **Caso de Prueba de Navegación:**
    * Verificar que el título de la página de inventario sea "Products".
    * Comprobar que existan productos visibles en la página.
    * Validar que elementos importantes de la UI estén presentes (menú, filtros, etc.).

* **Caso de Prueba de Carrito:**
    * Añadir un producto al carrito.
    * Verificar que el contador del ícono del carrito se incremente.
    * Navegar a la página del carrito.
    * Comprobar que el producto añadido aparezca correctamente.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python
* **Framework de Pruebas:** Pytest
* **Automatización de Navegador:** Selenium WebDriver
* **Reportes:** `pytest-html` (para la generación de reportes)
* **Control de Versiones:** Git y GitHub

---

## ⚙️ Configuración e Instalación

Para ejecutar este proyecto en tu máquina local, sigue estos pasos.

### 1. Clonar el Repositorio
```bash
git clone https://github.com/gergp62/pre-entrega-automation-testing-German-Pappalardo.git
cd pre-entrega-German-Pappalardo
```

### 2. (Opcional pero recomendado) Crear un Entorno Virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias
Este proyecto utiliza un archivo `requirements.txt` para manejar las dependencias.

*Si aún no lo has creado, crea un archivo `requirements.txt` con este contenido:*
```txt
pytest
selenium
pytest-html
```

*Luego, ejecuta el siguiente comando para instalar todo lo necesario:*
```bash
pip install -r requirements.txt
```

---

## 🚀 Ejecución de Pruebas

Para ejecutar la suite de pruebas completa y generar un reporte HTML, utiliza el siguiente comando desde la terminal (asegúrate de estar en la carpeta raíz del proyecto):

```bash
pytest pre-entrega-final/test_saucedemo.py -v --html=reporte.html
```

* `-v`: (Verbose) Muestra un resultado más detallado por cada test.
* `--html=reporte.html`: Genera un archivo llamado `reporte.html` en la misma carpeta con los resultados visuales de la ejecución.

Una vez finalizado, puedes abrir el archivo `reporte.html` en cualquier navegador web para ver los resultados.