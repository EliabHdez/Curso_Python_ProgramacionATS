# Conjuntos

# Los conjuntos son un tipo de coleccion donde los elementos se agregan de forma desordenada. Donde su principal caracteristica es que no puede haber elementos duplicados

# El conjunto se invoca mediante set(), seguido de llaves {} para la creacion del conjunto

# Los conjuntos al igual que las listas y las tuplas pueden almacenar cualquier tipo de dato, incluso pueden almacenar datos de diferentes tipos.

# Dentro de los conjuntos NO puede abrir otro tipo de colecciones como listas, tuplas o incluso otro conjunto

conjunto = set() # El set sirve para especificar que sera un conjunto, ya que si solo se ponen las llaves, Python lo identifica como un diccionario

conjunto = {1,2,3,'Hola', 4.56}

print(conjunto)

# Para agregar elementos a un conjunto se emplea el metodo add()

print('*****agregar elementos*****')

conjunto.add(5) # En los conjuntos al momento de agregar elementos no es como con las listas que el metodo mas basico para agregar añade el elemento al final, en los conjuntos al ser grupos de elementos desordenados agrega los nuevos elementos de forma aleatoria, donde el metodo quiera

print(conjunto)

conjunto.add('Adios')
conjunto.add('z')

print(conjunto)

# Para eliminar elementos se emplea el metodo discard(). A este se le pasa como parametro directamente el elemento a eliminar

print('*****eliminar elementos*****')

conjunto.discard('Adios')

print(conjunto)

# De igual manera podemos limpiar o vaciar el conjunto con el metodo clear()

conjunto.clear()

print(conjunto) # Como podemos observar aqui cuando corremos el programa no nos quedas las llaves vacias, si no que directamente podemos ver que nos arroja el set(), que es como que la base del conjunto y apartir de este set(), de esta base ya creamos el conjunto con las llaves

# Tambien se puede buscar un elemento en especifico con el in

print('*****existencia de elementos*****')

conjuntoUno = set()
conjuntoUno = {1,2,3,'Hello', 'World'}

print(3 in conjuntoUno)
print('Hello' in conjuntoUno)
print('Mundo' in conjuntoUno)

# Tambien se pueden generar negaciones en el in

print('*****negacion en el in*****')

print('World' not in conjuntoUno)
print(5 not in conjuntoUno)