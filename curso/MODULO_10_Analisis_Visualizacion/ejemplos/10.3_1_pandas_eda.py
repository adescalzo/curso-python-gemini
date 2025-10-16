import pandas as pd

# --- Cargar datos desde un archivo CSV ---
# La función pd.read_csv() es una de las más usadas en pandas.
# Convierte un archivo CSV en un DataFrame.
try:
    df = pd.read_csv("ejemplos/datos_ventas.csv")

    # --- Exploración de Datos Inicial (EDA) ---
    print("--- Primeras 5 filas del DataFrame con .head() ---")
    print(df.head())

    print("\n--- Información general del DataFrame con .info() ---")
    # .info() nos da un resumen: número de filas, columnas, tipos de datos y memoria usada.
    df.info()

    print("\n--- Resumen estadístico con .describe() ---")
    # .describe() calcula estadísticas descriptivas para las columnas numéricas.
    print(df.describe())

    # --- Selección y Filtrado ---
    print("\n--- Selección de la columna 'Producto' ---")
    print(df["Producto"])

    print("\n--- Filtrado: productos con ventas > 150 ---")
    filtro_ventas = df[df["Ventas"] > 150]
    print(filtro_ventas)

except FileNotFoundError:
    print("Error: El archivo 'datos_ventas.csv' no se encontró.")
    print("Asegúrate de que el archivo está en la carpeta 'ejemplos'.")
