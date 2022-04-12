
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

"""
axx
 a
  a
  b
  c
 b
  a
  b
  c
 c
  a
  b
  c
bxx
 a
  a
  b
  c
 b
  a
  b
  c
 c
  a
  b
  c
cxx
 a
  a
  b
  c
 b
  a
  b
  c
 c
  a
  b
  c
"""

"""
axx
 ax
  a
  b
  c
 bx
  a
  b
  c
 cx
  a
  b
  c
bxx
 ax
  a
  b
  c
 bx
  a
  b
  c
 cx
  a
  b
  c
cxx
 ax
  a
  b
  c
 bx
  a
  b
  c
 cx
  a
  b
  c
"""

def variaciones():
    lst = 'a b'.split()
    retorna = []
    for i in lst:
        for j in lst:
            for k in lst:
                print("i:{} j:{} k:{}".format(i, j, k))
                retorna.append(i + j + k)
    return retorna


def variaciones():
    lst = 'a b'.split()
    retorna = []
    for i in lst:
        for j in lst:
            retorna.append(i + j)
    return retorna

def vari(lst):
    retorno = []
    def aiuda(lst, n):
        if n:
            for i in lst:
                return i + aiuda(lst, n-1)
        else:
            return ""
    return aiuda(lst, len(lst))

def varis(lst, n):
    retorno = []
    if n:
        for i in lst:
            for j in varis(lst, n-1):
                retorno.append(i + j)
    else:
       return [""]
    return retorno

def base(lst, n):
    if not n:
        return lst
    else:
        for i in lst:
            return [i + j for j in base(lst, n-1)]
            print(i, j)

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
2 = 1*2
3 = 1*2*3
4 = 1*2*3*4
"""

def factor(num):
    if num:
        return num * factor(num-1)
    else:
        return 1       

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

