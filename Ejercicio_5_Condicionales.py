# Ejercicio 5 - Cajero Automático

""" Hacer un programa que simule un cajero automático con un saldo inicial de $1000 y tendrá el siguiente menú de opciones

    1 - Ingresar dinero a la cuenta
    2 - Retirar dinero de la cuenta
    3 - Mostrar dinero disponible
    4 - Salir """

saldoInicial = 1000

titleMenu = '\t.:MENU:.' # \t significa tabulacion de 4 espacios. Los puntitos solo es decoracion
# opsMenu = "1-Ingresar dinero en la cta   2-Retirar dinero de la cta   3-Mostrar saldo disponible   4-Salir"

print(titleMenu)
print('1. Ingresar dinero en la cuenta')
print('2. Retirar dinero de la cuenta')
print('3. Mostrar saldo disponible')
print('4. Salir')
# print(opsMenu)

opcion = int(input('\nDigite la opcion deseada > '))

if opcion == 1:
    ingresar = float(input('Digite el monto a ingresar: '))
    if ingresar > 0:
        saldoInicial += ingresar
        print(f'Su saldo actual es de: {saldoInicial:.2f}')
        print('\nGracias por usar nuestro cajero')
    else:
        print('El monto ingresado no es válido')
elif opcion == 2:
    retirar = float(input('Ingrese la cantidad a retirar: '))
    if retirar > saldoInicial:
        print('\nSaldo insuficiente')
    elif retirar > 0:
        saldoInicial -= retirar
        print(f'Su saldo actual es de: {saldoInicial:.2f}')
        print('\nGracias por usar nuestro cajero')
    else:
        print('El monto ingresado no es válido')
elif opcion == 3:
    print(f'Su saldo disponible es: {saldoInicial:.2f}')
    print('\nGracias por usar nuestro cajero')
elif opcion == 4:
    print('Gracias por usar unuestro cajero automático')
else:
    print('Opción de menú no válida')