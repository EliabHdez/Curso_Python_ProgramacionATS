# Ejercicio 3

# Hacer un programa para intercambiar el valor de 2 variables

""" Variables
        a = 10 --> a = 5
        b = 5 --> b = 10
"""

a = int(input("Define el valor de a: "))
b = int(input("Define el valor de b: "))

# Podemos intercambiar valores de las variables, asignando el valor de la variable a alguna otra, pero dentro de la misma linea de codigo, como se muestra abajo, donde estamos indicando el orden que deben obtener con respecto a los valores, es decir la primer variable del lado izquierdo del igual va a almacenar el valor de la primer variable del lado derecho del igual, y asi con las otras variables que le preceden

# Hay otras formas de intercambiar valores de variables, alguna otra puede ser usar una variable auxiliar o temporal que nos almacene el valor destinado para despues agregarlo a nuestra variable final

a , b = b , a

print(f"El nuevo valor de 'a' es: {a}")
print(f"El nuevo valor de 'b' es: {b}")

nombre = "Hernandez"
apellido = "Moises"

nombre , apellido = apellido , nombre

print(f"Tu nombres es: {nombre}")
print(f"Tu apellido es: {apellido}")

# En esta forma estamos utilizando una variable auxiliar o temporal para lograr intercambiar los valores, y tambien esta bien echo, sin embargo es mas laborioso y largo, la primer forma es la mas rapida y sencilla

varA = 10
varB = 20
varAux = varA

varA = varB
varB = varAux

print(varA, varB)