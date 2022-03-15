#Una función que, dado un número, imprime todos los números desde 1 hasta el número.
def fizzbuzz(numero):
#Usamos un bucle for para ir contando los numeros desde el 1 hasta en numero que elegimos
    for i in range(numero + 1):
        if i > 0:
#Usamos if para dar las condiciones del problema e imprimir el valor que deseamos
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 5 == 0:
                 print("Buzz")
            elif i % 3 == 0:
                 print("Fizz")
            else:
                print(i)

def fizzbuzz2(numero):
#Agregamos una lista vacia
    lista = []
    for i in range(numero + 1):
        if i > 0:
            if i % 3 == 0 and i % 5 == 0:
#Utilizamos append para añadir los valores que queremos imprimir dentro de la lista vacia
                 lista.append("FizzBuzz")
            elif i % 5 == 0:
                 lista.append("Buzz")
            elif i % 3 == 0:
                 lista.append("Fizz")
            else:
                 lista.append(i)
#Usamos return para que nos regrese la lista                 
    return lista


