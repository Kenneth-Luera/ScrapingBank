from selenium import webdriver
from src.products_page_scraper.paginas.cambiaFX_products_page_scraper import cambiaFXPageScraper
from src.products_page_scraper.paginas.cambioMundial_products_page_scraper import cambioMundialPageScraper
from src.products_page_scraper.paginas.cambioSol_products_page_scraper import cambioSolPageScraper
from src.products_page_scraper.paginas.yanki_products_page_scraper import yankiPageScraper

print("aqui entra")

def init():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--log-level=3")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    cambiaFX_search_result_url = "https://cambiafx.pe/"
    cambioMundial_search_result_url = "https://www.cambiomundial.com/?utm_source=ced"
    cambioSol_search_result_url = "https://cambiosol.pe/?utm_source=ced"
    yanki_search_result_url = "https://yanki.pe/?utm_source=CED&utm_medium=paid&utm_campaign=diciembre"
    intiCambio_search_result_url = "https://inticambio.pe/"

    cambiaFX_Cambio_Page_Scraper = cambiaFXPageScraper(driver=webdriver.Chrome(options=options))
    cambiaFX_search_result_html = cambiaFX_Cambio_Page_Scraper.get_html(cambiaFX_search_result_url)
    cambiaFX_cambio = cambiaFX_Cambio_Page_Scraper.get_cambio(html_content=cambiaFX_search_result_html)

    cambioMundial_Cambio_Page_Scraper = cambioMundialPageScraper(driver=webdriver.Chrome(options=options))
    cambioMundial_search_result_html = cambioMundial_Cambio_Page_Scraper.get_html(cambioMundial_search_result_url)
    cambioMundial_cambio = cambioMundial_Cambio_Page_Scraper.get_cambio(html_content=cambioMundial_search_result_html)

    cambioSol_Cambio_Page_Scraper = cambioSolPageScraper(driver=webdriver.Chrome(options=options))
    cambioSol_search_result_html = cambioSol_Cambio_Page_Scraper.get_html(cambioSol_search_result_url)
    cambioSol_cambio = cambioSol_Cambio_Page_Scraper.get_cambio(html_content=cambioSol_search_result_html)
    
    yanki_Cambio_Page_Scraper = yankiPageScraper(driver=webdriver.Chrome(options=options))
    yanki_search_result_html = yanki_Cambio_Page_Scraper.get_html(yanki_search_result_url)
    yanki_cambio = yanki_Cambio_Page_Scraper.get_cambio(html_content=yanki_search_result_html)

    print(cambioMundial_cambio,"<<<<<<<<<<<<<<<<<<<<<<<<<<< aqui el cambio asdsada")

    cambioList = [
        cambiaFX_cambio,
        cambioMundial_cambio,
        cambioSol_cambio,
        yanki_cambio
    ]
    
    return cambioList

            


if __name__== "__main__":
    init()