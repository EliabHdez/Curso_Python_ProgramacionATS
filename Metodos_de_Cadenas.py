# Metodos de cadenas

# Los metodos de cadenas son aquellos metodos que nos permiten interactuar con los strings (cadenas de texto), ya sea para conocer algo en particular o modificar en algun punto estas cadenas de texto

""" Algunos de estos metodos, son los siguientes. Que si bien no son los mas importantes si pueden ser de los mas utilizados

    - upper() --> Convierte las letras en mayusculas
    - lower() --> Convierte las letras en minusculas
    - capitalize() --> Pone la primer letra del string en mayuscula
    - count() --> Indica cuantas veces se repite una letra o una cadena dentro de un texto
    - find() --> Representa el indice (posicion) de un caracter o grupo de caracteres dentro de un texto
    - isdigit() --> Comprueba si un valor es numerico, es un digito o no lo es
    - isalum() --> Comprueba si un valor es alphanumerico
    - isalpha() --> Comprueba si hay solo letras (los espacios en blanco no los toma en cuenta)
    - split() --> Separa por palabras usando espacios
    - strip() --> Eliminas los espacios vacios o sobrantes al principio y al final
    - replace() --> Reemplaza una letra o palabra por otra dentro de un string
    - rfind() --> Comprueba el indice (posicion) de un caracter al igual que el find() solo que este lo hace empezando el conteo desde atras, es decir de derecha a izquierda """
    
nombre_usuario = input('Introduce tu nombre de usuario: ')

print(f'Tu nombre de usuario es: {nombre_usuario}')
print(f'Tu nombre de usuario es: {nombre_usuario.upper()}')
print(f'Tu nombre de usuario es: {nombre_usuario.lower()}')
print(f'Tu nombre de usuario es: {nombre_usuario.capitalize()}')

edad = input('Introduce tu edad: ')

while (edad.isdigit() == False):
    print('Introduce un valor numerico correspondiente a tu edad')
    
    edad = input('Introduce tu edad: ')
    
if int(edad) < 18:
    print('No se puede generar tu registro')
    
else:
    print('Ya puedes generar tu registro')