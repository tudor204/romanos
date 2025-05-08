from romanos_class import NumeroRomano
from romanos_exception import RomanNumberError


continuar = True
seguir = ""
operacion = ""
valor = ""

while continuar:
    print("Inicio del programa")
    operacion = input("Que desea realizar \n Romano a entero: presione r  \n Entero a romano presiones :e ")
    
    if operacion =="r":
        try:
            valor = input("Por favor ingrese el valor en romano")
            obj1 = NumeroRomano(valor)
            print(f"El valor de {obj1.representacion_romano} es igual a  {obj1.valor}")
        except RomanNumberError as e:
            print(e)
            break
    elif operacion == "e":
        valor = input("Por favor ingrese el valor entero")
        obj2 = NumeroRomano(valor)
        print(f"El valor de {obj2.valor} es igual a  {obj2.representacion_romano}")



    seguir = input("Si desea salir del programa presione s :")
    if seguir == "s":
        continuar = False
        print("Fin del programa")