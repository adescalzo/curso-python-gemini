# input() siempre devuelve un string.
anio_nacimiento_str = input("¿En qué año naciste? ")

# Usamos int() para convertir el string a un número entero.
anio_nacimiento_int = int(anio_nacimiento_str)

edad_aprox = 2025 - anio_nacimiento_int

print(f"En 2025, tendrás aproximadamente {edad_aprox} años.")
