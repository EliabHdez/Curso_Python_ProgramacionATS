# Tuplas

# Las tuplas son otro tipo de Colecciones, estas son muy parecidas a las Listas, las diferencias radican en dos puntos. El primero es que estan se generan entre parentesis () y la segunda es que son inmutables, es decir, no se pueden modificar de ninguna manera, esto quiere decir que no vamos a poder agregar, modificar y/o eliminar elementos

# Las listas y las tuplas son como las variables y las constantes en JavaScript, donde la variable puede empezar teniendo un valor y a medida que avanza el programa cambiar su valor, a diferencia de las constantes, las cuales no puede cambiar su valor y todo el programa se queda con el valor asignado desde el principio. En las listas y las tuplas en Python es lo mismo, donde las listas vendrian siendo las variables y poder cambiar y modificar sus elementos y su contenido, mientras las tuplas son las constantes y estas no puede sufrir alteracion alguna y se quedan con los valores asignados inicialmente durante todo el programa

tupla = (4, 'Hola', 6.78, [1,2,3], 4)

# tupla[0] = 8 # Esto seria una forma de modificar un elemento de una lista, sin embargo en la tuplas esto no es posible, si lo descomentamos y corremos el programa veremos que esto nos da un error

print(tupla)
print(tupla[1])

# Con las tuplas se pueden usar los mismo metodos que con las listas, metodos como len(), index(), count(), buscar por medio del in, seleccionar apartir de que elemento y hasta que elemento queremos ver etc...

print(4 in tupla)
print('Hola' in tupla)
print(tupla[1:4])
print(len(tupla))
print(tupla.index(6.78))
print(tupla.index('Hola'))
print(tupla.count(4))

tupla2 = ('moises', 'hernandez')*2

print(tupla2)

# Adicionalmente se pueden convertir tuplas en listas y listas en tuplas

tuplaUno = ('Tupla', 'de', 'Prueba')
print(tuplaUno)

listaUno = list(tuplaUno)
print(listaUno)

listaDos = ['Lista', 'de', 'Prueba']
print(listaDos)

tuplaDos = tuple(listaDos)
print(tuplaDos)

# Para efectos de ejecucion, las tuplas son mas rapidas y no consumen tantos recursos como las listas