# Ejercicio 8 - Pildoras Informaticas

# Crea un programa que pida números positivos indefinidamente. El programa termina cuando se introduce un número negativo. Finalmente el programa muestra la suma de todos los numeros introducidos

numPos = int(input('Introduce un numero positivo: '))
suma = 0

while numPos > 0:
    suma = suma + numPos
    numPos = int(input('Introduce un numero positivo: '))

print(f'La suma de los numeros es {suma}')
print('Fin del programa')