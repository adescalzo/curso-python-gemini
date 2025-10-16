from typing import List, Dict, Any

frutas: List[str] = ["manzana", "banana", "cereza"]
alumno: Dict[str, Any] = {
    "nombre": "Ada Lovelace",
    "edad": 25,
    "curso": "Python"
}

print("--- Mis Frutas ---")
for fruta in frutas:
    print(fruta.title())

print("\n--- Claves del Alumno ---")
for clave in alumno:
    print(clave)

print("\n--- Valores del Alumno ---")
for valor in alumno.values():
    print(valor)

print("\n--- Ficha Completa del Alumno ---")
for clave, valor in alumno.items():
    print(f"{clave.title()}: {valor}")

