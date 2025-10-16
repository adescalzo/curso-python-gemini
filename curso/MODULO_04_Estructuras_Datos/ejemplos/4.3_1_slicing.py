from typing import List

letras: List[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(f"Lista original: {letras}")

sub_lista: List[str] = letras[2:5]
print(f"letras[2:5] -> {sub_lista}")

primeros_tres: List[str] = letras[:3]
print(f"letras[:3] -> {primeros_tres}")

ultimos_cuatro: List[str] = letras[3:]
print(f"letras[3:] -> {ultimos_cuatro}")

pares: List[str] = letras[::2]
print(f"letras[::2] -> {pares}")

copia_independiente: List[str] = letras[:]
copia_independiente[0] = 'Z'

print(f"\nCopia modificada: {copia_independiente}")
print(f"Lista original (no ha cambiado): {letras}")
