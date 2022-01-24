# Conjuntos

# Los conjuntos son un tipo de coleccion donde los elementos se agregan de forma desordenada. Donde su principal caracteristica es que no puede haber elementos duplicados

# El conjunto se invoca mediante set(), seguido de llaves {} para la creacion del conjunto

# Los conjuntos al igual que las listas y las tuplas pueden almacenar cualquier tipo de dato, incluso pueden almacenar datos de diferentes tipos.

# Dentro de los conjuntos NO puede abrir otro tipo de colecciones como listas, tuplas o incluso otro conjunto

conjunto = set() # El set sirve para especificar que sera un conjunto, ya que si solo se ponen las llaves, Python lo identifica como un diccionario. Este set se declara siempre y cuando se vaya a crear en un inicio un conjunto vacio y posteriormente se le vaya a agregar contenido con el metodo add(). Si el conjunto que se crea va a tener contenido desde un inicio, no es necesario el set(), ya que en el momento de asignar contenido al conjunto y estar separados por comas y no haber : en este, Python sabe que es un conjunto y no un diccionario

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

# A continuacion creamos un conjunto sin la necesidad del set(), debido a que desde la creacion inicial del conjunto se esta creando con contenido

# Se pueden comparar dos conjuntos para saber si son iguales y tienen el mismo contenido. Esto regresara un valor de tipo booleano como resultado

conjunto2 = {1,2,3}
conjunto3 = {3,4,5}

print('****Igualdad entre conjuntos****')

print(conjunto2 == conjunto3) # Aqui vemos que nos da como resultado False debido a que claramente no tienen el mismo contenido, pero que pasa si tuvieran el mismo contenido aunque fuera en diferente orden???

conjA = {1,2,3}
conjB = {2,1,3}

print(conjA == conjB) # Pues como se puede observar en el resultado este da True debido a que aunque el contenido esta en diferente orden este es igual

# Tambien podemos ocupar el metodo o la funcion len() para saber cuantos elementos tiene el conjunto

print('***Metodo len()***')

print(len(conjA))

# Union de dos conjuntos

print('***Union conjuntos***')

# Para unir o los elementos de dos conjuntos no nos vale el signo + como en las listas, para los conjuntos necesitamos el signo '|'. Esto debido a que a las listas las podemos concatenar, in embargo a los conjuntos no, a los conjuntos los juntamos y mas en concreto unimos sus elementos

conjA = {1,2,3}
conjA = {3,4,5}

conjC = conjA | conjB

print(conjC) # Recordar que en los conjuntos no puede haber elementos duplicados, es por eso que el 3 al estar repetido en ambos conjuntos al momento de la union solo queda uno

print('***Interseccion de conjuntos***')

# La intersección son aquellos elementos que se encuentran en ambos conjuntos

# Para la intersección se utiliza el signo de ampersan '&'

conjC = conjA & conjB

print(conjC) # El resultado es 3 debido a que es el unico elemento que cae en la intersección, ya que es el único elemento que se encuentra en ambos conjuntos y lo tienen en comun

print('***Diferencia de conjuntos***')

# La diferencia en los conjuntos son los elementos que tiene un conjunto y que no tiene el otro. Para la diferencia utilizamos el signo de guiñon medio '-'. Vaya los elementos que tiene el conjunto a con respecto a los que no tiene el conjunto b y visceversa

conjC = conjA - conjB
print(conjC)

conjC = conjB - conjA
print(conjC)

print('***Diferencia simetrica***')

# La diferencia simetrica son los elementos que se encuentran en los conjuntos pero que no estan en ambos conjuntos

conjC = conjA ^ conjB

print(conjC)

# Podemos saber si un conjunto es un subconjunto o superconjunto de otro. Para que esto de como resultado True ambos conjuntos que se comparen deben tener los mismos elementos

print('***subconjuntos y superconjuntos***')

conjA = {1,2,3}
conjB = {3,4,5}
conjC = {1,2,3,4,5}

print('***Subconjunto***')

print(conjA.issubset(conjC))
print(conjB.issubset(conjC))
print(conjC.issubset(conjA))

print('***Superconjunto***')

print(conjC.issuperset(conjA))
print(conjC.issuperset(conjB))
print(conjA.issuperset(conjC))
print(conjB.issuperset(conjC))

# Los conjuntos disconexos son aquellos conjuntos que no tienen ni un elemento en comun

print('***Conjuntos disconexos ***')

conjA = {1,2,3}
conjB = {3,4,5}

print(conjA.isdisjoint(conjB)) # El resultado el False ya que ambos conjuntos comparten al menos un elemento en comun

# En caso contrario de no compartir ni un elemento

conjA = {1,2,3}
conjB = {4,5,6}

print(conjA.isdisjoint(conjB)) # El resultado es True ya que ambos conjuntos no comparten ni un elemento en comun, todos sus elementos son diferentes, por lo tanto son conjuntos disconexos

# Tambien podemos convertir un conjunto en inmutable, como las tuplas, donde no se pueda agregar ni eliminar elementos. Esto se hace mediante el metodo frozenset()

conjA = frozenset({1,2,3})

# conjA.add(4) # Si esto lo descomentamos y lo tratamos de imprimir veremos que nos arroja con error, debido a que el conjunto tiene el metodo frozenset() y por lo tanto no podemos modificarlo de ninguna manera. De echo si imprimimos un conjunto congelado veremos que en la impresion en consola nos aparece el metodo frozenset()

print(conjA)