import random

def gllista():
    l = []
    for i in range(3):
        l.append(random.randint(0, 99))
    return l 

def gresposta():
    m = []
    for i in range(3):
        m.append(int(input("Introduzca un número: ")))
    return m 

def comparar(l, m):
    #for i,e in enumerate(l):
    a= [0,0,0]
    for i in range(3): 
        if l[i] == m[i]:
            a[i]= 10
           
    if a[0]==10 and a [1]==10 and a[2]==10:
        print("Enarabona")
        return 0
    for i in range(3):
        if a[i]==0:
            if m[i] in l: 
                a[i]=5
    for i in range(3):
        if a[i]==10:
            print("L'element {} és correcte".format(m[i]))
        elif a[i]==5: 
            print("L'element {} existeix, però no està al seiu lloc".format(m[i]))
        else:print("L'element {} no existeix". format(m[i]))

            
    """
    1. Si són iguals llavors missatge tot ok
    
    2. Sino si hi ha qualque element ben col·locat o hi ha elements mal col·locats
        2.1. 
    3. Sino si no hi ha res llavors missatge un desastre!
        if m == l:
        print("Las listas son iguales")
    else:
        print("Las listas no son iguales")
    """    
    print("No sé comparar-ho de moment")


def pex1():
    # Pide al usuario que introduzca una lista de números
    lista_aleatoria = gllista()
    print("S'ha generat una llista aleatoria de 3 números del 0 al 100")
    lista_usuario = gresposta()
    print("Lista de usuario:", lista_usuario)
    comparar(lista_aleatoria, lista_usuario)

