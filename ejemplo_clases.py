class Heroe:
    #nombre, poder, apodo son variables de la clase Heroe
    nombre=""
    poder=""
    apodo=""
    #funcion especial de python que se ejecuta al crear un objeto
    #funcion inicial o constructor
    def __init__(self,nombre,poder,apodo):
        self.nombre = nombre
        self.poder = poder
        self.apodo = apodo

    def saludar(self):
        print(f"Hola {self.nombre}")


    #spiderman es un objeto de la clase Heroe
spiderman = Heroe("Peter parker","super fuerza","Hombre araña")
ironman = Heroe("tony Stark","Millonario","Hombre de acero")

spiderman.saludar()
ironman.saludar()
