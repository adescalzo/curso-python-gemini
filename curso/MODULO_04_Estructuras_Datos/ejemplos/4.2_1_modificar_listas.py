from typing import List

frutas: List[str] = ["manzana", "banana", "cereza"]
print(f"Lista inicial: {frutas}")

frutas[1] = "mango"
print(f"Después de cambiar: {frutas}")

frutas.append("naranja")
print(f"Después de append: {frutas}")

frutas.insert(1, "uva")
print(f"Después de insert: {frutas}")

fruta_eliminada: str = frutas.pop()
print(f"Se eliminó: {fruta_eliminada}")
print(f"Lista después de pop: {frutas}")

frutas.remove("manzana")
print(f"Después de remove('manzana'): {frutas}")

del frutas[0]
print(f"Después de del[0]: {frutas}")
