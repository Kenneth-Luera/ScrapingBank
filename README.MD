# Proyecto de Scraping de Tipos de Cambio

Este proyecto realiza **scraping de tipos de cambio** de diferentes entidades financieras.  
Está compuesto por dos partes principales:

- **Backend**: desarrollado en **Python Django** con **Celery** para la gestión de tareas asíncronas y **Selenium** para el scraping.  
- **Frontend**: desarrollado en **React** con **Ant Design**, desplegado en **AWS S3**.  

El repositorio actual contiene únicamente el **backend**.  
El frontend se encuentra en un repositorio separado:  
El backend está desplegado en **AWS EC2** y pueden revisarlo y probar la funcionalidad en:
 > **http://3.143.240.202:8000/api/lastScraping/**.  
 > **https://github.com/Kenneth-Luera/ScrapingBankFront**

---

## Requisitos

- Python **3.11 o superior**
- Navegador **Google Chrome**
- **ChromeDriver** correspondiente a tu versión de Chrome
- Entorno virtual recomendado

---

## Instalación y Configuración

### 1. Clonar el repositorio
```bash
  git clone https://github.com/Kenneth-Luera/ScrapingBank.git
```
### 2. Crear y activar entorno virtual

En Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
En Linux / Mac:
```bash
python -m venv venv
source venv/bin/activate
```
### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```
### 4. Configurar .env
Debes crear un archivo .env en la raíz del proyecto (donde está manage.py).
Dentro, define al menos la variable de entorno:
```bash
SECRET_KEY_DJANGO=tu_clave_generada
```
Para generar una nueva SECRET_KEY_DJANGO, ejecuta en la terminal:
```bash
python manage.py shell
```
y luego dentro de Python:
```bash
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```
Copia el valor generado y pégalo en tu .env.

### 5. Configurar ChromeDriver

En el archivo src/main.py encontrarás 2 indicaciones donde deberás ajustar la ruta de:

Google Chrome

ChromeDriver

Asegúrate de que ambas rutas apunten a donde tienes instalados estos recursos en tu sistema.

### Ejecución

### 1. Crear migraciones y migrar la base de datos
```bash
python manage.py makemigrations
python manage.py migrate
```
Esto creará una base de datos SQLite3 por defecto.
Si deseas usar otra base de datos, puedes configurarla en el archivo settings.py.

### 2. Levantar el servidor
```bash
python manage.py runserver
```

Para poder ejecutar el scraping en diferentes terminales dentro del proyecto:
```bash
celery -A Api_banco beat -l info
celery -A Api_banco worker -l info --pool=solo
```

El proyecto estará disponible en:
> http://127.0.0.1:8000/