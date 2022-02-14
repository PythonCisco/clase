
#switch con dictionarios

def miswitch(n):
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    else:
        print("cualquier cosa")

def tuswitch(n):
    elecciones = {1:1, 2:2}
    try:
        print(elecciones[n])
    except KeyError:
        print("cualquier cosa")
      

def suma():
    a = input("dame un numero: ")
    b = input("dame otro numero: ")
    print("la suma es:", float(a) + float(b))
    print("la suma es:", a + b)

"""temario
entrada y salida (input y print)
condicionales (if, and, or)
bucles(for y while)
tarea.
"""

"""
diccionario
{1:1, 2:2}
{
hash(1)-> 61832:1
hash(2)-> 56072:2
}
dicc[1]; hash(1) -> 61832
"""

"""
prefija:
+ 1 2 3

infija:
1 + 2 + 3

postfija
1 2 3 +
"""

"""
if [predicado]:
   programa
"""

def menorque(n):
    if n < 15:
        print("menor que 15")
    if n < 30:
        print("menor que 30")

def menoroigual(n):
    if n < 15:
        print("menor que 15")
    elif n == 15:
        print("igual a 15")
    else:
        print("mayor que 15")

def consonantes(cadena):
    conson = "bcdfghjklmnpqrstvwxyz"
    for i in cadena:
        if i in conson:
            print(i, end="")
    
def consonantes2(cadena):
    vocales = "aeiou"
    for i in cadena:
        if i not in vocales:
            print(i, end="")
