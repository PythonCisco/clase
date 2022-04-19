
"""
"""

import turtle

class Pluma():
    def __init__(self, color, grosor):
        self.color = color
        self.grosor = grosor
        self.posicion = [0, 0]
        self.previa = self.posicion

    def mueve(self, x, y):
        self.previa = self.posicion
        self.posicion = [x, y]
        turtle.goto(*self.posicion)

    def regresa(self):
        self.posicion, self.previa = self.previa, self.posicion
        turtle.goto(*self.posicion)

# añade a la clase Pluma una función llamada 'regresa' que mueva la pluma a su previa posición
