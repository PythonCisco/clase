"""
Bruno Franco Salamin
2022-02-14

listas y sus metodos
como imprimir una flecha
encifrado del cesar
refactorización comprensiva
buenos nombres
"""

cabeza = [
        "  *  ",
        " *** ",
        "*****"]

cuerpo = [" *** "] * 7

def flecha():
    for i in cabeza:
        print(i)
    for i in cuerpo:
        print(i)

def flecha2():
    for i in cabeza + cuerpo:
        print(i, "   ", i)

def flechaN(numero):
    """Imprime numero de flechas, todas una al lado de la otra.
    """

flcha = "  *  \n *** \n*****\n *** \n *** \n *** \n *** \n"
