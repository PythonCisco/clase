"""
Bruno Franco Salamin
2022-02-16
"""

"""
proceso y procedimiento
prueba de escritorio
"""

def uno():
    a = 0
    for i in range(1, 10):
        print(a, i)
        a += i
    print(a)

"Dada una fuente de numeros aleatorios, haz una lista de listas de numeros, donde dada lista de numeros termine en 3"
"""
0-9 -> [[0, 2, 4, 1, 3], [3], [5, 6, 2, 4, 1, 8, 3], ...]
N Buff      Resultado
4 [4]
5 [4, 5]
3 [4, 5, 3]
- []        [[4, 5, 3]]
6 [6]       [[4, 5, 3]]
"""
def dos(cantidad):
    from random import randint
    retorna = []
    buff = []
    for i in range(cantidad):
        numero = randint(0, 9)
        if numero == 3:
            retorna.append(buff)
            buff = []
        else:
            buff.append(numero)
        print(numero, buff, retorna)
    return retorna

def saludo(nombre, apellido):
    cadena = "hola {}. Te apellidas {} verdad?".format(nombre, apellido)
    print(cadena)
    
    
    


