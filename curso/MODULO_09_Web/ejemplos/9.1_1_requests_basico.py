import requests
from requests.models import Response

# La URL de la página que queremos descargar
url: str = "https://example.com"

try:
    # Hacemos la petición GET a la URL
    # El argumento `timeout` es importante para no esperar indefinidamente
    response: Response = requests.get(url, timeout=10)

    # response.raise_for_status() lanzará un error si la petición falló (ej: 404, 500)
    response.raise_for_status()

    # Si todo fue bien, el contenido HTML está en response.text
    print(f"Petición a {url} exitosa (Código de estado: {response.status_code})")
    print("\n--- COMIENZO DEL CONTENIDO HTML ---")
    print(response.text)
    print("--- FIN DEL CONTENIDO HTML ---")

except requests.exceptions.RequestException as e:
    print(f"Ocurrió un error al hacer la petición: {e}")
