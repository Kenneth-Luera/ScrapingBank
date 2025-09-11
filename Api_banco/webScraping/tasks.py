import requests
from celery import shared_task
from src import main



@shared_task
def enviar_post_automatico():
    url = "http://127.0.0.1:8000/api/scrapingList/"
    data = {
        "codScraping": "Scraping"
        }

    try:
        response = requests.post(url, json=data)
        return {"status": response.status_code, "response": response.text}
    except Exception as e:
        return {"error": str(e)}

@shared_task
def enviar_post_automatico_banco():
    enviar_post_automatico()
    results = []
    information = main.init()
    url = "http://127.0.0.1:8000/api/bancos/"
    print(information,"<<<<<<<<<<<<<<<<<<<<<<<<<<< aqui la information")
    for i in information:
        imformation_name = i["name"]
        imformation_compra = i["compra"]
        imformation_venta = i["venta"]
        data = {
            "name": imformation_name,
            "compra": imformation_compra,
            "venta": imformation_venta,
            }
        print(data,"<<<<<<<<<<<<<<<<<<<<<<<<<<< aqui el data")
        try:
            response = requests.post(url, json=data)
            print(response,"<<<<<<<<<<<<<<<<<<<<<<<<<<< aqui la response")
            results.append({
                "status": response.status_code,
                "response": response.text
            })

        except Exception as e:
            print(e,"<<<<<<<<<<<<<<<<<<<<<<<<<<< aqui el error")
            results.append({"error": str(e)})
    return results