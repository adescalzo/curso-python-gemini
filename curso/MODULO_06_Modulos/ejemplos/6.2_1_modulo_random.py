import random
from typing import List

# --- random.randint(a, b) ---
# Devuelve un número entero aleatorio entre a y b (ambos incluidos).
numero_aleatorio: int = random.randint(1, 10)
print(f"Número aleatorio entre 1 y 10: {numero_aleatorio}")

# --- random.choice(secuencia) ---
# Devuelve un elemento aleatorio de una secuencia (como una lista).
frutas: List[str] = ["manzana", "banana", "cereza", "naranja"]
fruta_elegida: str = random.choice(frutas)
print(f"Fruta elegida al azar: {fruta_elegida}")

# --- random.shuffle(lista) ---
# Mezcla los elementos de una lista "in-place" (modifica la lista original).
# No devuelve nada (devuelve None).
print(f"\nLista de frutas original: {frutas}")
random.shuffle(frutas)
print(f"Lista de frutas mezclada: {frutas}")
