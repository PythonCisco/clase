
"""
Bruno Franco Salamin
2022-02-18

comprension de listas (list comprehension)
"""

"for, if, listas"
def triangular(numero):
    """Retorna la lista [1, 1+2, 1+2+3, 1+2+3+4, 1+...+numero]
    """
    retorno = [0]
    for i in range(1, numero+1):
        previo = retorno[-1]
        retorno.append(i + previo)
    return retorno

def cuadrados(numero):
    retorno = []
    for i in range(1, numero+1):
        retorno.append(i**2)
    return retorno

def cuadrados_impares(numero):
    retorna = [i**2
               for i in range(1, numero+1)
               if i%2 != 0]
    return retorna

