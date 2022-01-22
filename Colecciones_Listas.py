# Listas

# Las listas son estructuras de elementos muy flexibles ya que nos permiten almacenar cualqier tipo de datos en ellas y no necesariamente de un tipo de dato en concreto, podemos almacenar diferentes tipos de datos en la misma lista.

# Las listas en Python son el equivalente a los arreglos (arrays) en otros lenguajes de programacion.

# Podemos almacenar cadenas, enteros, flotantes, booleanos, otras listas etc y estan se crean a partir de corchetes []

lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

print(lista)

# Podemos recorrer las listas como cualquier otro arreglo, sin olvidar que al igual que en los arrreglos los elementos de las listas comienzan a contabilizarse en el indice 0 su primer elemento. Podemos indicar desde que posicion queremos empezar y hasta que posicion queremos finalizar, esto lo hacemos mediante :. Si no le especificamos alguno de los dos parametros estara empezando desde el inicio o bien terminando hasta el final.

# De igual manera podemos empezar desde el final hacia el inicio especificandolo con numeros negativos, donde -1 es el ultimo elemento de la lista y hacia atras siguen los siguientes elementos -2, penultimo elemento, -3 antepenultimo elemento y asi sucesivamente

print(lista[0])
print(lista[-1])
print(lista[-4])

print(lista[0:3]) # Al indicar hasta donde queremos que nos muestre es importante recordar que nos va a mostrar un elementos antes del numero que le especifiquemos, por ej en este caso, le estamos diciendo que llegue hasta el elemento con el indice 3, sin embargo no es este elemento hasta donde llegara o el ultimo que nos mostrara, ya que llega uno antes, por lo tanto nos estara mostrando hasta el elemento con el indice 2
print(lista[1:4])
print(lista[:3])
print(lista[3:])

# Como se menciono anteriormente se pueden crear listas con diferentes tipos de datos en una misma

lista2 = ['Moises', 'Hernandez', 31, 8.5, True, ['facebook', 25, 90, 5555555]]

print(lista2)

#Podemos saber el numero de elementos de una lista con el metodo len()

print('****lenght****')

listaUno = [1,2,3,4,5]

print(len(lista2)) # Las listas dentro de listas cuentan como un solo elemento
print(len(listaUno))

# Podemos agregar elementos a las listas. Para esto hay 3 diferentes metodos

""" Metodos para agregar elementos
        append() - Agrega un elemento al final de la lista
        insert() - Inserta un elemento en la lista. Este nos permite agregarlo en el lugar que queramos. Requiere de dos parametros, el primero es el numero de indice donde queremos insertar el elemento y el segundo el elemento a insertar
        extend() - Nos permite agregar varios elementos al final de la lista, para esto necesitamos capturar estos elementos en forma de lista [] ej extend([1,2,3]) """

print('****agregar elementos****')

print(listaUno)

listaUno.append(7)

print((listaUno))

listaUno.insert(5, 6)

print(listaUno)

listaUno.extend([8,9,10])

print(listaUno)

# Tambien podemos sumar o concatenar 2 listas

print('****concatenar listas****')

listaDos = [11,12,13,14,15]
listaTres = listaUno + listaDos # Aqui estamos concatenando dos listas y la listaUno se concatena junto con todos los cambios que se le realizaron atravez del programa, con los elementos desde el 1 hasta el 10

print(listaTres)

# Podemos saber si un elemento se encuentra en una lista o no con el metodo in. Este nos retornara un valor booleano, ya sea True o False

print('****elemento existente en la lista****')

listaUno = [1,2,3,4,5, 'Eliab']

print(5 in listaUno)
print('Eliab' in listaUno)
print('Hernandez'in listaUno)

# Tambien podemos saber el numero del indice de 'x' elemento con el metodo index(). Este metodo como se describio anteriormente nos arrojara como resultado el indice del elemento en cuestion

print('****numero de indice de un elemento****')

print(listaUno.index(3))
print(listaUno.index(5))
print(listaUno.index('Eliab'))

listaUno.extend([6,7,8,9,10])

print(listaUno.index(10))
# print(listaUno.index(11)) # Cuando se le pasa un elemento que no existe en la lista nos arroja un error, pero este error claramente nos especifica que el elemento no existe en la lista

# Tambien podemos saber cuantas veces se repite un elemento dentro de una lsita. Esto lo hacemos con el metodo count()

print('****numero de veces de un elemento en la lista****')

lista = [1,2,3,4,5,'Eliab',1,2,3,'Eliab',1,3,5]

print(lista.count(1))
print(lista.count('Eliab'))
print(lista.count(3))
print(lista.count(4))
print(lista.count(5))
print(lista.count(10))

# Tambien podemos eliminar elementos de una lista, con los metodos pop(), remove() y clear()

""" Metodos para eliminar elemenetos de una lista
        pop() - Elimina un elemento a la vez, si no se le pasa ningun parametro, este metodo eliminara el ultimo elemento elemento de la lista. El parametro que recibe o se le puede pasar es el indice del elemento que queremos eliminar.
        remove() - Elimina el elemento que le pasemos como parametro. Asi que el parametro que recibe es directamente el elemento que queremos eliminar
        clear() - Elimina todos los elementos de la lista. Limpia la lista y la deja vacia """

print('****eliminar elementos****')

lista = [1,2,3,4,5,'Eliab',1,2,3,'Eliab',1,3,5]

lista.pop()
print(lista)
lista.pop(2)
print(lista)
lista.remove('Eliab') # Si hay varios elementos iguales en una lista, al momento de remover alguno de estos elimina el primero que encuentra
print(lista)
lista.clear()
print(lista)

# Se puede invertir el sentido de la lista

print('****invertir / voltear lista****')

lista = [1,2,3,'Meraxes']

lista.reverse()

print(lista)

# Podemos duplicar el contenido de la lista, en el mismo orden que se encuentra las veces que desemos

print('****duplicar contenido****')

lista = [1,2,3,'Meraxes']*2

print(lista)

lista = [1,2,3,'Meraxes']*3

print(lista)

# Algo que tambien podemos hacer y que podria resultar bastante util seria ordenar los elementos de una lista. Este metodo sirve siempre y cuando los elementos sean de tipo numerico

print('****ordenar elementos****')

lista = [5,4,-6,9,0,1,2]

lista.sort() # El metodo sort ordena los elementos de forma ascendente

print(lista)

# Que pasa si queremos ordenar los elementos de forma descendente. Pues solo aplicamos un reverse
lista.sort(reverse=True)

print(lista)

# Veamos que pasa cuando hay otro tipo de dato que no sea numerico

listaPrueba = ['World', 'Hello', 5, 3, 1, -10]

# listaPrueba.sort() # No se puede ocupar el metodo sort() cuando la lista contiene datos que no son numericos, marca error!!!

# print(listaPrueba)