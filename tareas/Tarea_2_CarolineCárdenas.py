"""
Caroline Cárdenas
2022-02-16
"""

"""SECUENCIA DE FIBONACCI
"""
def fibonacci(number):
    """Retorna el número que se encuentra en la secuencia de fibonacci
    según el índice dado
    """
    if (number == 0):
        return 0
    elif (number == 1):
        return 1
    else:
        return (fibonacci(number-2)+fibonacci(number-1))

def lista_fibo(n):
    """Retorna una lista de la secuencia de fibonacci hasta el índice dado
    """
    #declarar lista
    arr = [0,1]

    #if que valida los valores según el índice dado
    if (n == 1):
        #si el índice es 1, se imprime el 0
        print("0")
    elif (n == 2):
        #si el índice es 2, se imprime el 0 y el 1
        print('[0, ','1]')
    else:
        #si es mayor a 2 el valor del índice, se hace un while que se corre mientras
        #la longitud del índice sea menor al número dado.
        while(len(arr)<n):
            arr.append(0)
        if(n==0 or n==1):
            return 1
        else:
            arr[0]=0
            arr[1]=1
            for i in range(2,n):
                arr[i]=arr[i-1]+arr[i-2]
            print(arr)

"""FACTORIAL
"""
def factorial(n):
    """Retorna el factorial del número dado
    """
    fac = int(1)

    for i in range(1, n+1):
        fac = fac * i

    #Retorna el factorial del número dado
    return fac


def triangular(n):
    trian = int(1)
    """Retorna el triangular del número dado
    """

    for i in range(1, n+1):
        trian = trian + i

    #Retorna el triangular del número dado
    return trian



