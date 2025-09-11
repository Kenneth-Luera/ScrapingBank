from .zCambio import Cambio
from .products_page_scraper import CambioPageScraper
from bs4 import BeautifulSoup
from time import sleep

class cambioSolPageScraper(CambioPageScraper):

    def __init__(self, driver) -> None:
        self.driver = driver

    def get_html(self, url: str) -> BeautifulSoup:
        self.driver.get(url)
        sleep(2)
        content = self.driver.page_source
        html = BeautifulSoup(content, "html.parser")
        return html

    def get_cambio(self, html_content: BeautifulSoup): 

        name = ("CambioSol")
        
        compra =html_content.find("span",{"id": "buy-rate-display"})
        venta =html_content.find("span",{"id": "sell-rate-display"})

        compra = f" {compra.get_text(strip=True)}" if compra else None
        venta = f" {venta.get_text(strip=True)}" if venta else None

        return {"name":name, "compra":compra, "venta": venta}
