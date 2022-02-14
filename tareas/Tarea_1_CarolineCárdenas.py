#CIFRADO DEL CESAR

def cifradocesar():
    text = input("Escribe tu texto: ")

    if text == text.upper(): #MAYUSCULAS
        abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else:
        abc = "abcdefghijklmnopqrstuvwxyz" #minusculas

    valor = int(input("Valor de desplazamiento: "))

    #Cadena cifrada

    cadcif = ""

    #cifrado

    for x in text:
        if x in abc:
            cadcif += abc[(abc.index(x)+ valor)%(len(abc))]
        else:
            cadcif += x


    #TEXTO FINAL
    print("Texto cifrado:", cadcif)
    

#ELEFANTES

def elefantes(numero):
    
    for x in range(numero+1):
        if x == 1:
            cadena = str(x) + " elefante se columpiaba sobre la tela de una araña, como veia que resistia, fue a buscar otro elefante."
            print(cadena)
            print("")
        elif x > 1:
            cadena = str(x) + " elefantes se columpiaban sobre la tela de una araña, como veian que resistia, fueron a buscar otro elefante."
            print(cadena)
            print("")
            

#TERNA DE PITAGORAS
#Faltó la parte de no importa el orden.

def terna_pitagorica(a, b, c):

    if a**2 + b**2 == c**2:
        return True
    else:
        return False
    

                    
            
