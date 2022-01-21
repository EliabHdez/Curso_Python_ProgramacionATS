# Ejercicio 2

# Hacer un programa que pida 3 numeros y determine cual es el mayor

num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
num3 = int(input("Digite el tercer numero: "))

if num1 >= num2 and num1 >= num3:
    print(f'El numero mas alto es {num1}')
elif num2 >= num3 and num2 >= num1:
    print(f'El numero mas alto es {num2}')
elif num3 >= num1 and num3 >= num2:
    print(f'El numero mas alto es {num3}')
else:
    print('Todos los numeros son iguales')
