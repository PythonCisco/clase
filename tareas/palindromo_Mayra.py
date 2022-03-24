def palindromo(palabra):
    """
    La función acepta una palabra y retorna True si es palindroma y False si no.
    """
    # Utilicé una variable para invertir la palabra que se ingrese
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

"""
p("oro") "oro" "oro"
p("otorrinolaringologia") "otorrinolaringologia" "otorrinolaringologia"
"""

def palio(palabra):
    def invertido(num):
        """Retorna el indice inverso. 0 es -1, 1 es -2, y asi."""
        return - (num + 1)
    for i in range(len(palabra)):
        if palabra[i] != palabra[invertido(i)]:
            return False
    return True

def palino(palabra):
    for i in range(len(palabra)):
        if palabra[i] != palabra[-(i + 1)]:
            return False
    return True

def palindo(palabra):
    def invertido(num):
        """Retorna el indice inverso. 0 es -1, 1 es -2, y asi."""
        return - (num + 1)
    for i in range(len(palabra)//2):
        if palabra[i] != palabra[invertido(i)]:
            return False
    return True


"""
bruno
^   ^
0   -1
1   -2
2   -3

bruno
|   ^
 | ^
  |
 ^ |
^   |

aa
aaaa
aaaiaaa

oro
^ ^
"""


"""
interprete[ c, f, pm[palindromo, a, b], a ]
interprete[ c, f, a, b, palindromo ]
"""
