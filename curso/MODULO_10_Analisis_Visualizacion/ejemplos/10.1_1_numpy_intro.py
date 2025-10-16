import numpy as np
from typing import List

# --- Creación de un array de NumPy ---
# A partir de una lista de Python
lista_python: List[int] = [1, 2, 3, 4, 5]
array_np = np.array(lista_python)

print(f"Lista de Python: {lista_python}")
print(f"Array de NumPy: {array_np}")

# --- Operaciones vectorizadas ---
# Las operaciones se aplican a TODOS los elementos del array a la vez, sin necesidad de un bucle.

# Sumar 10 a cada elemento
array_sumado = array_np + 10
print(f"Array + 10: {array_sumado}")

# Multiplicar cada elemento por 2
array_multiplicado = array_np * 2
print(f"Array * 2: {array_multiplicado}")

# --- Ventajas de rendimiento ---
# NumPy es mucho más rápido para operaciones numéricas que las listas de Python.

# --- Atributos importantes ---
print(f"\nForma del array (shape): {array_np.shape}") # (5,) -> Es un vector de 5 elementos
print(f"Tipo de datos del array (dtype): {array_np.dtype}") # int64
