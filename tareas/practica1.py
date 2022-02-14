"""
Mayra Medina
2022-02-11
"""

def elefantes(numero):
    """Imprime las estrofas de la canción "un elefante se columpiaba" desde la primera hasta número.
    """
    for n in range(1,numero+1):
        if n==1:
            print(n," elefante se columpiaba sobre la tela de una araña,")
            print("como veia que resistia, fue a buscar otro elefante.")
        else:
            print(n," elefantes se columpiaban sobre la tela de una araña,")
            print("como veian que resistia, fueron a buscar otro elefante.")

def elefantes_ref(numero):
    """Imprime las estrofas de la canción "un elefante se columpiaba" desde la primera hasta número.
    """
    
    print(1," elefante se columpiaba sobre la tela de una araña,")
    print("como veia que resistia, fue a buscar otro elefante.")
    for n in range(2,numero+1):
        print(n," elefantes se columpiaban sobre la tela de una araña,")
        print("como veian que resistia, fueron a buscar otro elefante.")


def terna_pitagorica(a,b,c):
    #(a**2 + b**2 == c**2)
    if a>b:
        if a>c:
            m1=(b*b)+(c*c)
            m2=a*a
            if m1==m2:
                return True
            else:
                return False

    if b>a:
        if b>c:
            m1=(a*a)+(c*c)
            m2=b*b
            if m1==m2:
                return True
            else:
                return False

    if c>b:
        if c>a:
            m1=(b*b)+(a*a)
            m2=c*c
            if m1==m2:
                return True
            else:
                return False

def terna_pitagorica_ref(a,b,c):
    #(a**2 + b**2 == c**2)
    if a>b:
        if a>c:
            m1=(b*b)+(c*c)
            m2=a*a
            if m1==m2:
                return True
            else:
                return False

    if b>a:
        if b>c:
            m1=(a*a)+(c*c)
            m2=b*b
            if m1==m2:
                return True
            else:
                return False

    if c>b:
        if c>a:
            m1=(b*b)+(a*a)
            m2=c*c
            if m1==m2:
                return True
            else:
                return False

def terna(hipotenusa, cateto1, cateto2):
    #(a**2 + b**2 == c**2)
    cuadrado_catetos = (cateto1*cateto1)+(cateto2*cateto2)
    cuadrado_hipotenusa = hipotenusa*hipotenusa
    return cuadrado_catetos == cuadrado_hipotenusa

def terna_pitagorica_ref(a, b, c):
    return terna(a, b, c) or terna(b, a, c) or terna(c, a, b)
