import pandas as pd
from typing import List

# --- La Serie de Pandas ---
# Una Serie es como un array de NumPy pero con etiquetas (índices).
# Se puede crear a partir de una lista.

datos_serie: List[int] = [10, 20, 30, 40]
indices_serie: List[str] = ['a', 'b', 'c', 'd']

serie = pd.Series(data=datos_serie, index=indices_serie)

print("--- Serie de Pandas ---")
print(serie)
print(f"Valor en el índice 'c': {serie['c']}")

# --- El DataFrame de Pandas ---
# Un DataFrame es una tabla de 2 dimensiones, como una hoja de cálculo o una tabla de SQL.
# Se puede crear a partir de un diccionario de listas.

datos_df = {
    'Nombre': ['Ana', 'Luis', 'Marta', 'Juan'],
    'Edad': [28, 34, 29, 42],
    'Ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Valencia']
}

df = pd.DataFrame(datos_df)

print("\n--- DataFrame de Pandas ---")
print(df)

# --- Acceder a columnas ---
# Se puede acceder a una columna por su nombre, y devuelve una Serie.
print("\n--- Columna 'Edad' ---")
print(df['Edad'])
