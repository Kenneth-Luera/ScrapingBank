from .zCambio import Cambio
from .products_page_scraper import CambioPageScraper
from bs4 import BeautifulSoup
from time import sleep

class cambioMundialPageScraper(CambioPageScraper):

    def __init__(self, driver) -> None:
        self.driver = driver

    def get_html(self, url: str) -> BeautifulSoup:
        self.driver.get(url)
        sleep(30)
        content = self.driver.page_source
        html = BeautifulSoup(content, "html.parser")
        return html

    def get_cambio(self, html_content: BeautifulSoup):

        name = ("CambioMundial")


        compra = html_content.find("label", {"id": "lblvalorcompra"})
        venta = html_content.find("label", {"id": "lblvalorventa"})

        compra = f"S/ {compra.get_text(strip=True)}" if compra else None
        venta = f"S/ {venta.get_text(strip=True)}" if venta else None
        

        print(name, "<<<<<<<<<<< name")
        print("Compra:", compra, "<<<<<<<<<<<")
        print("Venta:", venta, "<<<<<<<<<<<")


        return {"name":name, "compra":compra, "venta": venta}