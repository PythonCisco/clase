
"""
lectura de archivos
packing y unpacking
ordenamiento de listas
pyc and importlib
 lean un archivo,
 extraigan todas las vocales
 cuenten la cantidad de vocales en el archivo
venv
"""

with open("cuarta.py") as f:
    lineas = f.readlines()
print(lineas)

"""
archivo = open("cuarta.py")
archivo.read()
archivo.readline()
archivo.readlines()
archivo.seek(0)
archivo.close()
"""

#[bruno\nfranco\nsalamin\nbrantley\nperez]
        #^

def mayor(estudiantes):
    ma = (0, "")
    for llave,valor in estudiantes.items():
        ma = max( (valor, llave) , ma)
    edad, nombre = ma
    return (nombre, edad)
        
