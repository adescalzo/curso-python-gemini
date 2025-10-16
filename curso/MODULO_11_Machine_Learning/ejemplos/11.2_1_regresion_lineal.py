import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# --- 1. Datos de ejemplo ---
# Imaginemos que tenemos datos de años de experiencia vs. salario (en miles)
# X debe ser un array 2D, por eso usamos .reshape(-1, 1)
anos_experiencia = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
salario = np.array([45, 50, 60, 65, 75, 80, 90, 95])

# --- 2. División de datos ---
# Dividimos los datos para entrenar y para probar
X_train, X_test, y_train, y_test = train_test_split(
    anos_experiencia, salario, test_size=0.2, random_state=42
)

# --- 3. Creación y Entrenamiento del Modelo ---
# Creamos una instancia del modelo de Regresión Lineal
modelo = LinearRegression()

# Entrenamos el modelo con los datos de entrenamiento
modelo.fit(X_train, y_train)

print("¡Modelo entrenado!")
print(f"La fórmula del modelo es: Salario = {modelo.coef_[0]:.2f} * Años + {modelo.intercept_:.2f}")

# --- 4. Realizar una Predicción ---
# ¿Cuál sería el salario para alguien con 10 años de experiencia?
anos_nuevos = np.array([[10]]) # Debe ser un array 2D

salario_predicho = modelo.predict(anos_nuevos)

print(f"\nPredicción para {anos_nuevos[0][0]} años de experiencia: ${salario_predicho[0]:.2f}k")

# --- 5. Evaluación (simple) ---
# Usamos los datos de prueba que el modelo no ha visto
puntuacion = modelo.score(X_test, y_test)
print(f"Puntuación del modelo (R^2): {puntuacion:.2f}")