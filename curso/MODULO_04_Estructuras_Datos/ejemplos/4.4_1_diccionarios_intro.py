from typing import Dict, Any, List

alumno: Dict[str, Any] = {
    "nombre": "Ada Lovelace",
    "edad": 25,
    "es_estudiante_activo": True,
    "calificaciones": [10, 9, 10]
}

print(f"Diccionario completo: {alumno}")

nombre_alumno: str = alumno["nombre"]
print(f"\nEl nombre del alumno es: {nombre_alumno}")

alumno["ciudad"] = "Londres"
print(f"\nDiccionario con ciudad: {alumno}")

alumno["edad"] = 26
print(f"\nDiccionario con edad modificada: {alumno}")

