# Diccionarios

# Son otro tipo de colección que de igual manera a los conjuntos los elementos se almacenan de forma desordenada.

# La principal caracteristica de los diccionarios es que tienen dos elementos por posición,la clave y el valor. En estos no puede haber claves duplicadas, estas tienen que ser unicas

# Los diccionarios tienen la caracteristica de que dos elementos de su contenido van de la mano, esto quiere decir que la clave va ligada al valor y estas se separan por dos puntos (:), estos valores por decirlo de alguna manera equivalen uno al otro, pero en otro sentido

# Para los diccionarios basta con poner las llaves, ya que si esta vacio de entrada Python sabra que es un diccionario, y si no lo esta, de acuerdo al contenido Python sabra si es un diccionario o un conjunto, esto lo hace mediante la clave, el valor y los dos puntos que unen estos dos ultimos, mientras que en los conjuntos solo hay valores y estos estan separados por comas. En los diccionarios tanto la clave como el valor corresponden a una sola posicion, digamos que para el indice ambos cuentan como uno solo. Primero se pone la clave y depues el valor ('clave':'valor')

diccionario = {'azul':'blue', 'rojo':'red', 'verde':'green'}

print(diccionario)

# Podemos mandar a llamar solo un valor del diccionario mediante su clave

print(diccionario['rojo'])
print(diccionario['verde'])

# Tambien podemos agregar mas elementos al diccionario, asi como modificar los elementos ya existentes. Para ambos casos se ocupa la misma forma o metodo y este es declarando el diccionario, entre corchetes y asignando el nuevo valor para el nuevo elemento o el nuevo valor para el elemento ya existente

diccionario['azul'] = 'BLUE' # Aqui lo unico que estoy cambiando es el nombre a puras mayusculas. Estoy modificando un elemento ya existente
diccionario['amarillo'] = 'yellow' # Aqui estoy agregando un nuevo elemento

print(diccionario)

# Tambien podemos eliminar elementos del diccionario y para este usamos la funcion del(), la cual lleva como parametro el diccionario al cual le vamos a eliminar un elemento y dentro de corchetes el elemento a eliminar

del(diccionario['amarillo'])

print(diccionario)

# Los diccionarios al igual que otra colecciones pueden almacenar cualquier tipo de dato y tambien estos datos de diferente tipo pueden estar en un mismo diccionario

personalEmpresa = {'Moises':{'edad':31,'sexo':'masculino', 'estatura':1.76}, 'Nahun':[48,'Arquitecto'], 'Efrain':[33,1.83]}

print(personalEmpresa)
print(personalEmpresa['Moises'])
print(personalEmpresa['Nahun'])
print(personalEmpresa['Efrain'])

print('*****Diccionarios Parte II*****')

motoGP = {46:'Valentino Rossi', 93:'Marc Márquez', 99:'Jorge Lorenzo', 26:'Dani Pedrosa'}

print(motoGP)
print(motoGP[93]) # En los diccionarios es importante no confundir la clave con el indice, ya que cuando queremos solicitar un elemento en especifico del diccionario, utilizamos corchetes y dentro de estos anotamos la clave del elemento que queremos ver y esto se puede prestar para una confusion pensando que estamos diciendole al programa que queremos el elemento en el indice 99 por ejemplo en este caso, cuando no es asi, mas bien el 99 corresponde a la clave de un elemento que se encuentra dentro del diccionario
print(motoGP[46])

# Hay dos maneras de mostrar u obtener la informacion del contenido de un diccionario. La primera es poniendo directamente entre corchetes la clave del elemento, sin embargo con esta forma, necesitas estar seguro del contenido del diccionario y de que la clave que estas poniendo existe y pertenece a un elemento, de lo contrario estaria arrojando un error, ya que no estaria encontrando la clave ni ningun valor correspondiente a esta

# La segunda manera es mediante el metodo get() y la ventaja de este metodo es que si no existe la clave que estamos solicitando podemos hacer una anotacion o poner un mensaje el cual se nos estaria mostrando al momento de no encontrar la clave solicitada y estariamos evitando como tal el error

print('*****Obtencion de datos mediante corchetes y metodo get()*****')

print(motoGP[99])
# print(motoGP[4]) # Como podemos ver al momento de ejecutar esta linea, la consola nos arroja un error debido a que no encuentra esa clave dentro del diccionario
print(motoGP.get(26, 'No existe ese numero de piloto'))
print(motoGP.get(4, 'No existe ese numero de piloto'))
print(motoGP.get(29, 'No existe ese numero de piloto')) # En los ultimos dos casos vemos que aunque no existe la clave 4 y 29 dentro de nuestro diccionario al momento de ejecutar la consola no nos esta arrojando ningun error como en el caso anterior que esta comentado, si no que por el contrario nos arroja el mensaje que pusimos en el metodo get si este no encontraba la clave solicitada, esto hace que el programa no se detenga por un error

# Podemos utilizar el metodo in como en las listas etc para buscar o confirmar la existencia de un elemento dentro de nuestro diccionario

print(46 in motoGP)
print(93 in motoGP)
print(4 in motoGP)

print('*****Solicitud de claves o valores*****')

# Tambien podemos realizar busquedas o mas que busqueda solicitar que claves o valores contiene nuestro diccionario, en lugar de que nos salga todo el contenido, nos mostraria uno en especifico, ya sea las claves o los valores existentes, dependiendo de lo solicitado

# Esto lo hacemos mediante los metodos keys() para las claves y values() para los valores

print(motoGP.keys()) # El metodo key() nos muestra todas las claves del diccionario, solo las claves
print(motoGP.values()) # El metodo values() nos muestra todos los valores del diccionario, solo los valores

# De igual forma podemos solicitar el contenido completo poniendo el nombre del diccionario, pero tambien lo podemos hacer mediante el metodo items(), el cual nos mostrara todo los elementos, pero este lo hara en forma de lista y cada elemento conformado por su clave y valor en un tupla

print(motoGP.items()) # Como se menciono anteriormente todos el contenido del diccionario se encuentra en una lista pero cada clave con su valor esta almacenado en una tupla

# Tambien podemos ocupar el metodo len() para saber cuantos elementos conforman el diccionario

print(len(motoGP))

# Podemos ocupar el metodo clear() para limpiar y vaciar el diccionario

motoGP.clear()
print(motoGP)