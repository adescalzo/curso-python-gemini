import math

# --- Constantes del módulo ---
# math.pi contiene una aproximación de alta precisión de Pi.
print(f"El valor de Pi es aproximadamente: {math.pi}")

# --- Funciones comunes ---

# math.sqrt(x) -> Calcula la raíz cuadrada.
raiz_de_16: float = math.sqrt(16)
print(f"La raíz cuadrada de 16 es: {raiz_de_16}")

# math.pow(x, y) -> Calcula x elevado a la potencia y.
potencia: float = math.pow(2, 3)
print(f"2 elevado a 3 es: {potencia}")

# math.ceil(x) -> Redondea un número HACIA ARRIBA al entero más cercano.
redondeo_arriba: int = math.ceil(9.2)
print(f"Redondeo hacia arriba de 9.2: {redondeo_arriba}")

# math.floor(x) -> Redondea un número HACIA ABAJO al entero más cercano.
redondeo_abajo: int = math.floor(9.8)
print(f"Redondeo hacia abajo de 9.8: {redondeo_abajo}")
