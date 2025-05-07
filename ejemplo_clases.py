class Heroe:
    #nombre, poder, apodo son variables de la clase Heroe
    nombre=""
    poder=""
    apodo=""
    edad =20
    #funcion especial de python que se ejecuta al crear un objeto
    #funcion inicial o constructor
    def __init__(self,nombre,poder,apodo):
        self.nombre = nombre
        self.poder = poder
        self.apodo = apodo

    def saludar(self):
        print(f"Hola {self.nombre}, tu edad es: {self.edad}")

    def datos(self):
        return f"Nombre:{self.nombre}, Poder:{self.poder}, Apodo:{self.apodo}, edad:{self.edad}"
#metodo mágico para representar una cadena d devolución
    def __repr__(self):
        return f"Nombre:{self.nombre}, Poder:{self.poder}, Apodo:{self.apodo}, edad:{self.edad}"
    
    
        

    #spiderman es un objeto de la clase Heroe
spiderman = Heroe("Peter parker","super fuerza","Hombre araña")
ironman = Heroe("tony Stark","Millonario","Hombre de acero")
ironman.edad=40
hulk =Heroe("Bruce Banner","Verde", "increible")
hulk.edad = 30

print(spiderman)
print(ironman.datos())
print(hulk.datos())
