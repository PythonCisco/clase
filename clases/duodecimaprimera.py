
"""
t.forward	t.fd
t.backward	t.bk
t.left		t.lt
t.right		t.rt

t.reset

"""

import duodecima as dd

def asdf(lgt):
    dd.poligono(4, lgt)
    
    t.fd(lgt)
    dd.poligono(4, lgt/2)
    
    t.lt(90)
    t.fd(lgt/2)
    t.rt(90)

def recursion(pasos, lgt):
    for i in range(pasos):
        asdf(lgt)
        lgt /= 2
    dd.poligono(4, lgt)

"""
que es un generador

0	1	2	3	4	5
1	2	3	4	5	6

yield(now + 1)  now
"""

def enteros(empieza):
    while True:
        empieza += 1
        yield empieza
