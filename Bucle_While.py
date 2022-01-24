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

while i == 5: # Le tenemos que especificar <= ya que aunque queremos que en cuanto llegue al 5 se detenga, si solo igualamos a 5 (i == 5), este bucle no se ejecutaria, debido a que como empezamos con el valor de 1, la variable i nunca valdria 5, debido a que como solo hay aumento de la variable si vale 5 y no puede llegar a este 5 sin tener aumento pues jamas entraria al bucle
    print(i)
    i += 1 