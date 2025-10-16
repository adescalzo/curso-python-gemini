import requests
from typing import List, Dict, Any

# JSONPlaceholder es una API pública y gratuita para pruebas.
# Este endpoint devuelve una lista de 200 "to-dos".
url: str = "https://jsonplaceholder.typicode.com/todos"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status() # Lanza un error si la petición falla

    # .json() es un método de la librería requests que deserializa
    # automáticamente la respuesta JSON a un objeto de Python (en este caso, una lista de diccionarios).
    todos: List[Dict[str, Any]] = response.json()

    print(f"Se han obtenido {len(todos)} tareas.")

    # --- Procesamos los datos ---
    # Imprimimos las primeras 5 tareas y si están completadas o no.
    print("\n--- Primeras 5 Tareas ---")
    for tarea in todos[:5]:
        titulo: str = tarea['title']
        completada: bool = tarea['completed']
        
        estado: str = "Completada" if completada else "Pendiente"
        print(f"- Título: {titulo} (Estado: {estado})")

except requests.exceptions.RequestException as e:
    print(f"Ocurrió un error al conectar con la API: {e}")
")