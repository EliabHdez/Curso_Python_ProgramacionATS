# BBDD I / Bases de Datos - Pildoras Informaticas / Videos 55 y 56

# SQL (Structured Query Language) --> Es el lenguaje de las bases de datos, con este es posible manejar base de datos con cualquier lenguaje de programacion

""" Creación de BBDD
        - Conexión con BBDD
        - Inserción de registros en BBDD 
    
    SGDB (system gestor database) y Python
        Python es capaz de trabajar con diferentes gestores de base de datos como por ejemplo
            - SQL Server
            - Oracle
            - MySQL
            - SQLite
            - PostgreSQL
            - Etc... """
            
""" SQLite
        - Sistema de gestion de BBDD relacional
        - Escrito en C, es de codigo abierto
        - Forma parte integral del programa
        - Se guarda como un unico fichero en host 
        
    Ventajas
        - Ocupa muy poco espacio en disco y memoria
        - Muy eficiente y rapido
        - Multiplataforma
        - Sin administracion / configuracion
        - Dominio publico. Sin costo
        
    Desventajas
        - No admite clausulas anidadas (where)
        - No existen usuarios (no acceso, simultaneo por parte de varios usuarios a la vez)
        - Falta de clave foranea cuando se crea en modo consola """
        
""" Pasos a seguir para conectar con BBDD

    1.- Abrir / Crear conexion
    2.- Crear puntero: El puntero es un objeto que se crear que nos permitira hacer 2 cosas; ejecutar querys / consultas y manejar los resultados, es decir nos permitira hacer los pasos 3 y 4
    3.- Ejecutar query (consulta) SQL
    4.- Manejar los resultados de la query (consulta)
        - Insertar, Leer, Actualizar, Borrar (Create, Read, Update, Delete) - CRUD 
    5.- Cerrar puntero
    6.- Cerrar conexion """
    
# No es necesario poner las instrucciones de sql en mayusculas, lo estoy haciendo asi ya que estoy siguiendo la forma en que lo hace el profe y el tiene la maña de poner las instrucciones de sql en mayusculas, pero hay que tener claro que esto no forzosamente tiene que ser asi

# A los datos o la informacion de la base de datos tambien se le conocen como registros
            
import sqlite3

conexion = sqlite3.connect('Date Base 1') # Aqui generamos la conexion con la base de datos. Si esta base no llegara a existir, con esto mismo se estaria creando la base de datos, asignandole el nombre que hemos definido

puntero = conexion.cursor() # Creamos el cursor o puntero

# puntero.execute('CREATE TABLE PRODUCTOS (NOMBRE VARCHAR(50), PRECIO INTEGER, CATEGORIA VARCHAR(20))') # Creamos la tabla que va a contener la base de datos y que almacenara los datos que vayan dentro de esta tabla. Esta despues de crearla y ejecutar el programa para que se cree y se vea reflejada en la base de datos despues de guardar el archivo y ejecutar hay que comentar la linea, quitarla o lo que sea pero esta linea de codigo no tiene que volverse a ejecutar ya que estaria arrojando un error al momento de correr el programa

# varchar = cadena de texto o string y el valor entre parentesis hace referencia al numero maximo de caracteres que podra tener esta string

# integer = valor de tipo numerico

# puntero.execute('INSERT INTO PRODUCTOS VALUES("CAJA PAPEL BOND TAMAÑO CARTA MARCA SCRIBE", 980, "Papel Bond")') # Agregamos datos o informacion a la tabla.

# Posterior a esto hay que decirle al programa que vamos a aceptar los cambios o modificaciones que estamos generando y esto lo hacemos mediante el metodo commit()

# Se pueden insertar lotes de registros utilizando listas y tuplas (con lotes de registros nos referimos a varios datos a la vez), y esto lo hacemos de la siguiente manera

# Creamos una lista con tuplas dentro que contendran los datos qe vamos a añadir a la tabla de la base de datos

# listaProductos1 = [
#     ('Cinta de empaque trasnparente', 55, 'Cintas'),
#     ('Playo Calibre 60', 180, 'Playo'),
#     ('Hielera de Unicel', 30, 'Unicel')
# ]

# Posteriormente tenemos que agregar esta lista con los datos a la base de datos

# puntero.executemany('INSERT INTO PRODUCTOS VALUES (?,?,?)', listaProductos1) # Utilizamos el metodo executemany que nos sirve para agregar una lista con datos en forma de tupla, de ahi el many que es agregar o executar 'muchos' y en el valor tenemos que poner entre parentesis un signo de ? por cada dato que contenga cada tupla, en este caso son 3 que corresponden a nombre, precio y categoria, seguido del nombre de la lista que queremos agregar

puntero.execute('select * from productos') # De esta manera leemos informacion de la base de datos. Con esto leemos la informacion pero no la vemos, para ver la informacion tenemos que hacer lo siguiente

# Ahora para ver la informacion que estamos leyendo de la base de datos tenemos que crear una variable la cual almacenara una lista la cual va a contener los registros leidos de la base de datos y esta a su vez como lo mencionamos anteriormente se tiene que almacenar en algun sitio y este sitio es una variable

listaProductos = puntero.fetchall() # Recuperamos la informacion que se encuentra en la base de datos

for p in listaProductos:
    print(p)
    
print('--- Nombre Productos ---')

for p in listaProductos:
    print(p[0])
    
print('--- Nombre y categorias Productos ---')

for p in listaProductos:
    print(f'Nombre: {p[0]} - Categoria: {p[2]}')

# print(listaProductos) # imprimimos para poder ver la informacion recuperada de la base de datos

conexion.commit() # Aceptamos los cambios o modificaciones que estamos haciendo

puntero.close() # Creo de esta manera cerramos el puntero o cursor y digo creo porque fue algo le falto enseñar al profe en el curso o al menos en los dos videos referentes a este archivo, posiblemente lo veamos o lo enseñe mas adelante, de ser asi procurare cambiar la info de este archivo si es que no se me olvida, si se me olvida, seguramente tendre un comentario de como cerrar el puntero o cursor en el momento en que lo enseñe

conexion.close() # Cerramos la conexion