import matplotlib.pyplot as plt
from typing import List

# --- Datos para el gráfico ---
meses: List[str] = ['Ene', 'Feb', 'Mar', 'Abr', 'May']
ventas: List[int] = [150, 170, 160, 180, 190]

# --- Creación del Gráfico ---

# plt.figure() crea una "figura" o lienzo para nuestro gráfico.
# figsize especifica el ancho y alto en pulgadas.
plt.figure(figsize=(8, 5))

# plt.plot() crea el gráfico de líneas.
# El primer argumento es el eje X, el segundo es el eje Y.
plt.plot(meses, ventas, marker='o') # marker='o' dibuja círculos en los puntos de datos

# --- Añadir Títulos y Etiquetas ---
plt.title("Ventas Mensuales")
plt.xlabel("Mes")
plt.ylabel("Ventas (en unidades)")

# --- Mostrar el Gráfico ---
# plt.grid(True) añade una cuadrícula al fondo para facilitar la lectura.
plt.grid(True)

# plt.show() abre una ventana y muestra el gráfico.
# La ejecución del script se pausa hasta que se cierra la ventana.
plt.show()
