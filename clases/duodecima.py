
"""
Comandos cubiertos
turtle.forward(pixeles)
    turtle.fd(pixeles)
turtle.backward(pixeles)
    turtle.bk(pixeles)
turtle.left(angulo)
    turtle.lt(angulo)
turtle.right(angulo)
    turtle.rt(angulo)
turtle.up()
turtle.down()
turtle.goto(x, y)
"""

import turtle as t

def escalon(altura, inclinacion):
    t.forward(altura)
    t.left(inclinacion)
    t.forward(altura)
    t.right(inclinacion)

def esca(alt):
    t.left(90)
    t.forward(alt)
    t.right(90)
    t.forward(alt)

def escalonado(altura, inclinacion):
    t.forward(altura)
    t.left(inclinacion)
    t.forward(altura)
    t.right(inclinacion)
    t.forward(altura)


def escalera(escalones):
    for i in range(escalones):
        esca(40)

def adeiz(longitud, angulo):
    t.forward(longitud)
    t.left(angulo)

def cuadrado(lado):
    for i in range(4):
        adeiz(lado, 90)

def co(lado):
    t.forward(lado)
    t.left(90)
    t.forward(lado)
    t.left(90)
    t.forward(lado)
    t.left(90)
    t.forward(lado)
    t.left(90)

def cdo(lado):
    for i in range(4):
        adeiz(lado, 90)

def triangulo(lado):
    for i in range(3):
        adeiz(lado, 120)

def poligono(lados, longitud):
    for i in range(lados):
        adeiz(longitud, 360/lados)

def isoceles(longitud, angulo):
    angulos = [angulo, 180 - 2*angulo, angulo]
    for a in angulos:
        adeiz(longitud, 180 - a)
