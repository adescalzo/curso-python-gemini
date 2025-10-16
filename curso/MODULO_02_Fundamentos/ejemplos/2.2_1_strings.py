# --- Concatenación ---
nombre = "Ada"
apellido = "Lovelace"
nombre_completo = nombre + " " + apellido
print("Concatenación:", nombre_completo)

# --- f-strings (recomendado) ---
nombre_completo_fstring = f"El nombre es: {nombre} {apellido}"
print("f-string:", nombre_completo_fstring)

# --- Métodos de String ---
frase = "  Python es Genial  "
print("Mayúsculas:", frase.upper())
print("Minúsculas:", frase.lower())
print("Sin espacios:", frase.strip())
