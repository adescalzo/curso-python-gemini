# --- break: Rompe el bucle por completo ---
print("--- Ejemplo de break ---")
for numero in range(10):
    if numero == 5:
        print("Encontramos el 5. ¡Saliendo del bucle!")
        break # Termina el bucle for
    print(f"El número actual es {numero}")

print("El bucle ha terminado.")

# --- continue: Salta a la siguiente iteración ---
print("\n--- Ejemplo de continue ---")
for numero in range(10):
    if numero % 2 == 0: # Si el número es par
        continue
    
    print(f"Número impar encontrado: {numero}")

