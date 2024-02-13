#Version 1.0.0 - Desarrollado por PrograMEX.
#Feliz Día de San Valentín para TODOS.
#Usen este código con Responsabilidad.
import turtle
import time

def escribir_mex():
    writer = turtle.Turtle()
    writer.hideturtle()  # Ocultar la tortuga para que no se vea, solo queremos el texto
    writer.penup()  # Levantar el "lápiz" para no dibujar una línea al moverse
    writer.goto(0, 0)  # Mover la tortuga al centro de la pantalla
    writer.color("white")  # Establecer el color del texto
    writer.write("MEX", align="center", font=("Courier", 5, "bold"))
    writer.penup()  # Asegurar que la tortuga no dibuje al moverse después

# Configuración inicial de Turtle para la primera parte
wn = turtle.Screen()
wn.title("Dia de San Valentín-PrograMex")
wn.bgcolor("#ba161e")  # Color de fondo inicial para Iron Man

escribir_mex()
# Función para dibujar las piezas de Iron Man
def dibujar_iron_man(t):
    x_offset, y_offset = 0, 120
    zoom_factor = 15

    pieces = [
        [[0, -2, -3.5, -6.5, -8.5, -8.5, -8.0, -8.5, -7.5, -7.0, -2.0, 0],
         [0, 0, 7, 5.5, 4, -1, -4, -5.5, -6.5, -5.5, -7.0, -7.0]],

        [[0, -2.0, -2.5, -5.0, -6.5, -8.8, -9.3, -9.3, -6.0, -5.5, -4.0, -3.2, 0],
         [-7.5, -7.5, -8.0, -8.3, -8.0, -6.0, -7.5, -8.0, -14.5, -16.5, -17.5, -16.5, -16.5]],

        [[0, -3.0, -4.0, -5.5, -6.0, -4.5, -3.0, -1.5, -1.0, 0],
         [-17.0, -17.0, -18.0, -17.0, -18.5, -20.0, -19.0, -19.0, -18.5, -18.5]]
    ]

    for piece in pieces:
        t.penup()
        t.goto(piece[0][0] * zoom_factor + x_offset, piece[1][0] * zoom_factor + y_offset)
        t.pendown()
        t.color('#fab104')  # Light Yellow
        t.begin_fill()
        for i in range(1, len(piece[0])):
            x, y = piece[0][i] * zoom_factor + x_offset, piece[1][i] * zoom_factor + y_offset
            t.goto(x, y)
        for i in range(len(piece[0])-1, -1, -1):
            x, y = piece[0][i] * zoom_factor * -1 + x_offset, piece[1][i] * zoom_factor + y_offset
            t.goto(x, y)
        t.end_fill()

# Función para preparar la escena para el contador y el corazón
def preparar_escena():
    wn.bgcolor("black")  # Cambio de color de fondo para el contador y mensaje
    global contador
    contador = turtle.Turtle()
    contador.color("white")
    contador.penup()
    contador.hideturtle()

# Función para dibujar un corazón
def dibujar_corazon():
    corazon = turtle.Turtle()
    corazon.color("red")
    corazon.begin_fill()
    corazon.fillcolor("red")
    corazon.penup()
    corazon.goto(0, -100)
    corazon.pendown()
    corazon.left(140)
    corazon.forward(179)
    corazon.circle(-90, 200)
    corazon.setheading(60)
    corazon.circle(-90, 200)
    corazon.forward(179)
    corazon.end_fill()
    corazon.hideturtle()
#PROGRAMEX
    
# Función para ajustar la fuente según el tamaño de la ventana
def ajustar_fuente():
    ancho_ventana, alto_ventana = wn.window_width(), wn.window_height()
    # Ajustar el tamaño de la fuente y las posiciones basadas en el tamaño de la ventana
    if ancho_ventana < 600:  # Considerado como dispositivo móvil
        tamaño_fuente = 24
        posición_contador = -30
        posición_mensaje = -150
    else:  # Considerado como dispositivo de escritorio
        tamaño_fuente = 80
        posición_contador = -10
        posición_mensaje = -180
    return tamaño_fuente, posición_contador, posición_mensaje
# Función para mostrar el contador y el mensaje
def mostrar_contador_y_mensaje(t):
    preparar_escena()
    dibujar_corazon()
    t.clear()  # Borra el dibujo de Iron Man justo antes de iniciar el contador

    tamaño_fuente, posición_contador, posición_mensaje = ajustar_fuente()

    # Mostrar el contador
    contador.goto(0, posición_contador)
    for numero in range(3, -1, -1):
        contador.clear()
        contador.write(numero, align="center", font=("Courier", tamaño_fuente, "bold"))
        time.sleep(1)

    # Mostrar el mensaje final
    contador.goto(0, posición_mensaje)
    contador.write("¡I LOVE YOU!", align="center", font=("Courier", tamaño_fuente//2, "bold"))
    time.sleep(2)
    contador.clear()


    # Preparar para el nuevo dibujo
    t.reset()
    escribir_mex()
    dibujar_nuevo_diseno()

def dibujar_nuevo_diseno():
    turtle.speed(13) 
    turtle.bgcolor("#990000")
    turtle.pensize(10)
    turtle.penup()
    turtle.goto(0,50)
    turtle.pendown()
    turtle.circle(-120)
    turtle.penup()
    turtle.circle(-120,-60)
    turtle.pendown()
    turtle.pensize(5)
    turtle.right(50)
    turtle.circle(70,55)
    turtle.right(85)
    turtle.circle(75,58)
    turtle.right(90)
    turtle.circle(70,55)
    turtle.right(90)
    turtle.circle(70,58)

    #RAYAS
    turtle.penup()
    turtle.pensize(10)
    turtle.goto(80,15)
    turtle.pendown()
    turtle.seth(92)
    turtle.fd(135)
    turtle.seth(125)
    turtle.circle(30,135)
    turtle.seth(190)
    turtle.fd(50)
    turtle.seth(125)
    turtle.circle(30,135)
    turtle.seth(275)
    turtle.fd(90)

    #CABEZA
    turtle.penup()
    turtle.pensize(10)
    turtle.goto(92,-150)
    turtle.seth(240)
    turtle.pendown()
    turtle.fd(80)
    turtle.left(10)
    turtle.circle(-28,185)


#PROGRAMEX
    #PIERNAS
    turtle.penup()
    turtle.goto(0,50)
    turtle.seth(0)
    turtle.pensize(10)
    turtle.circle(-120,-60)
    turtle.seth(200)
    turtle.pendown()
    turtle.fd(72)
    turtle.left(20)
    turtle.circle(30,150)
    turtle.left(20)
    turtle.fd(20)
    turtle.right(15)
    turtle.fd(10)
    turtle.pensize(5)
    turtle.fillcolor("#3366cc")
    turtle.begin_fill()
    turtle.seth(92)
    turtle.circle(-120,31)
    turtle.seth(200)
    turtle.fd(45)
    turtle.left(90)
    turtle.fd(52)
    turtle.end_fill()
    turtle.fd(-12)
    turtle.right(90)
    turtle.fd(40)
    turtle.penup()
    turtle.right(90)
    turtle.fd(18)
    turtle.pendown()
    turtle.right(86)
    turtle.fd(40)
    turtle.penup()
    turtle.goto(-152,-86)
    turtle.pendown()
    turtle.left(40)
    turtle.circle(35,90)

    #BRAZOS
    turtle.penup()
    turtle.goto(-80,116)
    turtle.seth(10)
    turtle.pensize(5)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("#3366cc")
    turtle.fd(155)
    turtle.seth(-88)
    turtle.fd(37)
    turtle.seth(195)
    turtle.fd(156)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-75,38)
    turtle.seth(15)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fd(158)
    turtle.seth(-88)
    turtle.fd(55)
    turtle.seth(140)
    turtle.circle(120,78)
    turtle.end_fill()


#PROGRAMEX

    #CUERPO
    turtle.penup()
    turtle.fillcolor("#3366cc")
    turtle.pensize(5)
    turtle.goto(75,-170)
    turtle.pendown()
    turtle.begin_fill()
    turtle.seth(240)
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(17)
    turtle.end_fill()
    turtle.fd(10)
    turtle.left(80)
    turtle.fd(55)
    turtle.penup()
    turtle.left(90)
    turtle.fd(15)
    turtle.pendown()
    turtle.left(85)
    turtle.fd(55)
    turtle.penup()
    turtle.goto(43,-225)
    turtle.left(84)
    turtle.pendown()
    turtle.circle(60,51)

    turtle.speed(0)
   

    for i in range(3):
        turtle.penup()
        turtle.goto(-70+i*15,135)
        turtle.seth(-90)
        turtle.pendown()
        turtle.pensize(5)
        turtle.fd(15-2*i)
    for i in range(3):
        turtle.penup()
        turtle.goto(36 + i * 15, 156)
        turtle.seth(-90)
        turtle.pendown()
        turtle.pensize(5)
        turtle.fd(15 - 2 * i)

        a = -60
        b = 70
    for i in range(4):
        turtle.penup()
        turtle.goto(a,b)
        a=a+40
        b=b+10
        turtle.seth(-90)
        turtle.pendown()
        turtle.pensize(5)
        turtle.fd(26)


    def oo (li,jing):
        turtle.penup()
        turtle.goto(0,50)
        turtle.seth(0)
        turtle.circle(-120, li)
        turtle.pendown()
        turtle.right(jing)
#PROGRAMEX
    turtle.pensize(5)
    oo(-60,110)
    turtle.fd(130)
    oo(-28,96)
    turtle.fd(140)
    oo(9,89)
    turtle.fd(144)
    oo(42,70)
    turtle.fd(160)
    oo(80,60)
    turtle.fd(130)

    turtle.penup()
    turtle.goto(-80,-40)
    turtle.right(160)
    turtle.pendown()
    turtle.right(50)
    turtle.circle(70,45)
    turtle.right(75)
    turtle.circle(70,38)
    turtle.right(50)
    turtle.circle(70,45)
    turtle.right(90)
    turtle.circle(70,48)

    turtle.penup()
    turtle.goto(-53,-70)
    turtle.pendown()
    turtle.left(40)
    turtle.circle(70,30)
    turtle.right(50)
    turtle.circle(70,20)
    turtle.right(50)
    turtle.circle(70,38)
    turtle.right(70)
    turtle.circle(70,24)

    turtle.penup()
    turtle.goto(-19,-105)
    turtle.left(72)
    turtle.pendown()
    turtle.fd(22)
    turtle.right(60)
    turtle.fd(22)

    oo(-140,80)
    turtle.circle(-90,120)

    turtle.penup()
    oo(140,100)
    turtle.circle(90,13)
    turtle.pendown()
    turtle.right(-50)
    turtle.circle(70,45)
    turtle.right(75)
    turtle.circle(70,38)
    turtle.right(50)
    turtle.circle(70,36)

    turtle.penup()
    turtle.goto(22,-185)
    turtle.right(70)
    turtle.pendown()
    turtle.fd(72)

    turtle.penup()
    turtle.goto(-40,-182)
    turtle.right(38)
    turtle.pendown()
    turtle.fd(70)




    turtle.speed(10)

    #OJO IZQUIERDO
    turtle.penup()
    turtle.pensize(7)
    turtle.goto(-15,-110)
    turtle.seth(0)
    turtle.pendown()
    turtle.pensize(10)
    turtle.begin_fill()
    turtle.left(130)
    turtle.fd(110)
    turtle.right(250)
    turtle.circle(90,60)
    turtle.circle(40,120)
    turtle.fillcolor("#F5FFFA")
    turtle.end_fill()
    #OJO DERECHO
    turtle.penup()
    turtle.goto(5,-110)
    turtle.pendown()
    turtle.begin_fill()
    turtle.right(30)
    turtle.fd(110)
    turtle.right(-250)
    turtle.circle(-90,60)
    turtle.circle(-40,120)
    turtle.end_fill()


def draw_shape(some_turtle, radius):
    some_turtle.circle(radius, 60)
    some_turtle.left(120)
    some_turtle.circle(radius, 60)

def draw_flower():
    # Ajustar la posición inicial de la tortuga para dibujar la flor en la esquina inferior izquierda
    # Establecemos la posición inicial de la tortuga `petal` antes de comenzar a dibujar
    petal = turtle.Turtle()
    petal.penup()  # Levantar el lápiz para no dibujar mientras se mueve a la posición inicial
    petal.goto(-wn.window_width() / 2 + 140, -wn.window_height() / 2 + 120)  # Ajusta estos valores según necesites # Posición en la esquina inferior izquierda
    petal.pendown()  # Bajar el lápiz para empezar a dibujar
    petal.shape("turtle")
    petal.color("white")
    petal.speed(15)
    petal.width(2)

    the_petals = 15
    the_radius = 150

    for _ in range(the_petals):
        draw_shape(petal, the_radius)
        petal.left(360 / the_petals)

    
# Ejecución principal
wn = turtle.Screen()  # Mover la creación de la ventana fuera de draw_flower
wn.bgcolor("#ba161e")  # Esto establece el color de fondo inicial. Ajusta según necesidad.

t = turtle.Turtle()
t.hideturtle()
t.speed(3)
escribir_mex()
dibujar_iron_man(t)
escribir_mex()
mostrar_contador_y_mensaje(t)
escribir_mex()

# Ajustar la posición inicial según sea necesario antes de dibujar la flor

draw_flower()  # Llamada a la función para dibujar la flor después del contador y mensaje


# Cerrar la ventana de Turtle al finalizar
turtle.done()

#Espero les guste :)
