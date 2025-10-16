from typing import List, Any

numeros: List[int] = [1, 2, 3, 4, 5]
print(f"Lista de números: {numeros}")

frutas: List[str] = ["manzana", "banana", "cereza"]
print(f"Lista de frutas: {frutas}")

mixta: List[Any] = ["texto", 100, 3.14, True]
print(f"Lista mixta: {mixta}")

primera_fruta: str = frutas[0]
print(f"La primera fruta es: {primera_fruta}")

ultima_fruta: str = frutas[-1]
print(f"La última fruta es: {ultima_fruta}")
