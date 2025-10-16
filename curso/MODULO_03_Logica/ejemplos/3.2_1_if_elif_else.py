nota_str: str = input("Introduce tu nota (0-10): ")
nota: float = float(nota_str)

if nota >= 9.0:
    print("Sobresaliente. ¡Felicidades!")
elif nota >= 7.0:
    print("Notable.")
elif nota >= 5.0:
    print("Aprobado.")
else:
    print("Suspendido.")

print("Fin del programa de calificación.")
