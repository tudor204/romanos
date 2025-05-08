from romanos_exception import RomanNumberError
from utiles import dic_entero_a_romanos, dic_romano_a_entero, restas

class NumeroRomano:
    def __init__(self, valor):
        self.valor = valor
        self.valor_romano = ""
        self.valor_entero = 0
        self.representacion_romano =""

        if isinstance(valor, str):  # Si es string, asumimos que es romano
            self.representacion_romano = valor
            self.valor = self.romano_a_entero(valor)
        elif isinstance(valor, int):  # Si es entero
            self.valor = valor
            self.representacion_romano = self.entero_a_romano(self.valor)            
        else:
            raise RomanNumberError("El valor debe ser un entero o una cadena romana")

    def entero_a_romano(self, numero: int) -> str:
        if numero > 3999 or numero < 0:
            raise RomanNumberError("El límite es entre 0 y 3999")
        if numero == 0:
            return ""

        numero = "{:0>4d}".format(numero)  # Asegura 4 dígitos
        list_numero = list(numero)
        self.valor_romano = ""
        longitud = len(list_numero)

        for i in range(longitud):
            potencia = longitud - i - 1
            clave = int(list_numero[i]) * (10 ** potencia)
            self.valor_romano += dic_entero_a_romanos.get(clave, "")

        return self.valor_romano

    def romano_a_entero(self, valor: str) -> int:
        lista_romano = list(valor)
        self.valor_entero = 0
        cont_repes = 0
        caracter_anterior = ""
        caracter_ant_anterior = ""

        for caracter in lista_romano:
            if caracter == caracter_anterior:
                if caracter in "DLV":
                    raise RomanNumberError("Los caracteres D, L y V no se pueden repetir")
                cont_repes += 1
                if cont_repes >= 3:
                    raise RomanNumberError("No se puede repetir el valor más de tres veces")
            else:
                cont_repes = 0

            if (caracter_anterior and 
                dic_romano_a_entero.get(caracter_anterior, 0) < dic_romano_a_entero.get(caracter, 0)):
                
                if caracter_anterior in "DLV":
                    raise RomanNumberError("Los caracteres D, L y V no se pueden usar en resta")
                
                permitidos = restas.get(caracter_anterior, [])
                if caracter not in permitidos:
                    raise RomanNumberError(f"{caracter_anterior} solo se puede restar de {', '.join(permitidos)}")

                if caracter_anterior == caracter_ant_anterior and caracter_anterior in "IXC":
                    raise RomanNumberError("El valor no puede restarse si ya ha sido repetido antes")
                
                self.valor_entero -= 2 * dic_romano_a_entero.get(caracter_anterior, 0)

            caracter_ant_anterior = caracter_anterior
            caracter_anterior = caracter
            self.valor_entero += dic_romano_a_entero.get(caracter, 0)

        return self.valor_entero

    def __repr__(self):
        return self.representacion_romano
    
    def __add__(self,otro):
        if isinstance(otro,NumeroRomano):
            return NumeroRomano(self.valor+otro.valor)
        elif isinstance(otro,int):
            return NumeroRomano(self.valor+otro)
        
    def __sub__(self,otro):
          if isinstance(otro,NumeroRomano):
            return NumeroRomano(self.valor-otro.valor)
          elif isinstance(otro,int):
            return NumeroRomano(self.valor-otro)


probar1 = NumeroRomano("XXVII")
print("romano a entero representacion:", probar1)
print("valor entero:",probar1.valor)
print("Valor romano:",probar1.representacion_romano)
probar2 = NumeroRomano(1977)
print("romano a entero representacion:", probar1)
print("valor entero:",probar2.valor)
print("Valor romano:",probar2.representacion_romano)

