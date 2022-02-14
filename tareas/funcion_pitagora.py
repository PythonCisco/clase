"""
Anselmo Mc Taggart
2022-02-11
"""


def terna_pitagorica(n1, n2, n3):
    """Imprime si los tres argumentos forman una terna pitagórica.

    No puede distinguir si el orden de los valores no es a, b, c.
    Los dos primeros tienen que ser los catetos, el último debe ser la hipotenusa.
    No retorna nada, solo imprime.
    """

  a = n1 * n1
  b = n2 * n2
  c = n3 * n3
  print(a)
  print(b)
  print(c)
  if a + b == c:
   print(" TRUE Es una Terna Pitagorica")
  else:
   print(" FALSE No una Terna Pitagorica")
  

terna_pitagorica(3, 4, 5)

def terna_pitagorica(n1, n2, n3):
    """Imprime si los tres argumentos forman una terna pitagórica.

    No puede distinguir si el orden de los valores no es a, b, c.
    Los dos primeros tienen que ser los catetos, el último debe ser la hipotenusa.
    No retorna nada, solo imprime.
    """

    # crea variables
    a = n1 * n1
    b = n2 * n2
    c = n3 * n3

    # chekea terna
    if a + b == c:
        terna = True
    else:
        terna = False

    return terna


def imprime_terna(n1, n2, n3):
    # imprime variables
    a, b, c = n1, n2, n3

    print(a)
    print(b)
    print(c)

    if terna_pitagorica(a, b, c):
        print(" TRUE Es una Terna Pitagorica")
    else:
        print(" FALSE No una Terna Pitagorica")
