from .zCambio import Cambio
from .products_page_scraper import CambioPageScraper
from bs4 import BeautifulSoup
from time import sleep

class intiCambioPageScraper(CambioPageScraper):

    def __init__(self, driver) -> None:
        self.driver = driver

    def get_html(self, url: str) -> BeautifulSoup:
        self.driver.get(url)
        sleep(2)
        content = self.driver.page_source
        html = BeautifulSoup(content, "html.parser")
        return html

    def get_cambio(self, html_content: BeautifulSoup) -> list[Cambio]:
        cambio: list[Cambio] = []

        venta = html_content.find_all("div", {"class": "font-bold cursor-pointer flex flex-col rounded-r-lg py-2 px-4 text-center uppercase text-md shadow-sm text-black hover:bg-gray-100"})
        compra = html_content.find_all("div", {"class": "text-sm font-medium flex mb-2"})
            
        precios=[compra,venta]

        

        name = ("IntiCambio")
        

        for a in precios:
            for index, item in enumerate(a):
                try:
                    item_price = item.text.strip().replace(",", "")
                    cambio.append(Cambio(name=name, price=str(item_price)))
                except Exception as e:
                    print(f"Error con item {index}: {e}")
                    pass
            return cambio