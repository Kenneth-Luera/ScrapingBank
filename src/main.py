import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
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

def create_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--log-level=3")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    temp_profile_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={temp_profile_dir}")

    options.binary_location = "/usr/bin/google-chrome"
    service = Service("/usr/local/bin/chromedriver")

    driver = webdriver.Chrome(service=service, options=options)
    return driver

def init():


    urls = {
        "cambiaFX" : "https://cambiafx.pe/",
        "cambioMundial" : "https://www.cambiomundial.com/?utm_source=ced",
        "cambioSol" : "https://cambiosol.pe/?utm_source=ced",
        "yanki" : "https://yanki.pe/?utm_source=CED&utm_medium=paid&utm_campaign=diciembre",
        "inti" : "https://www.cambiomundial.com/?utm_source=ced",
        "chapa" : "https://chapacambio.com/?c=CHAPACUANTO",
        "dichiKash" : "https://dichikash.com/?utm_source=ced",
        "digital" : "https://cambiodigitalperu.com/",
        "wester" : "https://www.westernunionperu.pe/cambiodemoneda?utm_source=ced&utm_content=listado",
        "acomo" : "https://acomo.com.pe/"
    }

    cambiaFX_driver = create_driver()
    cambiaFX_Cambio_Page_Scraper = cambiaFXPageScraper(driver=cambiaFX_driver)
    cambiaFX_search_result_html = cambiaFX_Cambio_Page_Scraper.get_html(urls["cambiaFX"])
    cambiaFX_cambio = cambiaFX_Cambio_Page_Scraper.get_cambio(html_content=cambiaFX_search_result_html)
    cambiaFX_driver.quit()

    cambioMundial_driver = create_driver()
    cambioMundial_Cambio_Page_Scraper = cambioMundialPageScraper(driver=cambioMundial_driver)
    cambioMundial_search_result_html = cambioMundial_Cambio_Page_Scraper.get_html(urls["cambioMundial"])
    cambioMundial_cambio = cambioMundial_Cambio_Page_Scraper.get_cambio(html_content=cambioMundial_search_result_html)
    cambioMundial_driver.quit()

    cambioSol_driver = create_driver()
    cambioSol_Cambio_Page_Scraper = cambioSolPageScraper(driver=cambioSol_driver)
    cambioSol_search_result_html = cambioSol_Cambio_Page_Scraper.get_html(urls["cambioSol"])
    cambioSol_cambio = cambioSol_Cambio_Page_Scraper.get_cambio(html_content=cambioSol_search_result_html)
    cambioSol_driver.quit()

    yanki_driver = create_driver()
    yanki_Cambio_Page_Scraper = yankiPageScraper(driver=yanki_driver)
    yanki_search_result_html = yanki_Cambio_Page_Scraper.get_html(urls["yanki"])
    yanki_cambio = yanki_Cambio_Page_Scraper.get_cambio(html_content=yanki_search_result_html)
    yanki_driver.quit()
    
    inti_driver = create_driver()
    inti_Cambio_Page_Scraper = intiCambioPageScraper(driver=inti_driver)
    inti_search_result_html = inti_Cambio_Page_Scraper.get_html(urls["inti"])
    inti_cambio = inti_Cambio_Page_Scraper.get_cambio(html_content=inti_search_result_html)
    inti_driver.quit()
    
    chapa_driver = create_driver()
    chapa_Cambio_Page_Scraper = chapaCambioPageScraper(driver=chapa_driver)
    chapa_search_result_html = chapa_Cambio_Page_Scraper.get_html(urls["chapa"])
    chapa_cambio = chapa_Cambio_Page_Scraper.get_cambio(html_content=chapa_search_result_html)
    chapa_driver.quit()
    
    dichikash_driver = create_driver()
    dichikash_Cambio_Page_Scraper = dichiKashPageScraper(driver=dichikash_driver)
    dichikash_search_result_html = dichikash_Cambio_Page_Scraper.get_html(urls["dichiKash"])
    dichikash_cambio = dichikash_Cambio_Page_Scraper.get_cambio(html_content=dichikash_search_result_html)
    dichikash_driver.quit()

    digital_driver = create_driver()
    digital_Cambio_Page_Scraper = digitalCambioPageScraper(driver=digital_driver)
    digital_search_result_html = digital_Cambio_Page_Scraper.get_html(urls["digital"])
    digital_cambio = digital_Cambio_Page_Scraper.get_cambio(html_content=digital_search_result_html)
    digital_driver.quit()

    westerUnion_driver = create_driver()
    westerUnion_Cambio_Page_Scraper = westerUnionPageScraper(driver=westerUnion_driver)
    westerUnion_search_result_html = westerUnion_Cambio_Page_Scraper.get_html(urls["wester"])
    westerUnion_cambio = westerUnion_Cambio_Page_Scraper.get_cambio(html_content=westerUnion_search_result_html)
    westerUnion_driver.quit()

    acomo_driver = create_driver()
    acomo_Cambio_Page_Scraper = acomoPageScraper(driver=acomo_driver)
    acomo_search_result_html = acomo_Cambio_Page_Scraper.get_html(urls["acomo"])
    acomo_cambio = acomo_Cambio_Page_Scraper.get_cambio(html_content=acomo_search_result_html)
    acomo_driver.quit()

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