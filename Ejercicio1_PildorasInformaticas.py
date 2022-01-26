# Ejercicio 1 - Pildoras Informaticas

# Crea un programa que pida dos numeros por teclado. El programa tendra una funcion llamada devuelveMax encargada de devolver el número más alto de los dos ingresados

num1 = int(input('Introduzca el primer digito: '))
num2 = int(input('Introduzca el segundo digito: '))

def devuelveMax(num1, num2):
    if num1 > num2:
        print(f'El numero mas alto es: {num1}')
    elif num2 > num1:
        print(f'El numero mas alto es: {num2}')
    else:
        print('Ambos numeros introducidos son iguales')
        
devuelveMax(num1, num2)

print('Fin del programa escrito por Moises')

# Metodo de solucion del profe Juan de Pildoras Informaticas

print('*****Metodo solucion profe*****')

def devuelve(n1, n2):
    if n1 < n2:
        print(n2)
    elif n1 > n2:
        print(n1)
    else:
        print('Son iguales')
        
print('El numero mas alto es: ')
    
devuelve(num1, num2)

print('Fin del programa escrito por el profe Juan de Pildoras Informaticas')