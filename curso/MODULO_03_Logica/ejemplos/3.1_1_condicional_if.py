edad_str: str = input("¿Cuál es tu edad? ")
edad: int = int(edad_str)

if edad >= 18:
    print("Eres mayor de edad.")
    print("Puedes pasar.")

print("Esta línea se ejecuta siempre, sin importar la condición.")
