from typing import Tuple

def sumar(a: int, b: int) -> int:
    """Recibe dos números y devuelve su suma."""
    return a + b

valor_suma: int = sumar(5, 3)
print(f"El resultado es: {valor_suma}")

def obtener_coordenadas() -> Tuple[int, int]:
    """Devuelve una tupla con coordenadas X e Y."""
    return (10, 20)

x, y = obtener_coordenadas()
print(f"\nCoordenada X: {x}, Coordenada Y: {y}")
")