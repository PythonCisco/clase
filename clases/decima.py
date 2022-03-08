
"""
excepciones
"""
# out of bounds exception
# keyerror
# excepcion para mejor validación de entrada
# excepcion para continuar en un error (keyerror en mi piano)

#
def nombres(nom):
    tortugas_ninja = {"rafael":16, "miguelangel":16, "donatello":15, "leonardo":17}
    return tortugas_ninja[nom]

def edad(nom):
    try:
        return nombres(nom)
    except KeyError:
        return False

def prog():
    a = int(input("deme un numero entero"))
    b = int(input("deme otro numero entero"))
    print(a+b)

def prog():
    flg = True
    while flg:
        try:
            a = int(input("deme un numero entero"))
            flg = False
        except ValueError:
            print("ese no es un numero entero")

    flg = True
    while flg:
        try:
            b = int(input("deme otro numero entero"))
            flg = False
        except ValueError:
            print("ese no es un numero entero")

    print(a+b)

def valida(mensaje, cast, el_error, mensaje_error):
    flg = True
    while flg:
        try:
            a = cast(input(mensaje))
            flg = False
        except el_error:
            print(mensaje_error)
    return a

def prog():
    a = valida("deme un numero entero ", int, ValueError, "ese no es un numero entero")
    b = valida("deme otro numero entero ", int, ValueError, "ese no es un numero entero")
    print(a+b)

def contrasenia():
    return valida("deme una contraseña fuerte: ", lambda x: x.index("0"), ValueError, "esta contraseña es DEBIL") 

"""
try:
    raise(ZeroDivisionError)
except BaseException:
    print("hubo un error")

try:
    raise(ZeroDivisionError)
except:
    print("hubo un error")
"""
