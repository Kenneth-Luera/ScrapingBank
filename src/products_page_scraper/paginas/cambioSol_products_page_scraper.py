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

    def get_cambio(self, html_content: BeautifulSoup) -> list[Cambio]:
        cambio: list[Cambio] = []

        precios = html_content.find_all("div", {"class": "rate-box sell"})
        name = ("CambioSol")
        
        for index, item in enumerate(precios):
            try:
                item_price = item.text.strip().replace(",", "")
                cambio.append(Cambio(name=name, price=str(item_price)))
            except Exception as e:
                print(f"Error con item {index}: {e}")
                pass

        return cambio
