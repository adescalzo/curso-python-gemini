import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from typing import List

url: str = "https://example.com"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    # 1. Crear un objeto BeautifulSoup a partir del contenido HTML
    # El segundo argumento, 'html.parser', es el analizador que usará.
    soup = BeautifulSoup(response.text, 'html.parser')

    # 2. Encontrar elementos por su etiqueta
    
    # .find() devuelve la PRIMERA etiqueta que coincide
    titulo_tag: Tag | None = soup.find('h1')
    if titulo_tag:
        # .get_text() extrae solo el texto de dentro de la etiqueta
        titulo: str = titulo_tag.get_text()
        print(f"El título H1 de la página es: '{titulo}'")

    parrafo_tag: Tag | None = soup.find('p')
    if parrafo_tag:
        parrafo: str = parrafo_tag.get_text()
        print(f"El primer párrafo dice: '{parrafo}'")

    # .find_all() devuelve una LISTA con TODAS las etiquetas que coinciden
    enlaces_tags: List[Tag] = soup.find_all('a')
    print(f"\nSe encontraron {len(enlaces_tags)} enlaces en la página.")

    for enlace_tag in enlaces_tags:
        # Podemos acceder a los atributos de una etiqueta como si fuera un diccionario
        url_enlace: str = enlace_tag['href']
        print(f"- Enlace encontrado: {url_enlace}")

except requests.exceptions.RequestException as e:
    print(f"Ocurrió un error al hacer la petición: {e}")
