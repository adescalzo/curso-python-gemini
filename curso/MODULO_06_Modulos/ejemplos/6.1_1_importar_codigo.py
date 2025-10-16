# --- Opción 1: Importar el módulo completo ---
# Se importa el módulo como un "objeto" que contiene todas sus funciones y variables.
import mi_modulo

# Para usar algo del módulo, se usa la sintaxis: nombre_del_modulo.elemento
saludo_completo: str = mi_modulo.saludar("Mundo")
print(saludo_completo)

print(f"El valor de PI según mi_modulo es: {mi_modulo.PI}")

# --- Opción 2: Importar elementos específicos ---
# Se importan solo las funciones o variables que necesitamos.
from mi_modulo import sumar, PI

# Ahora podemos usar los elementos directamente por su nombre.
resultado: int = sumar(10, 5)
print(f"El resultado de la suma es: {resultado}")
print(f"El valor de PI importado directamente es: {PI}")

# --- Opción 3: Usar un alias ---
# Podemos darle un "apodo" (alias) a un módulo para que sea más corto o para evitar colisiones de nombres.
import mi_modulo as mm

resultado_alias: int = mm.sumar(100, 200)
print(f"Suma usando alias: {resultado_alias}")
