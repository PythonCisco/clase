
"""
words with n letters
variaciones
 dadas las letras a, b, c. Cuantas palabras de 3 letras se pueden crear?
 abc, aaa, acc, aba
permutaciones
 dadas las letras a, b, c. Cuantas palabras de 3 letras se pueden crear, donde no se repita ni una letra
 abc, cab; aab, bbb,
addicion
 2 5 + ; 1+ 1- 0=
descanso y trabajo
abreviaciones
 ["bruno", "franco", "salamin", "brantley"] -> ["bru", "f", "s", "bra"]
"""

# variaciones
# [a, b, c] -> 4

def variaciones():
    lst = 'a b c'.split()
    retorna = []
    for i in lst:
        for j in lst:
            for k in lst:
                print("i:{} j:{} k:{}".format(i, j, k))
                retorna.append(i + j + k)
    return retorna

#def variaciones(lst):
    #for i in lst:

def permutaciones():
    lst = 'a b c d'.split()
    retorna = []
    print("lst\t\t\tll\t\t\tla\t\ti+j+k")
    for i in lst:
        ll = lst.copy()
        ll.remove(i)
        for j in ll:
            la = ll.copy()
            la.remove(j)
            for k in la:
                retorna.append(i+j+k)
                print("{}\t\t{}\t\t{}\t\t{}".format(lst, ll, la, i+j+k))
    return retorna
        

"""
1) como se ve la entrada
2) como se ve la salida
3) que cambio le puedo hacer a la entrada para que se parezca más a la salida
4) que cambio le puedo hacer a la salida para que se parezca más a la entrada
5) intenta juntar ambos lados

1) parte el paso grande en pasos pequeñitos
2) haz cada paso pequeñito uno a uno

maximo: 1 2 -> 2
 2
pares:  [1, 2, 3, 4, 5, 6] -> 2 4 6  [2, 4, 6]
 [2, 3, 4, 5, 6]
 [2, 4, 5, 6]
[2, 4, 5, 6]
[2, 4, 6]

identificar los numeros impares
 n % 2 != 0
 el numero es impar
removerlos de la lista
 reasignar la lista
 construir una nueva lista solo con los elementos seleccionados

celula: "nombre" | "apodo" | "cargo" | 432 -> "1-234-567"
"""

