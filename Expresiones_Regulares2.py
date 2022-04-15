# Expresiones Regulares 2 - Pildoras Informaticas / Videos 71 y 72

# Rangos, Match y Search

# Rangos

# Diferencia entre mayusculas y minusculas

""" Metacaracteres / Anclas --> '^', '$' (Inicio / Fin)
    Clases de caracteres --> []
    Rangos --> Determinar un rango especifico: ej de una letra a otra. Este rango se especifica dentro de los corchetes (clases de caracteres) """

import re

lista_nombres = [
    'Moises',
    'Efrain',
    'Nahun',
    'Arnulfo',
    'Lilia',
    'Susett',
    'Sandra'
]

print('--- Nombres que contengan las letras entre la o y la t en ellos ---')

for element in lista_nombres:
    if re.findall('[o-t]', element):
        print(element)
        
print('--- Nombres que comiencen con las letras entre la O y la T ---')

for element in lista_nombres:
    if re.findall('^[O-T]', element):
        print(element)
        
print('--- Nombres que terminan con las letras entre la o y la t ---')

for element in lista_nombres:
    if re.findall('[o-t]$', element):
        print(element)
        
# Como podemos observar los rangos van de la mano con las clases de caracteres y se pueden utilizar en conjunto con los metacaracteres para generar busquedas mas detallas o especificas

# Los rangos suelen ser bastantes utiles cuando tenemos codigos como de productos, zonas, clientes etc dentro de una lista

# Supongamos que creamos un programa que determine mediante el numero de cliente el numero de pedido que ha hecho y que estos los queremos filtrar o mostrar ya sea de acuerdo al codigo del cliente o a numeros de pedidos similares etc

print('--- Numero de pedidos de un cliente mediante el rango ---')

lista_pedidos = [
    'Mo-1',
    'Ef.1',
    'Na:1',
    'Mo-2',
    'Ar.1',
    'Ar.2',
    'Li:1',
    'Na-2',
    'Li:2',
    'Ef.2',
    'Mo-3',
    'Li:3',
    'Mo-4',
    'Mo-A',
    'Mo-5',
    'Mo-B',
    'Mo-C'
]

for element in lista_pedidos:
    if re.findall('Mo-[0-3]', element):
        print(element)
        
# Podemos generar el resultado inverso, que en ves de que nos arroje del 0 al 3, sean estos los que no tome en cuenta, y esto lo hacemos con el acento circunflejo, de esta manera estamos como invirtiendo o negando el rango, no entendi muy bien como funciona y porque, pero de esta manera generamos el resultado contrario o inverso

print('--- Resultado inverso del anterior ---')

for element in lista_pedidos:
    if re.findall('Mo-[^0-3]', element):
        print(element)
        
print('--- Resultado mezclando diferentes caracteres ---')

for element in lista_pedidos:
    if re.findall('Mo-[0-3A-B]', element):
        print(element)
        
print('--- Resultado con signos ---')

for element in lista_pedidos:
    if re.findall('[.:]', element):
        print(element)
        
# De igual manera podemos filtras estos resultados con el codigo de un cliente en concreto

print('--- Filtrado por un cliente en concreto ---')

for element in lista_pedidos:
    if re.findall('Ar[.:]', element) or re.findall('Li[.:]', element):
        print(element)
        
print('--- Filtrado por un cliente en concreto 2 ---')

for element in lista_pedidos:
    if re.findall('Ef[.:]', element) or re.findall('Na[.:]', element):
        print(element)
        
# Funciones match y search

# match() --> Busca si hay coincidencias en un patron de busqueda al comienzo de una cadena de texto, siempre al comienzo.

# La funcion match distingue entre mayusuclas y minusculas

# De entrada lleva 2 parametros, el primero es el patron de busqueda y el segundo es con quien lo queremos comparar o donde lo queremos buscar. Adicional acepta un tercer parametro que hace referencia a lo que se denomina 'flag'. Este tercer parametro es para el case sensitive, para que no haga distincion entre mayusculas y minusculas y el parametro es re.IGNORECASE

print('----- Funcion match() -----')

nombre_uno = 'Sandra López'

nombre_dos = 'Antonio Gómez'

nombre_tres = 'María López'

if re.match('Sandra', nombre_uno):
    print('Nombre encontrado')
else:
    print('Nombre NO encontrado')
    
if re.match('Sandra', nombre_dos):
    print('Nombre encontrado')
else:
    print('Nombre NO encontrado')
    
if re.match('sandra', nombre_uno):
    print('Nombre encontrado')
else:
    print('Nombre NO encontrado')
    
if re.match('Sandra', nombre_uno, re.IGNORECASE):
    print('Nombre encontrado')
else:
    print('Nombre NO encontrado')
    
# Podemos utilizar el punto que sirve como comodin

print('--- Comodin punto (.) ---')

nombre_uno = 'Jara Lopez'

nombre_dos = 'Lara Croft'

if re.match('.ara', nombre_uno):
    print(f'Se ha encontrado el nombre {nombre_uno}')
else:
    print('No se ha encontrado ninguna coincidencia')
    
if re.match('.ara', nombre_dos):
    print(f'Se ha encontrado el nombre {nombre_dos}')
else:
    print('No se ha encontrado ninguna coincidencia')
    
# Cadenas que empiecen con numeros

# Hay una expresion regular en Python la cual es \d, esta lo que hara ver si la cadena comienza con un numero o no. Con match buscara al inicio, ya que match siempre busca al comienzo

print('--- Cadenas con numeros ---')

cadena_uno = '51349'

cadena_dos = 'a56457'

if re.match('\d', cadena_uno):
    print('La cadena comienza con un numero')
else:
    print('La cadena NO comienza con un numero')
    
if re.match('\d', cadena_dos):
    print('La cadena comienza con un numero')
else:
    print('La cadena NO comienza con un numero')
    
# Funcion search() --> Busca si hay coincidencias en un patron de busqueda en toda la cadena de texto

print('----- Funcion search() -----')

nombre_uno = 'Sandra López'

nombre_dos = 'Antonio Gómez'

nombre_tres = 'María López'

if re.search('Lopez', nombre_uno):
    print('Se ha encontrado el apellido López')
else:
    print('No se ha encontrado el apellido López')
    
if re.search('L[oó]pez', nombre_uno):
    print('Se ha encontrado el apellido López')
else:
    print('No se ha encontrado el apellido López')
    
codigo_uno = 'kjskdhf jsdklfid71fjek njvbnvcxlk sdkjfdf'

codigo_dos = 'hjshdus71ksdj fijdifdñdf kodkfo'

codigo_tres = 'mnjdhfui ewioejf nklsc jpomd'

if re.search('71', codigo_uno):
    print('Se a encontrado el numero 71')
else:
    print('No se ha encontrado el numero 71')
    
if re.search('71', codigo_dos):
    print('Se a encontrado el numero 71')
else:
    print('No se ha encontrado el numero 71')
    
if re.search('71', codigo_tres):
    print('Se a encontrado el numero 71')
else:
    print('No se ha encontrado el numero 71')