
"""
tuplas mutabilidad
diccionarios
 no puedes usar elementos mutables como llave en un diccionario
pip y paquetes
dot notation
lectura de archivos
recursión
scope
magic methods
everything is an object
literals
"""

# mutabilidad

"""
mutables:
 list
 dict

inmutables:
 tuple
 str
 fun
"""

# Scope, contexto, namespace
c = 10
d = 30

def fun(a, b):
    return a + b + c

def bar(a, b):
    c = 50
    return a + b + c

def contexto():
    d = 20
    return d

"""
GLOBAL---
d -> 40
DECIMOPRIMERA---
d -> 30
DECIMOPRIMERA.CONTEXTO---
d -> 20
"""

# dot notation

# todo es un objeto (everything is an object)
# attribute, method

# diccionarios

# recursion

def factorial(a):
    for i in range(1, a):
        a *= i
    return a

def rf(a):
    if a == 0:
        return 1
    else:
        return a * rf(a-1)

"""
rf(5)
5 * rf(5-1)
5 * rf(4)
5 * 4 * rf(4-1)
5 * 4 * rf(3)
5 * 4 * 3 * rf(2)
5 * 4 * 3 * 2 * rf(1)
5 * 4 * 3 * 2 * 1 * rf(0)
5 * (4 * (3 * (2 * (1 * (1)))))
5 * (4 * (3 * (2 * (1 * 1))))
5 * (4 * (3 * (2 * (1))))
5 * (4 * (3 * (2)))
120
"""

def rrf(a):
    def ayuda(a, b):
        if b == 0:
            return a
        else:
            return ayuda(a * b, b-1)
    return ayuda(1, a)

"""
rrf(4)
ayuda(1 , 4)
ayuda(4 , 3)
ayuda(12, 2)
ayuda(24, 1)
ayuda(24, 0)
24
"""

# pip y paquetes

