#estudiante: Carlos Gonzalez


def codigo_cesar():
    

    #introduciomos el texto para cifrar en codigo cesar
    texto=input("la palabra: ")

    #creamos la cadena de caracteres que usaremos para comprobar la posicion de cada letra
    if texto== texto.upper():
        abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    else:
        abc="abcdefghijklmnñopqrstuvwxyz"

    #definimos el numero codigo que usaremos
    k =int(input("ingrese el codigo para criptar: "))

    #creamos una variable para guardar la palabra criptada
    cifra=""

    #empezamos el cifrado
    for c in texto:
        if c in abc:
            cifra += abc[(abc.index(c)+k)%(len(abc))]
        else:
            cifra+=c
    
    #palabra criptada
    print(texto)
    print(cifra)

def elefantes():
    #ingrese el numero de veces que se repite el programa
    n=int(input("ingrese cuantos elefantes se balancean: "))
    i=0

    #se usa un for para imprimir cada cadena
    for i in range(n+1):
        if(i>0):
            print(str(i)+" elefante se columpiaba sobre la tela de una araña\ncomo veia que resistia, fue a buscar otro elefante\n")

def pitagoras():
    #ingreso de a,b,c para calcular el teorema de pitagoras
    a= float(input("Ingrese un numero: "))
    b= float(input("Ingrese un numero: "))
    c= float(input("Ingrese un numero: "))

    #comprobamos cual de los tres numeros es mayor para si hacer la suma

    #Se comprueba que a es el mayor
    if a>b and a>c:
        resultado=(b*b)+(c*c)
        #se demuestra que si es verdad o falso, calculando los dos numeros menores elevandolos a dos y sumar el total de ambos.
        if resultado==(a*a):
            print("true")
        else:
            print("false")
    #Se comprueba que b es el mayor
    elif b>a and b>c:
        resultado=(c*c)+(a*a)
        #se demuestra que si es verdad o falso, calculando los dos numeros menores elevandolos a dos y sumar el total de ambos.
        if resultado==(b*b):
            print("true")
        else:
            print("false")
    #Se comprueba que c es el mayor
    else:
        resultado=(b*b)+(a*a)
        #se demuestra que si es verdad o falso, calculando los dos numeros menores elevandolos a dos y sumar el total de ambos.
        if resultado==(c*c):
            print("true")
        else:
            print("false")
    
    print("resultado: "+str(resultado)+"\na: "+str(a)+"\nb: "+str(b)+"\nc: "+str(c))