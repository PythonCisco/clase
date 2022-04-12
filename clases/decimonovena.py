
"""
sintaxis de objetos y objetos incrementadores
objeto como la instancia de una clase

que es un objeto
que es ser una instancia
que es una clase
como todo es distinto uno de otro
constructor de objeto
"""

class Contador():
    todos = 0

    def __init__(self, empieza, fin):
        self.corriente = empieza
        self.fin = fin
    def inc(self, salto=1):
        self.corriente += salto
    def terminado(self):
        return self.corriente == self.fin
    def valor(self):
        return self.corriente

    def juntos(self, salto):
        Contador.todos += salto
    def valor_todos(self):
        return Contador.todos

class ContadorAlfabeto():

    def __init__(self, empieza, fin):
        self.lista = "abcdefghijklmnopqrstuvwxyz"
        self.corriente = self.lista.index(empieza)
        self.fin = fin
    def inc(self, salto=1):
        self.corriente += salto
    def terminado(self):
        return self.lista[self.corriente] == self.fin
    def valor(self):
        return self.lista[self.corriente]
        

def acumula(fin):
    acc = 0
    while acc < fin:
        acc += 1
        print(acc)

def acumula2(fin):
    cont = Contador(0, fin)
    while not cont.terminado():
        print(cont.valor())
        cont.inc()

def acumula_letras(empieza, fin):
    cont = ContadorAlfabeto(empieza, fin)
    while not cont.terminado():
        print(cont.valor())
        cont.inc()

def sucesor(objeto, empieza, fin):
    cont = objeto(empieza, fin)
    while not cont.terminado():
        print(cont.valor())
        cont.inc()
