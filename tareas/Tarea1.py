"""
Rafael Romero
2022-02-11
"""

def pitagorica():
    #Terna Pitagorica
    a = float(input("Rngrese el primer lado del triangulo: "))
    b = float(input("Ingrese el segundo lado del triangulo: "))
    c = float(input("Ingrese el tercer lado del triangulo: "))

    if (a**2 + b**2)==c**2:
        print("\nLos lados forman un triangulo rectangulo.")
    elif (a**2 + c**2)==b**2:
        print("\nLos lades forman un triangulo rectangulo.")
    elif (b**2 + c**2)==a**2:
        print("\nLos lados forman un triangulo rectangulo.")     
    else:
        print("\nLos lados no forman un triangulo rectangulo.")



def cesar():
    #Cifrado de Cesar
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    mensaje = "scoobydoo papa"
    clave = 3
    cifrado = ""

    for letra in mensaje.upper():
        if letra in alfabeto:
            indice = alfabeto.find(letra)
            indice += clave
            if indice >=27:
                indice -= 27
            cifrado += alfabeto[indice]
        else:
            cifrado += letra

    print(cifrado)
