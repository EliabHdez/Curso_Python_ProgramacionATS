# Ejercicio 7 - Pildoras Informaticas

# Crea un programa que pida números infinitamente. Los números introducidos deben ser cada vez mayores. El programa finalizará cuando se introduzca un número menor que el anterior

numMenor = int(input('Introduce un numero: '))
numMayor = int(input(f'Introduzca un numero mayor a {numMenor}: '))

while numMayor > numMenor:
    numMenor = numMayor
    numMayor = int(input('Introduce un numero: '))

print('El numero introducido es menor que el anterior')

print('Fin del programa')