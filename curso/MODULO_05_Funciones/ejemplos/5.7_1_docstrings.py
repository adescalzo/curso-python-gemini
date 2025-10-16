def calcular_area_rectangulo(base: float, altura: float) -> float:
    """Calcula el área de un rectángulo.

    Args:
        base (float): La longitud de la base del rectángulo.
        altura (float): La altura del rectángulo.

    Returns:
        float: El área calculada del rectángulo. Devuelve 0 si los valores son negativos.
    """
    if base < 0 or altura < 0:
        return 0.0
    return base * altura

print("--- Docstring de la función ---")
print(calcular_area_rectangulo.__doc__)

area: float = calcular_area_rectangulo(10.0, 5.0)
print(f"\nEl área es: {area}")

