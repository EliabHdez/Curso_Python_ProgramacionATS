# Funciones Integradas

# Una funcion integrada sirve para hacer conversiones de tipos de datos. int(), float() etc...

""" Algunas funciones integradas son:
        - int() --> Convierte el dato a tipo numerico entero
        - float() --> Convierte el dato a tipo numerico float
        - str() --> Convierte el dato a tipo string
        - bin() --> Convierte el dato a tipo binario (los dos primeros valores indican que es un dato de tipo binario)
        - hex() --> Convierte el dato a tipo hexadecimal (los dos primeros valores indican que es un dato de tipo hexadecimal)
        - abs() --> Da como resultado el valor absoluto de "x" numero. (El valor absoluto es el valor positivo)
        - round() --> Redondea el valor hacia la baja o alza dependiendo del decimal, de .5 para arriba se va para el alza, de .4 para abajo se para la baja
        - len() --> Cuenta el numero de caracteres que conforman una string
"""

a = int("10")
print(a)
print(type(a))

a = float("10.59")
print(a)
print(type(a))

a = str(10.9)
print(a)
print(type(a))

b = bin(10)
print(b)
print(type(b))

h = hex(10)
print(h)
print(type(h))

# Tanto en la funcion integrada bin() como en la hex() aunque en el tipo de dato aparezca como str, los primeros digitos del resultado de estas dos nos indican que tipo de dato es. Para los binarios sera "0b" y para los hexadecimales sera "0x", con esto podemos asegurarnos que nuesto valor no es una string si no un binario o hexadecimal

# De igual forma podemos convertir binarios o hexadecimales a tipo de dato entero

# Para convertir datos de tipo binario y hexadecimal a entero es necesario poner el valor en forma de string, seguido de una coma y por ultimo la base en la que se encuentra el valor a convertir --> binario = 2 y hexadecimal = 16

b = int("0b1010", 2)
print(b)
print(type(b))

h = int("0xa", 16)
print(h)
print(type(h))

pos = abs(-8)
print(pos)
print(type(pos))

red = round(5.6)
red2 = round(5.4)

print(red, red2)
print(type(red), type(red2))

nombre = len("Eliab Hdez") # Los espacios cuentan como caracteres
print(nombre)