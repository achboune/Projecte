import ex1
import ex2
import ex3
import ex4
import ex5
import ex6



def menu():
    op=0
    while op<1 or op>7:
        print("""
        Programa principal
        1.llistes 
        2.fitxers
        3.Joc 
        4.Aplicació amb objectes 
        5.Scrapping
        6.Web
        7.Sortir
        """)
        op = int(input("Introdueix una opció : "))
        if op<1 or op>7:
            print("Opció no vàlida, torni a elegir una opció \n")
        else:
            return op


#Programa principal
op=0
while op!=7:
    op=menu()
    match(op):
        case 1:
            ex1.pex1()
        case 2:
            ex2.pex2()
        case 3:
            ex3.pex3()
        case 4:
            ex4.pex4()
        case 5:
            ex5.pex5()
        case 6:
            ex6.pex6()
        case 7:
            print("Gracies per utilitzar-me")
