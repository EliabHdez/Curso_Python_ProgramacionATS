#  Ejercicio 6 Bucle for - Pildoras Informaticas

# Crea un programa que evalue si una dirección de correo electrónico es válida o no en función de si tiene '@' o '.'. Hay que tener en cuenta que la dirección se considera correcta si solo tiene un @ y si tiene uno o mas puntos '.'

email = input('Introduce tu email: ')
contador1 = 0
contador2 = 0

for i in email:
    if i == '@':
        contador1 = contador1 + 1
    if i == '.':
        contador2 = contador2 + 1
if contador1 == 1 and contador2 >= 1:
    print('Email válido')
else:
    print('Error: Email inválido')
    
print('***Solucion profe Juan Pildoras Informaticas***')

for i in range(len(email)):
    if email[i] == '@':
        contador1 = contador1 + 1
    if email[i] == '.':
        contador2 = 1
if contador2 == 0 or contador1 != 1:
    print('email incorrecto')
else:
    print('email correcto')