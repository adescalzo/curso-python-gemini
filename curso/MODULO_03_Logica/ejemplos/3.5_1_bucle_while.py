# --- Ejemplo 1: Contador simple ---
print("Iniciando contador con while:")
contador: int = 0
while contador < 5:
    print(f"El contador vale {contador}")
    contador += 1 # Abreviatura de contador = contador + 1

print("Contador finalizado.")

# --- Ejemplo 2: Menú interactivo ---
opcion: str = ""

while opcion != "salir":
    print("\n--- MENÚ ---")
    opcion = input("Escribe 'salir' para terminar: ")
    
    if opcion == "saludar":
        print("¡Hola!")
    elif opcion == "salir":
        print("Adiós.")
    else:
        print("Opción no reconocida.")

