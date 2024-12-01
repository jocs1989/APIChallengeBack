import motor.motor_asyncio
import logging
from playwright.async_api import async_playwright, TimeoutError
import asyncio

# Configuración de logging
logging.basicConfig(level=logging.INFO)

class Scraper():
    def __init__(self, url="https://www.tiendasjumbo.co/televisores-y-audio", headless=False) -> None:
        self.headless = headless
        self.url = url

    async def start(self):
        """Iniciar el proceso de scraping."""
        async with async_playwright() as p:
            logging.warning("Iniciar el proceso de scraping.")
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context()

    
            page = await context.new_page()

            try:
                # Abrir la URL
                await asyncio.wait_for(page.goto(self.url), timeout=10)

                # Ejemplo: Extraer información de productos (por ejemplo, los nombres de los televisores)
                products = await page.query_selector_all('div.product')  # Cambia el selector según el sitio web

                product_names = []
                for product in products:
                    name = await product.query_selector('span.product-name')  # Cambia según el selector
                    if name:
                        product_names.append(await name.inner_text())

                logging.info(f"Productos encontrados: {product_names}")
                return product_names

            except TimeoutError:
                logging.error("Tiempo de espera agotado al cargar la página.")
            except Exception as e:
                logging.error(f"Error al intentar hacer scraping: {e}")
            finally:
                await browser.close()

async def get_data(url: str = "https://www.tiendasjumbo.co/televisores-y-audio"):
    scraper = Scraper(url=url)
    result = await scraper.start()
    return result

# Función principal para ejecutar el script
