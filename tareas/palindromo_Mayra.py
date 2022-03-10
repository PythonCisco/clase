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
