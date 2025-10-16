def describir_persona(nombre: str, edad: int, ciudad: str) -> None:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")

print("--- 1. Argumentos Posicionales ---")
describir_persona("Ana", 30, "Barcelona")

print("\n--- 2. Argumentos Nominales (Keyword) ---")
describir_persona(edad=45, ciudad="Madrid", nombre="Carlos")

def saludar(nombre: str, saludo: str = "Hola") -> None:
    print(f"{saludo}, {nombre}!")

print("\n--- 3. Valores por Defecto ---")
saludar("Elena")
saludar("Elena", saludo="Buenos días")
