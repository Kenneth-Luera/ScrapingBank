from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from .zCambio import Cambio


class CambioPageScraper(ABC):
    @abstractmethod
    def get_html(self,url:str)-> BeautifulSoup:
        ...

    @abstractmethod
    def get_cambio(self,html_content: BeautifulSoup)-> list[Cambio]:
        ...