from playwright.async_api import async_playwright, TimeoutError
from uuid import uuid4
import asyncio
import logging
from src.template.template import Template
from src.database.connections.mongodb.bd import get_collection
from src.enum.status_enum import Status
from datetime import datetime
# Configuración de logging
logging.basicConfig(level=logging.INFO)
def normalize_item(item):
    """
    Normaliza un solo item de la colección, transformando las propiedades
    para que tenga una salida más sencilla.
    """

    # Normalizar ObjectId
    normalized_item = {
        "id": str(item["_id"]),  # Convertir ObjectId a string
        "batchId": item["batchId"],
        "createdAt": item["createdAt"].isoformat() if isinstance(item["createdAt"], datetime) else item["createdAt"],
        "updatedAt": item["updatedAt"].isoformat() if isinstance(item["updatedAt"], datetime) else item["updatedAt"],
        "status": item["status"],
        "producto": item["producto"],
        "precio": item["precio"],
        "img": item["img"]
    }

    return normalized_item

class Scraper:
    def __init__(
        self, url="https://www.tiendasjumbo.co/televisores-y-audio", headless=True, bach_id=str(uuid4())
    ) -> None:
        self.headless = headless
        self.url = url
        self.bach_id = bach_id

    async def start(self):
        """Iniciar el proceso de scraping."""
        async with async_playwright() as p:
            logging.warning("Iniciar el proceso de scraping.")
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context()

            page = await context.new_page()

            try:
                # Abrir la URL
                await page.goto(self.url)

                # Esperar a que la página cargue completamente
                await page.wait_for_load_state("load", timeout=30000)

                # Realizar scroll hasta el final de la página para cargar todos los productos
                last_height = await page.evaluate('document.body.scrollHeight')
                
                while True:
                    # Hacer scroll hacia abajo
                    await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
                    await page.wait_for_timeout(1000)  # Esperar un segundo para que se carguen los productos
                    
                    # Verificar si el scroll ha llegado al final
                    new_height = await page.evaluate('document.body.scrollHeight')
                    if new_height == last_height:
                        break
                    last_height = new_height

                # Buscar todos los elementos con la clase 'tiendasjumboqaio-cmedia-integration-cencosud-0-x-galleryItem'
                productos = await page.query_selector_all(
                    ".tiendasjumboqaio-cmedia-integration-cencosud-0-x-galleryItem"
                )

                # Verificar si se encontraron productos
                if productos:
                    logging.info(f"Se encontraron {len(productos)} productos.")

                    for producto in productos:
                        # Extraer el nombre del producto
                        nombre = await producto.query_selector(
                            ".vtex-product-summary-2-x-productNameContainer"
                        )
                        logging.info("Obteniendo nombre del producto.")
                        nombre_producto = (
                            await nombre.inner_text()
                            if nombre
                            else "Nombre no disponible"
                        )

                        # Extraer el precio
                        logging.info("Obteniendo precio del producto.")
                        precio = await producto.query_selector(
                            ".tiendasjumboqaio-jumbo-minicart-2-x-price"
                        )
                        precio_producto = (
                            await precio.inner_text()
                            if precio
                            else "Precio no disponible"
                        )

                        # Extraer la URL de la imagen
                        logging.info("Obteniendo url de la imagen del producto.")
                        imagen = await producto.query_selector(
                            ".vtex-product-summary-2-x-imageNormal.vtex-product-summary-2-x-image"
                        )
                        imagen_url = (
                            await imagen.get_attribute("src")
                            if imagen
                            else "Imagen no disponible"
                        )

                        # Mostrar los resultados
                        data = Template(bach_id=self.bach_id).run()
                        data["producto"] = nombre_producto
                        data["precio"] = precio_producto
                        data["img"] = imagen_url
                        data["status"] = Status.COMPLETE.value
                        try:
                            collection = next(get_collection())
                            logging.info(f"Guardando en base de datos")
                            await collection.insert_one(data)

                        except Exception as e:
                            logging.error(f"No se pudo conectar a base de datos: {e}")
                            
                        logging.info(f"Producto: {nombre_producto}")
                        logging.info(f"Precio: {precio_producto}")
                        logging.info(f"Imagen: {imagen_url}")
                        logging.info(data)
                        logging.info("-" * 40)
                    logging.info(f"Sacando resultados")
                  
                    result= await collection.find({"batchId":self.bach_id}).to_list(length=None)
                   
                    return [normalize_item(item) for item in result]
                   
                       
                            
                            

                else:
                    logging.warning("No se encontraron productos con esa clase.")

            except TimeoutError:
                logging.error("Tiempo de espera agotado al cargar la página.")
                data["status"] = Status.FAILED.value
                
            except Exception as e:
                logging.error(f"Error al intentar hacer scraping: {e}")
                data["status"] = Status.FAILED.value
            finally:
                await browser.close()


async def get_data(
    url: str = "https://www.tiendasjumbo.co/tecnologia/informatica/computadores-portatiles",
):
    scraper = Scraper(url=url)
    await scraper.start()
