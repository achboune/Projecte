import os


def mostrar_menu():
        print("""
        1. Generar fitxer
        2. Llegir contingut
        3. Actualitzar fitxer
        4. Eliminar fitxer
        5. Sortir
        """)

def generar_fitxer(nom_fitxer, contingut):
        with open(nom_fitxer, "w") as fitxer:
            fitxer.write(contingut)

def llegir_fitxer(nom_fitxer):
        try:
            with open(nom_fitxer, "r") as fitxer:
                return fitxer.read()
        except FileNotFoundError:
            return "Fitxer no trobat"

def actualitzar_fitxer(nom_fitxer, contingut):
        generar_fitxer(nom_fitxer, contingut)

def eliminar_fitxer(nom_fitxer):
        try:
            os.remove(nom_fitxer)
            return "Fitxer esborrat amb èxit"
        except FileNotFoundError:
            return "Fitxer no trobat"

def pex2():
        while True:
            mostrar_menu()
            opcio = int(input("Introdueix una opció: "))
            
            if opcio == 1:
                nom_fitxer = input("Introdueix el nom del fitxer: ")
                contingut = input("Introdueix les dades: ")
                generar_fitxer(nom_fitxer, contingut)
            elif opcio == 2:
                nom_fitxer = input("Introdueix el nom del fitxer a llegir: ")
                print(llegir_fitxer(nom_fitxer))
            elif opcio == 3:
                nom_fitxer = input("Introdueix el nom del fitxer a actualitzar: ")
                contingut = input("Introdueix les noves dades: ")
                actualitzar_fitxer(nom_fitxer, contingut)
            elif opcio == 4:
                nom_fitxer = input("Introdueix el nom del fitxer a eliminar: ")
                print(eliminar_fitxer(nom_fitxer))
            elif opcio == 5:
                print("Gràcies per utilitzar-me")
                break
            else:
                print("La opció no és vàlida")

if __name__ == "__main__":
        pex2()