from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# --- 1. Carga de Datos ---
# El dataset Iris es un conjunto de datos clásico incluido en scikit-learn.
# Contiene medidas de 3 especies de flores Iris.
iris = load_iris()
X = iris.data # Características (largo/ancho de sépalos/pétalos)
y = iris.target # Etiquetas (la especie de flor: 0, 1 o 2)

# --- 2. División de datos ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# --- 3. Creación y Entrenamiento del Modelo ---
# Usaremos el clasificador "K-Nearest Neighbors" (Vecinos más cercanos).
# n_neighbors=3 significa que mirará a sus 3 vecinos más cercanos para decidir.
modelo = KNeighborsClassifier(n_neighbors=3)

modelo.fit(X_train, y_train)
print("¡Modelo de clasificación entrenado!")

# --- 4. Realizar Predicciones ---
# Usamos los datos de prueba que el modelo no ha visto.
predicciones = modelo.predict(X_test)

print("\n--- Comparando predicciones y etiquetas reales (primeros 5) ---")
print(f"Predicciones: {predicciones[:5]}")
print(f"Reales:       {y_test[:5]}")

# --- 5. Evaluación ---
# Para clasificación, una métrica común es la "accuracy" (precisión).
# ¿Qué porcentaje de las predicciones fueron correctas?
precision = accuracy_score(y_test, predicciones)

print(f"\nLa precisión del modelo es: {precision:.2f} ({precision:.0%})")
