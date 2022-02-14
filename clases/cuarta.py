"""
fecha:2022-02-11

Temas:
3 formas de escribir cadenas (", ', \"\"\")
docstring (al principio del archivo, sobre variables, dentro de funciones)
refactorización
factores de un número
separar en funciones mas pequeñas.
operadores logicos (and, or, not).
bucles
"""

"lista de notaciones para cadenas. Se verán todas iguales al correr."
listaDeCadenas = ["cadena" ,'cadena', """cadena"""]

def pan(a):
    """Retorna a + 1.
    
    Función de ejemplo para docstring de funciones.
    """

    return a + 1

"""factorización
12 = 3 * 4
12 = 3 * 2 * 2
12 = 2 * 6
12 = 1 * 12
"""

"for, while"

def for_eg(lista):
    accumulador = 0
    for i in lista:
        accumulador += i
    return accumulador

def foreg1(pares):
    """Unpacking demostración.
    """
    for a, b in pares:
        print(a, b, a+b)

def forpara(numeros, paro):
    for i in numeros:
        print(i)
        if paro(i):
            break

def forsalta(numeros, salto):
    for i in numeros:
        if i == salto:
            continue
        print(i)

def whileeg(comienzo, final):
    while comienzo != final:
        print(comienzo)
        comienzo += 1

def whileeg(comienzo, final, para):
    print(comienzo)
    comienzo += 1
    while comienzo != final:
        print(comienzo)
        comienzo += 1
        if comienzo == para:
            break
