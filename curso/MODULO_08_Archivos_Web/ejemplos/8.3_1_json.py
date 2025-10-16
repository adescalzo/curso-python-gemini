import json
from typing import Dict, Any

# Imagina que tenemos un diccionario de Python
datos_python: Dict[str, Any] = {
    "nombre": "Ada Lovelace",
    "edad": 25,
    "es_estudiante": True,
    "cursos": ["Python", "Álgebra"]
}

# --- Escribir JSON en un archivo (Serialización) ---
# Convertimos el objeto de Python a un string con formato JSON y lo guardamos.

with open("datos.json", "w", encoding="utf-8") as f:
    # json.dump() escribe el objeto directamente en el fichero.
    # `indent=4` hace que el archivo JSON sea legible para los humanos.
    json.dump(datos_python, f, indent=4)

print("El archivo 'datos.json' ha sido creado.")

# --- Leer JSON de un archivo (Deserialización) ---
# Leemos el archivo JSON y lo convertimos de vuelta a un objeto de Python.

with open("datos.json", "r", encoding="utf-8") as f:
    # json.load() lee el fichero y lo convierte en un objeto de Python (un diccionario).
    datos_leidos: Dict[str, Any] = json.load(f)

print("\n--- Datos leídos del archivo JSON ---")
print(datos_leidos)

# Ahora podemos trabajar con los datos como un diccionario normal de Python
print(f"\nNombre: {datos_leidos['nombre']}")
print(f"Primer curso: {datos_leidos['cursos'][0]}")
