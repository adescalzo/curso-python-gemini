import turtle

# --- Configuración inicial ---
# Crear una "pantalla" donde la tortuga dibujará
wn = turtle.Screen()
wn.title("Mi Primer Dibujo con Turtle")
wn.bgcolor("lightblue")

# Crear un objeto "tortuga"
mi_tortuga = turtle.Turtle()
mi_tortuga.shape("turtle")
mi_tortuga.color("green")

# --- Dibujando un cuadrado ---

# Levantar el lápiz para mover la tortuga sin dibujar
mi_tortuga.penup()
mi_tortuga.goto(-50, 50)

# Bajar el lápiz para empezar a dibujar
mi_tortuga.pendown()

mi_tortuga.speed(3) # Velocidad de dibujo (1=lento, 10=rápido, 0=instantáneo)

for _ in range(4):
    mi_tortuga.forward(100) # Moverse hacia adelante 100 píxeles
    mi_tortuga.right(90)    # Girar a la derecha 90 grados

# --- Fin del dibujo ---
# Ocultar la tortuga al final
mi_tortuga.hideturtle()

# Mantener la ventana abierta hasta que se haga clic
wn.exitonclick()
