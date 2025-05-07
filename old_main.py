
diccionario={"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1} 
dic_entero_a_romanos={
    1:"I",2:"II",3:"III",
    4:"IV",5:"V",6:"VI",
    7:"VII",8:"VIII",9:"IX",

    10: "X", 20: "XX", 30: "XXX",
    40: "XL", 50: "L", 60: "LX",
    70: "LXX", 80: "LXXX", 90: "XC",

    100:"C",200:"CC",300:"CCC",
    400:"CD",500:"D",600:"DC",
    700:"DCC",800:"DCCC",900:"CM",

    1000:"M",2000:"MM",3000:"MMM"
}

dic_romano_a_entero={
    "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000
}

restas = { "I":("V", "X"), "X": ("L", "C"), "C": ("D", "M") }

class RomanNumberError(Exception):
    pass

def romano_a_entero(valor:str)->int:
    lista_romano = list(valor)
    valor_entero =0
    cont_repes = 0
    caracter_anterior=""
    caracter_ant_anterior=""

    for caracter in lista_romano:
        if caracter == caracter_anterior:
            if caracter in "DLV":
                raise RomanNumberError("Los caracterers D, L y V no se pueden repetir")
            cont_repes += 1
            if cont_repes == 1 and (caracter in "IXC"):
                raise RomanNumberError("el valor no puede restarse")
        else:
            cont_repes = 0
       
        if cont_repes >= 3:
            raise RomanNumberError("No se puede repetir el valor más de tres veces")

        if caracter_anterior and dic_romano_a_entero.get(caracter_anterior,0) < dic_romano_a_entero.get(caracter,0):
            if caracter_anterior in "DLV":
                raise RomanNumberError("Los caracterers D, L y V no se pueden repetir")

            
            if  caracter not in restas[caracter_anterior]:
                  raise RomanNumberError(f"{caracter_anterior} solo se puede restar de {restas[caracter_anterior][0]} y {restas[caracter_anterior][1]}" )
            valor_entero -= dic_romano_a_entero.get(caracter_anterior,0)*2

            if caracter_anterior == caracter_ant_anterior and caracter_anterior in "IXC":
                raise RomanNumberError("el valor no puede restarse")
              
        caracter_ant_anterior = caracter_anterior
        caracter_anterior = caracter
        valor_entero += dic_romano_a_entero.get(caracter,0)

    
    return valor_entero

def entero_a_romano(numero:int)->str:
    if numero > 3999 or numero > 0 :
        raise RomanNumberError("El límite es entre 0 y 3999")
    if numero == 0:
        return ""
    
    numero = "{:0>4d}".format(numero)
    list_numero = list(numero)
    valor_romano=""
    longitud = len(list_numero)

    for i in range(longitud):
        longitud = longitud-1
        list_numero[i] = list_numero[i] + "0"* longitud
        valor_romano += dic_entero_a_romanos.get(int(list_numero[i]), "")

    return valor_romano
    
print(entero_a_romano(4000))