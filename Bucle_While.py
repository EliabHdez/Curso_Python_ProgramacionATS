# Bucle While

# En pocas palabras los bucles son ciclos que mientras se cumpla la condicion que se les asigna estos se siguen ejecutando, en el momento que deje de cumplirse la condicion, este se detiene y deja de ejecutarse. Esto aplica para cualquier bucle o ciclo

# El bucle while se conoce por ser un bucle con un numero indeterminado de iteraciones, esto quiere decir que se puede repetir x cantidad de veces, todas las que sean necesarias o ninguna vez, dependiendo de si se cumple la condicion o no

import math

numero = int(input('Digite un número: '))

while numero < 0:
    print('Error: El numero a digitar tiene que ser positivo')
    numero = int(input('Digite un número: '))
    
print(f'\nLa raiz cuadrada es: {math.sqrt(numero):.2f}')

# Podemos ocupar variables iteradoras para cumplir un determinado numero de repeticiones en un bucle

print('***Bucle 1***')

i = 0

while i < 5:
    print('Hello World')
    i += 1
    
# Con el siguiente bucle imprimimos el numero de vueltas que da el ciclo mientras la condicion se cumpla, por lo tanto me imprime hasta el numero 4, ya que al momento de llegar al 5 la condicion se cumple y ahi ya no se ejecuta el bucle y ya no imprime el 5

print('***Bucle 2***')
    
i = 0

while i < 5:
    print(i)
    i += 1
    
# Si lo que queremos es que por ej se imprima del 1 al 5, tenemos que cambiar la condicion, al igual que el valor de la variable, ya que la primera impresion es con el valor inicial de la variable debido a que la primer vuelta antes del primer aumento a la variable iteradoradora tambien cuenta

print('***Bucle 3***')

i = 1

while i <= 5: # Le tenemos que especificar <= ya que aunque queremos que en cuanto llegue al 5 se detenga, si solo igualamos a 5 (i == 5), este bucle no se ejecutaria, debido a que como empezamos con el valor de 1, la variable i nunca valdria 5, debido a que como solo hay aumento de la variable si vale 5 y no puede llegar a este 5 sin tener aumento pues jamas entraria al bucle
    print(i)
    i += 1
    
# Informacion adicional del Bucle While - Pildoras Informaticas

# Como podemos hacer que el Bucle While en ciertos casos no sea un bucle infinito? Ej si tenemos un programa donde nos pida la edad del usuario y este lo limitamos con un bucle while para que la edad este entre 5 y 100 y el usuario se empeña en meter un dato menor a 5 o mayor a 100 el bucle se repetiria de forma infinita ya que el usuario no pasaria nunca un valor entre 5 y 100. Hay una manera de que este bucle pare en cierto punto y es mediante el break. El break lo que hace es decirle al bucle que se rompa y se salga de este. Veamos esto con un ejemplo practico para entenderlo

print('Programa validación edad del usuario')

edad = int(input('Introduce tu edad: '))
intentos = 0

while edad < 5 or edad > 100:
    error = 'Edad incorrecta. Vuelve a intentarlo'
    print(error)
    intentos += 1
    edad = int(input('Introduce tu edad: '))
    if intentos == 5:
        print('Edad inválida. Haz alcanzado el límite de intentos')
        break
if intentos < 5:
    print('Edad válida')

print('Fin del programa')

# Ejercicio realizado por el profe Juan de Pildoras Informaticas en el video del curso

# print('Programa de calculo de raiz cuadrada')

# numero = int(input('Introduce un numero: '))
# intentos = 0

# while numero < 0:
#     print('No se puede calcular la raiz cuadrada de un numero negativo')
    
#     if intentos == 2:
#         print('Haz consumido demasiados intentos')
#         break
    
#     numero = int(input('Introduce un numero positivo: '))
#     if numero < 0:
#         intentos += 1
        
# if intentos < 2:
#     solucion = math.sqrt(numero)
#     print(f'La raiz cuadrada de {numero} es: {solucion}')
    
# print('Fin del programa')