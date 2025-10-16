from typing import List

# --- Forma tradicional de crear una lista de cuadrados ---
numeros: List[int] = [1, 2, 3, 4, 5]
cuadrados_tradicional: List[int] = []
for numero in numeros:
    cuadrados_tradicional.append(numero ** 2)

print(f"Lista de cuadrados (tradicional): {cuadrados_tradicional}")

# --- Usando List Comprehension ---
# Sintaxis: [expresion for elemento in iterable]
cuadrados_comprehension: List[int] = [numero ** 2 for numero in numeros]

print(f"Lista de cuadrados (comprehension): {cuadrados_comprehension}")

# --- List Comprehension con condición ---
# Sintaxis: [expresion for elemento in iterable if condicion]

# Crear una lista solo con los números pares
pares: List[int] = [numero for numero in numeros if numero % 2 == 0]

print(f"Números pares de la lista original: {pares}")

# Crear una lista de frutas que empiezan con "m"
frutas: List[str] = ["manzana", "banana", "mango", "cereza"]
frutas_con_m: List[str] = [fruta for fruta in frutas if fruta.startswith("m")]

print(f"Frutas que empiezan con 'm': {frutas_con_m}")
