import time

def intro() -> None:
    print("Despiertas en una habitación oscura.")
    time.sleep(1)
    print("Sientes una brisa que viene del norte.")
    time.sleep(1)
    print("Hay una puerta al este.")

def elegir_camino() -> str:
    camino: str = ""
    while camino != "norte" and camino != "este":
        camino = input("¿Qué camino eliges? (norte/este) ")
    return camino

def explorar_camino(camino_elegido: str) -> None:
    print(f"\nDecides ir hacia el {camino_elegido}...")
    time.sleep(2)

    if camino_elegido == "norte":
        print("El viento te guía por un pasillo estrecho.")
        time.sleep(1)
        print("Llegas a un balcón y ves las estrellas. ¡Has escapado!")
    elif camino_elegido == "este":
        print("Abres la puerta y entras en una sala llena de tesoros.")
        time.sleep(1)
        print("¡Has encontrado la cámara del tesoro!")

def main() -> None:
    intro()
    decision: str = elegir_camino()
    explorar_camino(decision)
    print("\n--- FIN DEL JUEGO ---")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
