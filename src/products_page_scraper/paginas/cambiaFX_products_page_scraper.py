from .zCambio import Cambio
from .products_page_scraper import CambioPageScraper
from bs4 import BeautifulSoup
from time import sleep

class cambiaFXPageScraper(CambioPageScraper):

    def __init__(self, driver) -> None:
        self.driver = driver

    def get_html(self, url: str) -> BeautifulSoup:
        self.driver.get(url)
        sleep(2)
        content = self.driver.page_source
        html = BeautifulSoup(content, "html.parser")
        return html

    def get_cambio(self, html_content: BeautifulSoup):
        
        name = ("CambiaFX")

        compra, venta = None, None

        for span in html_content.find_all("span", class_="text-xs lg:text-sm font-semibold"):
            parts = [t.strip() for t in span.stripped_strings]
            if len(parts) >= 2:
                if parts[0].lower() == "compra":
                    compra = parts[1]
                elif parts[0].lower() == "venta":
                    venta = parts[1]

        #print(name)
        #print(compra)

        #print(f"banco: {name}, compra: {compra}, venta: {venta}")

        return {"name":name, "compra":compra, "venta":venta}