from selenium import webdriver
from src.products_page_scraper.paginas.cambiaFX_products_page_scraper import cambiaFXPageScraper
from src.products_page_scraper.paginas.cambioMundial_products_page_scraper import cambioMundialPageScraper
from src.products_page_scraper.paginas.cambioSol_products_page_scraper import cambioSolPageScraper
from src.products_page_scraper.paginas.yanki_products_page_scraper import yankiPageScraper
from src.products_page_scraper.paginas.intiCambio_products_page_scraper import intiCambioPageScraper
from src.products_page_scraper.paginas.chapaCambio_products_page_scraper import chapaCambioPageScraper
from src.products_page_scraper.paginas.dichiKash_products_page_scraper import dichiKashPageScraper
from src.products_page_scraper.paginas.digitalCambio_products_page_scraper import digitalCambioPageScraper
from src.products_page_scraper.paginas.wester_products_page_scraper import westerUnionPageScraper
from src.products_page_scraper.paginas.acomo_products_page_scraper import acomoPageScraper

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
    inti_search_result_url = "https://www.cambiomundial.com/?utm_source=ced"
    chapa_search_result_url = "https://chapacambio.com/?c=CHAPACUANTO"
    dichiKash_search_result_url = "https://dichikash.com/?utm_source=ced"
    digital_search_result_url = "https://cambiodigitalperu.com/"
    wester_search_result_url = "https://www.westernunionperu.pe/cambiodemoneda?utm_source=ced&utm_content=listado"
    acomo_search_result_url = "https://acomo.com.pe/"

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
    
    inti_Cambio_Page_Scraper = intiCambioPageScraper(driver=webdriver.Chrome(options=options))
    inti_search_result_html = inti_Cambio_Page_Scraper.get_html(inti_search_result_url)
    inti_cambio = inti_Cambio_Page_Scraper.get_cambio(html_content=inti_search_result_html)
    
    chapa_Cambio_Page_Scraper = chapaCambioPageScraper(driver=webdriver.Chrome(options=options))
    chapa_search_result_html = chapa_Cambio_Page_Scraper.get_html(chapa_search_result_url)
    chapa_cambio = chapa_Cambio_Page_Scraper.get_cambio(html_content=chapa_search_result_html)
    
    dichikash_Cambio_Page_Scraper = dichiKashPageScraper(driver=webdriver.Chrome(options=options))
    dichikash_search_result_html = dichikash_Cambio_Page_Scraper.get_html(dichiKash_search_result_url)
    dichikash_cambio = dichikash_Cambio_Page_Scraper.get_cambio(html_content=dichikash_search_result_html)

    digital_Cambio_Page_Scraper = digitalCambioPageScraper(driver=webdriver.Chrome(options=options))
    digital_search_result_html = digital_Cambio_Page_Scraper.get_html(digital_search_result_url)
    digital_cambio = digital_Cambio_Page_Scraper.get_cambio(html_content=digital_search_result_html)

    westerUnion_Cambio_Page_Scraper = westerUnionPageScraper(driver=webdriver.Chrome(options=options))
    westerUnion_search_result_html = westerUnion_Cambio_Page_Scraper.get_html(wester_search_result_url)
    westerUnion_cambio = westerUnion_Cambio_Page_Scraper.get_cambio(html_content=westerUnion_search_result_html)

    acomo_Cambio_Page_Scraper = acomoPageScraper(driver=webdriver.Chrome(options=options))
    acomo_search_result_html = acomo_Cambio_Page_Scraper.get_html(acomo_search_result_url)
    acomo_cambio = acomo_Cambio_Page_Scraper.get_cambio(html_content=acomo_search_result_html)

    print(cambioMundial_cambio,"<<<<<<<<<<<<<<<<<<<<<<<<<<< aqui el cambio asdsada")

    cambioList = [
        cambiaFX_cambio,
        cambioMundial_cambio,
        cambioSol_cambio,
        yanki_cambio,
        inti_cambio,
        chapa_cambio,
        dichikash_cambio,
        digital_cambio,
        westerUnion_cambio,
        acomo_cambio
    ]
    
    return cambioList

            


if __name__== "__main__":
    init()