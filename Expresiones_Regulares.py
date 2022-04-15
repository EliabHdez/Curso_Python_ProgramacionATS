# Expresiones Regulares o regex - Pildoras Informaticas / Videos 69 y 70

# Metacaracteres, clases de caracteres y algunas expresiones regulares del modulo re

""" Las expresiones regualares son una secuencia de caracteres que forman un patron de busqueda

    Sirven para el trabajo y procesamiento de texto
    
    Algunos ejemplos serian:
    
        - Buscar un texto que se ajuste a un formato determinado (email)
        - Buscar si existe o no una cadena de caracteres dentro de un texto
        - Contar el numero de coincidencias dentro de un texto
        - Etc... """
        
# Para trabajar con regex hay que importar el metodo 're'. Este metodo almacena varias regex que podemos utilizar. Para ver todos las regex de este metodo podemos buscar en google regex en python y en la documentacion oficial encontraremos todos las regex disponibles en este metodo.

# En este archivo solo veremos algunas de estas regex

# Podemos crear nuestras propias expresiones regulares dentro de Python

import re

# ----- Regex search() -----

print('----- Regex search -----')

cadena = 'Vamos a aprender expresiones regulares'

texto_buscar = 'aprender'

# is not es el equivalente a !=, este 'is not' no lo hemos visto hasta ahora pero es mas que valido en python

if re.search(texto_buscar, cadena) is not None:
    print(f'Eh encontrado el texto "{texto_buscar}"')

else:
    print(f'No eh encontrado el texto "{texto_buscar}"')
    
texto_buscar = 'regex'

if re.search(texto_buscar, cadena) != None:
    print(f'Eh encontrado el texto "{texto_buscar}"')

else:
    print(f'No eh encontrado el texto "{texto_buscar}"')
    
# ----- Regex start() -----

print('----- Regex start -----')

# La regex start nos arroja como resultado el index o caracter donde comienza la palabra, el valor o caracter que le pasamos como parametro a buscar

indice_comienzo = 'expresiones'

texto_encontrado = re.search(indice_comienzo, cadena)

print(texto_encontrado.start())

# ----- Regex end() -----

print('----- Regex end -----')

# La regex end nos arroja como resultado el index o caracter donde finaliza la palabra, el valor o caracter que le pasamos como parametro a buscar

indice_comienzo = 'expresiones'

texto_encontrado = re.search(indice_comienzo, cadena)

print(texto_encontrado.end())

# ----- Regex span() -----

print('----- Regex span -----')

# La regex span nos arroja como resultado en forma de tupla los indices donde comienza y finaliza la palabra, el valor o caracter que le pasamos como parametro a buscar. Es un 2 es 1, hace el trabajo del start y del end en uno solo

indices = 'regulares'

texto_encontrado = re.search(indices, cadena)

print(texto_encontrado.span())

# ----- Regex findall() -----

print('----- Regex findall -----')

# La regex findall nos arroja como resultado en forma de lista todas las coincidencias que encontro de la palabra, el valor o caracter que le pasamos como parametro a buscar

cadena = 'Vamos a aprender expresiones regulares en Python. Python cuenta con una libreria o metodo que ya tiene expresiones regulares las cuales las podemos ocupar de forma libre. Estas expresiones son muy utilizadas a la hora de programar'

coincidencias = 'Python'

print(re.findall('Python', cadena))

print(re.findall('expresiones', cadena))

print(re.findall('regulares', cadena))

# Dentro de la lista que arroja el resultado del findall nos dara no el numero de veces que se repite una palabra, valor o caracter si no todas las coincidencias de estos ultimos, ya se una, dos, diez, cien etc. Pero ya con esto podemos saber cuantas veces se repite una palabra, valor o caracter con el metodo len por si llegasen a ser muchos no estar contando uno por uno para saber el numero de veces que se repite

print(len(re.findall('Python', cadena)),'- Son las veces que se repite la palabra Python en el texto')

print(len(re.findall('expresiones', cadena)),'- Son las veces que se repite la palabra expresiones en el texto')

print(len(re.findall('regulares', cadena)),'- Son las veces que se repite la palabra regulares en el texto')

print('')
print('----- EXPRESIONES REGULARES 2DA PARTE -----')
print('')

# metacaracteres (tambien se llegan a conocer como caracteres comodin)

# Anclas y clases de caracteres

# ----- Anclas -----

# Hay anclas de principio y fin y estas nos sirven para determinar busquedas que empiecen o terminen con una palabra, valor o caracter en especifico

# Lo que vamos a hacer a continuacion es usar anclas de principio (^) y fin ($) para buscar dentro de una lista personas que empiecen con un nombre en especifico asi como las personas que terminen con un apellido en especifico

lista_nombres = [
    'Ana Gomez',
    'Maria Martín',
    'Sandra López',
    'Santiago Martín',
    'Sandra Fernández'
]

print('----- Metacaracter inicio / Ancla ^ -----')

for elemento in lista_nombres:
    if re.findall('^Sandra', elemento):
        print(elemento)
        
print('----- Metacaracter fin / Ancla $ -----')
        
for elemento in lista_nombres:
    if re.findall('Martín$', elemento):
        print(elemento)
        
print('----- Ejemplos con urls -----')
        
lista_urls = [
    'http://paperforall.com',
    'ftp://paperforall.com',
    'http://paperforall.es',
    'ftp://paperforall.es',
    'http://paperforall.mx',
    'ftp://paperforall.mx'
]

print('--- Comienzo ftp ---')

for elemento in lista_urls:
    if re.findall('^ftp', elemento):
        print(elemento)
        
print('--- Termina es ---')
        
for elemento in lista_urls:
    if re.findall('es$', elemento):
        print(elemento)
        
print('--- Comienzo http ---')
        
for elemento in lista_urls:
    if re.findall('^http', elemento):
        print(elemento)
        
print('--- Termina com ---')
        
for elemento in lista_urls:
    if re.findall('com$', elemento):
        print(elemento)
        
print('--- Termina mx ---')
        
for elemento in lista_urls:
    if re.findall('mx$', elemento):
        print(elemento)
        
print('--- Termina com.mx ---')

for elemento in lista_urls:
    if re.findall('com.mx$', elemento):
        print(elemento)
    else:
        print('No hay urls con dominios .com.mx')


# Clases de caracteres --> Estos van entre corchetes [] y nos sirven como patron de busqueda, lo que vaya dentro de los cochetes es lo que va a buscar pero no necesariamente en el orden en el que se encuentren

print('----- Clases de caracteres -----')

lista_paginas = [
    'https://elpapeldelmañana.com',
    'https://paperforall.com',
    'https://labodegadepapel.com'
]

for elemento in lista_paginas:
    if re.findall('[ñ]', elemento):
        print(elemento)
        
# Vemos al imprimir que nos imprime la primer pagina ya que esta contiene en su nombre el caracter 'ñ'

# Tambien podemos hacer patrones de busquedas mas complejos o especificos

print('')

lista_seres = [
    'hombres',
    'mujeres',
    'niños',
    'niñas',
    'mascotas',
]

for elemento in lista_seres:
    if re.findall('niñ[oa]s', elemento):
        print(elemento)
        
# El patron de busqueda diferencia caracteres como el acento y tambien entre mayusculas y minusculas

print('')

lista_camion = [
    'camión',
    'camion',
    'Camion',
    'Camión'
]

for elemento in lista_camion:
    if re.findall('Cami[oó]n', elemento):
        print(elemento)