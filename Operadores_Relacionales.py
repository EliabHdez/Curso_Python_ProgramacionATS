""" Óperadore Relacionales
        - Se utilizan para establecer una relacion entre 2 valores
        - Compara estos valores entre si y esta comparacion produce un resultado de certeza o falsedad (verdadero o falso)
        - Tienen el mismo nivel de prioridad en su evaluacion
        - Los operadores relacionales tiene menor prioridad que los aritmeticos """

""" 
    Tipos de Operadores Relacionales
        > Mayor que
        < Menor que
        >= Mayor o igual que
        <= Menor o igual que
        != Diferente
        == Igual 
"""

print("***********")

resultado = 10 < 20
print(resultado)

print("***********")

resultado = 10 > 20
print(resultado)

print("***********")

resultado = 10 == 20 # No hay que confundir el operador relacional de igualdad (==) con el operador de asignacion (=). El primero son dos signos de igual seguidos y juntos y el segundo solo es uno. Asi mismo el primero nos sirve para comparar dos valores y el segundo sirve para asignar valores a las variables
print(resultado)

print("***********")

resultado = 10 != 20
print(resultado)

print("***********")

# En los operacidores relacionales mayor / menor o igual que, evalua dos condiciones y si alguna de las dos se cumple arroja verdadero, si ninguna se cumple el resultado sera falso

print("*****mayor / menor o igual que******")

resultado = 10 <= 20
print(resultado)

print("***********")

resultado = 10 >= 20
print(resultado)

print("***********")

resultado = 20 <= 20
print(resultado)

print("***********")

resultado = 20 >= 20
print(resultado)

print("*****OpMat / OpRel******")

# Los operadores relacionales se pueden combinar con los operadores matematicos

# LOS OPERADORES MATEMATICOS TIENEN PRIORIDAD SOBRE LOS OPERADORES RELACIONALES

a = 10
b = 20
c = 30

resultado = a+b == c
print(resultado)

resultado = a+b != c
print(resultado)

# Como podemos observar en los ejemplos anteriores se realiza primero la operacion matematica (suma) y despues la comparacion entre los valores de acuerdo al operador relacional asignado, esto debido a que los operadores matematicos tienen mayor peso y mas prioridad que los operadores relacionales