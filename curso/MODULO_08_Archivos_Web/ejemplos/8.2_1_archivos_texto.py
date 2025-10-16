from typing import List

# --- Escribir en un archivo (modo 'w') ---
# El modo 'w' (write) crea el archivo si no existe.
# ¡CUIDADO! Si el archivo ya existe, SOBREESCRIBE todo su contenido.

# La construcción `with open(...)` es la forma recomendada de trabajar con archivos.
# Se encarga de cerrar el archivo automáticamente, incluso si ocurren errores.

with open("mi_archivo.txt", "w", encoding="utf-8") as f:
    f.write("Hola, mundo.\n")
    f.write("Esta es la segunda línea.\n")

print("Archivo 'mi_archivo.txt' creado y escrito.")

# --- Añadir a un archivo (modo 'a') ---
# El modo 'a' (append) añade contenido al FINAL del archivo sin borrar lo anterior.
with open("mi_archivo.txt", "a", encoding="utf-8") as f:
    f.write("Esta línea ha sido añadida.\n")

print("Contenido añadido al archivo.")

# --- Leer un archivo (modo 'r') ---
# El modo 'r' (read) es el modo por defecto.

print("\n--- Contenido completo del archivo ---")
with open("mi_archivo.txt", "r", encoding="utf-8") as f:
    contenido_completo: str = f.read()
    print(contenido_completo)

print("\n--- Leyendo el archivo línea por línea ---")
with open("mi_archivo.txt", "r", encoding="utf-8") as f:
    for linea in f:
        # .strip() elimina los saltos de línea y espacios extra al inicio/final
        print(linea.strip())
