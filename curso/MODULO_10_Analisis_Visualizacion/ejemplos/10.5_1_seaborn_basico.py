import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Seaborn se integra muy bien con Pandas.
# Usaremos el mismo DataFrame de la lección anterior.

try:
    df = pd.read_csv("ejemplos/datos_ventas.csv")

    # --- Gráfico de Barras con Seaborn ---
    # sns.barplot() es ideal para mostrar una métrica (eje y) por categoría (eje x).
    plt.figure(figsize=(8, 6))
    sns.barplot(x='Producto', y='Ventas', data=df, palette='viridis')
    
    plt.title("Ventas por Producto")
    plt.ylabel("Total de Ventas")
    plt.xlabel("Producto")
    
    # plt.show() sigue siendo necesario para mostrar el gráfico
    print("Mostrando gráfico de barras...")
    plt.show()

    # --- Gráfico de Dispersión (Scatter Plot) ---
    # sns.scatterplot() es perfecto para ver la relación entre dos variables numéricas.
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='Precio', y='Ventas', data=df, hue='Categoria', s=100) # s=100 hace los puntos más grandes

    plt.title("Relación entre Precio y Ventas")
    plt.xlabel("Precio del Producto")
    plt.ylabel("Unidades Vendidas")

    print("Mostrando gráfico de dispersión...")
    plt.show()

except FileNotFoundError:
    print("Error: El archivo 'datos_ventas.csv' no se encontró.")
