# Condicionales

# Los condicionales nos sirven para evaluar y comparar datos y valores, que de acuerdo a cierta instruccion, resultado o sentencia se ejecute "x" accion. Estos condicionales comparan dos valores para determinar que accion llevar a cabo. En pocas palabras actuan de la siguiente manera...

""" 
    "si (if)" se cumple esta condicion --> ejecuta esta accion
        "si no, si (elif)" se cumple esta condicion --> ejecuta esta accion (Este se vendria ocupando cuando vamos a tener varias condiciones diferentes, es decir que si no es una, es otras y si no otras y asi sucesivamente)
            "si no (else)" --> ejecuta esta accion (si no se cumplio ninguna de las anteriores) (Este seria el utimo a poner, quiere decir que llevara la ultima condicion, ya no habra mas condicionales despues de este)
"""


numero = int(input("Digite un numero: "))

if numero > 0:
    print("El numero es positivo")
elif numero == 0:
    print("El numero es 0")
else:
    print("El numero es negativo")

print('Fin del programa')