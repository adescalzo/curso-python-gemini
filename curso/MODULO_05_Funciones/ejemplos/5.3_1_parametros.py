def saludar(nombre: str) -> None:
    """Recibe un nombre y muestra un saludo personalizado."""
    print(f"¡Hola, {nombre}! Qué buen día.")

saludar("Ana")
saludar("Luis")

def describir_mascota(tipo_animal: str, nombre_mascota: str) -> None:
    """Muestra información sobre una mascota."""
    print(f"\nTengo un {tipo_animal}.")
    print(f"Mi {tipo_animal} se llama {nombre_mascota.title()}.")

describir_mascota("perro", "fido")
describir_mascota(tipo_animal="gato", nombre_mascota="bigotes")

