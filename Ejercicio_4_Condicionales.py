# Ejercicio 4 - Calculadora Basica

# Construir un programa que simule el funcionamiento de una calculadora que puede realizar las 4 operaciones aritméticas básicas (suma, resta, multiplicación y división). El usuario debe especificar la operación con el primer carácter del nombre de la operación

# S, s --> Suma
# R, r --> Resta
# M, m --> Multiplicación
# D, d --> División

num1 = int(input('Digite un numero: '))
num2 = int(input('Digite otro numero: '))
op = input('Digite la letra inicial de la operacion a realizar: s - suma, r - resta, m - multiplicacion, d - division. Que operación desea realizar? ')

op = op.lower()

if op == "s":
    resultado = num1 + num2
    print(f'El resultado es: {resultado}')
elif op == "r":
    resultado = num1 - num2
    print(f'El resultado es: {resultado}')
elif op == "m":
    resultado = num1 * num2
    print(f'\nEl resultado es: {resultado}')
elif op == "d":
    resultado = num1 / num2
    print(f'\nEl resultado es: {resultado:.2f}')
else:
    print("La letra ingresada no es válida.")