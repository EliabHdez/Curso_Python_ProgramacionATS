# Ejercicio 4 Bucle for - Pildoras Informaticas

# Crea un programa que muestre los numeros impares del 1 al 100. Los números deberán aparecer uno al lado del otro sin salto de línea

for i in range(0,100):
    if i % 2 == 1:
        print(i, end=' ')
        
# Solucion profe Juan Pildoras Informaticas

print('\n***Solucion profe Juan***')

for i in range(1,100,2):
    print(i, end=' ')