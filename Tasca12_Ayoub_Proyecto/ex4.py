
class Animal: 
    def __init__(self, nombre):
        self.nombre = nombre
        
    def sonido(self):
        return "Hace algún sonido"

class Perro(Animal):
    def sonido(self):
        return "Guau guau"

class Gato(Animal):
    def sonido(self):
        return "Miau Miau"
        

def pex4():
    
    l=[Perro("Firulais"), Gato("Garfield")]
    for e in l:
          print(e.sonido())
        
#pex4()  
        

   
    

        