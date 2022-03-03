# Factorial de un numero entero

def factorial(n):
    if n == 0:
        return 1
    else:
        recursivo = factorial(n-1)
        resultado = n * recursivo
        return resultado

if __name__ == '__main__':

    print(factorial(4))
