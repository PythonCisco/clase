"""
Mayra Medina
17/2/2022
"""

def factorial(numero):
    """
    Esta función retorna el factorial del número dado
    """

    resultado = 1

    if numero >= 0:
        #Utilicé la n para realizar la secuencia de la multiplicacion de numeros de 1 a n
        for n in range(numero,0,-1):
            resultado = resultado*n
        print("El factorial de {} es: {}".format(numero,resultado))

    else:
        print("Ingrese un número positivo :)")

def ref_factorial(numero):
    """
    Esta función retorna el factorial del número dado
    validación. i/o entrada/salida. lógica
    """
    resultado = 1
    if numero >= 0:
        #Utilicé la n para realizar la secuencia de la multiplicacion de numeros de 1 a n
        for n in range(numero,0,-1):
            resultado = resultado*n
        print("El factorial de {} es: {}".format(numero,resultado))
    else:
        print("Ingrese un número positivo :)")

def factorial(numero):
    resultado = 1
    for n in range(numero,0,-1):
        resultado = resultado*n
    return resultado

def val_factorial(numero):
    if numero >=0:
        return factorial(numero)
    else:
        print("Ingrese un número positivo :)")

def print_factorial(numero):
    print("El factorial de {} es: {}".format(numero, val_factorial(numero)))
    
def triangular(numero):
    resultado = 1
    for n in range(numero,0,-1):
        resultado = resultado+n
    return resultado



def triangular(numero):
    """
    Esta función realiza la suma de los números desde 1 a n
    """

    suma=1
    if numero == 1:
         print("El triangular de {} es: {}".format(numero,suma+1))
    elif numero>=2:
        for n in range(numero,1,-1):
            suma = suma+n
        print("El triangular de {} es: {}".format(numero,suma))

    else:
        print("Ingrese un número positivo :)")
