
"""
clase
instancia
objetos
"""

class MyClass():

    def __init__(self, a):
        self.a = a

    def hola(self):
        print("hola mundo")

    def adios(self):
        print("chao")

def base(lst, num):
 if num == 1:
  return lst
 else:
  a = []
  for i in lst:
   a.append( [i + j for j in base(lst, num-1)])
  return a

def varias(lst, num):
 if num == 1:
  return lst
 else:
  a = []
  for i in lst:
   a += [i+j for j in varias(lst, num-1)]
  return a

"""
varia0
 lst
  [a, b, c, ...]
  [a, b, c]
  [a, b]
  [a]
  []
 num
  4
  3 [aaa, aab, aac, ...]
  2 [aa, ab, ac, ..., ba, bb, bc, ...]
  1 [a, b, c, d, ...]
  0

0-1-3
   -4
 -2-5
   -6
"""

def varia0(lst, num):
 if num == 0:
  return [""] * len(lst)
 else:
  a = []
  for i in lst:
   a += [i+j for j in varia0(lst, num-1)]
  return a


variaciones = basee

def permutaciones(lst, longitud):
    if longitud == 0:
        return [""]
    else:
        ret = []
        for i in lst:
            lst = lst.copy()
            lst.remove(i)
            ret += [i+j for j in permutaciones(lst, longitud-1)]
        return ret

def permutaciones(lst, longitud):
    if longitud:
        ret = []
        for i in lst:
            lst = lst.copy()
            lst.remove(i)
            ret += [i+j for j in permutaciones(lst, longitud-1)]
        return ret
    return [""]


def permall(lst):
    acumula_permutaciones = []
    for i in range(1, len(lst)+1):
        acumula_permutaciones += permutaciones(lst, i)
    return [""] + acumula_permutaciones

def perm(lst):
    return permutaciones(lst, len(lst))

def swap(lst):
    return ["".join(lst[:]), "".join(lst[::-1])]

def reordenaciones(lst):
    if len(lst) == 0:
        return [""]
    if len(lst) == 1:
        return lst
    if len(lst) == 2:
        return swap(lst)
    else:
        retorno = []
        for i in lst:
            lista = lst.copy()
            lista.remove(i)
            retorno += [i + j for j in reordenaciones(lista)]
        return retorno
"""
1
1
12
21
123
132
213
312
1234
"""


"""
clase
constructor
objeto
"""
