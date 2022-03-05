# Archivos Externos --> Trabajar con ficheros externos de texto con el modulo 'io'

""" Objetivo de trabajar con archivos externos:
    
    - Persistencia de datos: Es la posibilidad de guardar los datos que se han estado utilizando en la aplicacion o en el programa para que no se pierdan 
    
    A la hora de almacenar datos tenemos dos opciones o alternativas
    
    Alternativas:
        
        - Manejo de archivos externos --> Guardar los datos en archivos externos
        
        - Trabajo con BBDD: Guardar la informacion o datos en base de datos """
        
""" Fases necesarias para guardar informacion en archivos externos

    - Creación
    - Apertura
    - Manipulación
    - Cierre """
    
""" Diferencias entre el modo write (w) y el modo append (a)

    - El modo escritura nos permite añadir contenido pero este contenido sustituye el contenido actual, es decir borra el contenido que tiene actualmente el archivo para sustituirlo por el nuevo contenido que estamos definiendo en el modo write

    - El modo append nos permite añadir contenido sumandolo al contenido actual que ya tiene. El contenido que agregamos con el append se incorpora al archivo despues del contenido que este ya tiene """
    
# Esto de los archivos externos es algo confuso, pero a como lo entendi es poder crear archivos, si es que no existen utilizando codigo mediante el modulo 'io', si ya existen se pueden manipular los existentes o los que python crea al momento. Estos archivos se cierran y se abren pero ojo, esto de abrir y cerrar no es como dar doble click en el archivo para abrirlo y pulsar en la X para cerrarlo, no es esto, es abrir o cerrar el espacio en memoria para poder interactuar con ellos

# Si el archivo no existe, python lo crea

# Para que los cambios surtan efecto, desde que el archivo sea creado por python hasta lo que agreguemos al archivo en modo escritura es necesario ejecutar el codigo, no basta con guardar los cambios en el editor de texto, es necesario ejecutar el programa si o si

# A continuacion podemos ver en el ejemplo las fases que corresponden a los archivos externos

from io import open

archivo_texto = open('archivo_texto.txt', 'w') # Creacion y apertura. Abierto en modo escritura (w)

texto = 'Katana esta en la ventana... \nChismorreando como siempre!!!'

archivo_texto.write(texto) # Manipulacion

archivo_texto.close() # Cierre

# Abrir programa en modo lectura (r)

archivo_read = open('archivo_texto.txt', 'r')

leer_contenido = archivo_read.read()

archivo_read.close()

print(leer_contenido)

archivo_read.close()

# Metodo readlines() --> Este metodo lo que hace es guardar la informacion en una lista. Cada linea de texto que conforma el contenido es un elemento de la lista

archivo_read2 = open('archivo_texto.txt', 'r')

lineas_texto = archivo_read2.readlines()

archivo_read2.close()

print(lineas_texto)

archivo_read2.close()

# Podemos hacer con esta lista devuelta por el metodo readlines lo mismo que hariamos con una lista cualquiera creada en un principio como tal

print('---Imprimiendo el primer elemento de la lista---')
print(lineas_texto[0])

print('---Imprimiendo el segundo elemento de la lista---')
print(lineas_texto[1])

# append (a) --> Este sirve para agregar informacion a un archivo

archivo_append = open('archivo_texto.txt', 'a')

archivo_append.write('\nLe encanta estar asomada y sacar la cabeza')

archivo_append.close()

print('-----Manejo del puntero en archivos externos-----')

# Como manejar el puntero dentro de un fichero de texto

# Esto nos permitara trabajar solo con cierto texto del archivo

archivo_texto2 = open('archivo_texto.txt', 'r')

print(archivo_texto2.read())

# Cuando trabajamos con archivos externos estos no se comportan de la misma manera que el codigo, un ejemplo de esto es que aqui podemos ver que tenemos dos veces print con el mismo codigo en el interior de los parentesis, pero al momento de ejecutar el programa e imprimirlo en consola el segundo no se imprime, no como cuando trabajmos con codigo normal que podemos imprimir lo mismo cuantas veces queramos y esto se debe a la posicion del puntero en el archivo de texto externo que estamos leyendo e imprimiendo
print(archivo_texto2.read())

# Este archivo de texto al abrirlo podremos ver que el puntero se encuentra al inicio del texto, pero despues de haberlo leido una vez este puntero termina al final del texto y ahi se queda, entonces al momento de volverle a dar el siguiente print ya no nos imprime nada en consola porque en el archivo ya no hay nada que leer despues de la posicion del puntero el cual se encuentra al final del texto

# Podemos manipular la posicion del puntero para asi conseguir trabajar o utilizar cierto contenido del texto, en este caso como tener 2 print tener algo mas que leer e imprimir al momento de ejecutar el segundo print y esto lo hacemos con el metodo seek(), el cual nos permite pasarle un valor el cual hara referencia a la posicion en la que se ubicara el puntero. Este metodo no hace que el puntero al momento de leer el archivo termine en esa posicion, si no que el puntero regrese a esa posicion despues de haber leido todo el texto. En lugar de quedarse al final del texto este se coloca en la posicion asignada en el metodo seek()

print('-----Metodo seek()-----')

archivo_texto2.seek(11)

print(archivo_texto2.read())

# Tambien el metodo read() nos sirve para posicionar el puntero en una posicion, sin embargo hay una diferencia entre el metodo seek y el metodo read cuando lo ocupamos para posicionar el puntero y esta es que el metodo seek() lo posiciona en la ubicacion que le indiquemos, mientras read(valor) hace una lectura hasta el valor que le hayamos definido

archivo_texto2.seek(0) # Posicione el puntero en indice 0 para que empiece la lectura al principio del archivo y no tener que comentar el seek de arriba, ya que si no posiciono el puntero al inicio, este despues de la lectura del primer seek que se encuentra arriba se quedaria al final del texto

print('-----Metodo read(valor) para posicionar el puntero-----')

print(archivo_texto2.read(11)) # Como podemos observar con el read(valor) lo que conseguimos es lea hasta la posicion que le hemos indicado se coloque el puntero, que en este caso es al final de la palabra 'esta', abarcando nada mas 'Katana esta'

print(archivo_texto2.read()) # Aqui podemos ver que aunque tenemos un segundo read si nos imprime en consola texto, ya que el read anterior tiene un valor (11) y esto hace que al final de esa lectura el puntero se quede en esa posicion y por lo tanto el siguiente read() empezara a leer desde esa posicion hasta el final del texto

# Apartir de esto podemos hacer diferentes cosas como posicionar el puntero en medio del texto, como hariamos esto?

archivo_texto2.close()

print('---Archivo texto 3---')

archivo_texto3 = open('archivo_texto.txt', 'r')

archivo_texto3.seek(len(archivo_texto3.read())/2)

print(archivo_texto3.read())

archivo_texto3.close()

print('---archivo texto 4---')

archivo_texto4 = open('archivo_texto.txt', 'r')

archivo_texto4.seek(len(archivo_texto4.readline()))

print(archivo_texto4.read())

archivo_texto4.close()

print('---archivo texto 5---')

archivo_texto5 = open('archivo_texto.txt', 'r+') # Abierto en modo lectura y escritura

archivo_texto5.write('Inicio del texto') # Estos cambios los podemos ver si abrimos el archivo desde la carpeta donde se encuentra

archivo_texto5.close()

print('---archivo texto 6---')

archivo_texto6 = open('archivo_texto.txt', 'r+')

# print(archivo_texto5.readlines())

lista_texto = archivo_texto6.readlines()

lista_texto[1] = 'Dandose un llegue de aire fresco \n'

print(lista_texto)

archivo_texto6.seek(0)

archivo_texto6.writelines(lista_texto)

print(archivo_texto6.read())

archivo_texto6.close()