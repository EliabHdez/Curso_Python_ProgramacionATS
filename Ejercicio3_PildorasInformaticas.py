# Ejercicio 3 - Pildoras Informaticas

# Crea un programa que pida tres numeros por teclado. El programa imprime en consola la media aritmpetica de los números introducidos

num1 = float(input('Digita el primer número: '))
num2 = float(input('Digita el segundo número: '))
num3 = float(input('Digita el tercer número: '))

mediaAritmetica = (num1 + num2 + num3) / 3

print(f'La media aritmpetica es: {mediaAritmetica:.2f}')