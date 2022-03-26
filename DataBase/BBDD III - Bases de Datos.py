# BBDD III / Bases de Datos - Pildoras Informaticas / Video 58

# Clausula / Instruccion UNIQUE

""" La instruccion o clausula UNIQUE la debemos definir en el campo que la requiera y solo afectar de forma personal a este. Esta instruccion se puede colocar en cualquier campo y se puede utilizar las veces que sea necesario, aun en el mismo archivo, la misma tabla etc. Este no es clave o codigo principal como el que se genera con la instruccion PRIMARY KEY, pero si tiene en comun con este ultimo que no se pueda repetir y que su valor tiene que ser unico para cada registro """

# Operaciones CRUD

""" CRUD = Create, Read, Update, Delete
        - Asi se define o conoce a estos cuatro procesos que podemos hacer a la tabla de una base de datos. Estos como ya hemos visto con los dos primeros (Create y Read), se realizan mediante instrucciones del lenguajes SQL, y los dos ultimo no son la excepcion 
        
        - Create es para crear. Nos sirve tanto para crear la tabla misma como registros que seran añadidos a las tablas
        
        - Read nos sirve para leer la informacion de la tabla, sin embargo esta palabra de READ no se emplea como tal o al menos no se a empleado hasta ahora, para leer lo tenemos que hacer mediante la instruccion 'SELECT * FROM' si no mal recuerdo, si no es asi, o hay algun cambio o añadido respecto a esto, cambiare esta informacion """

import sqlite3

conexion = sqlite3.connect('Catalogo Productos')

puntero = conexion.cursor()

# El unique en el campo articulo nos va a servir para que dos articulos no puedan tener el mismo nombre o valor

# puntero.execute(""" 
#                 CREATE TABLE CATALOGO (
#                     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                     ARTICULO VARCHAR(50) UNIQUE,
#                     PRECIO INTEGER,
#                     CATEGORIA VARCHAR(20)) """)

# productos = [
#     ('CJ PAPEL BOND T/C', 980, 'PAPEL'),
#     ('CJ PAPEL BOND T/O', 1350, 'PAPEL'),
#     ('CINTA TRANSPARENTE', 55, 'CINTA EMPAQUE'),
#     ('PLAYO 18" CAL 60', 180, 'PLAYO')
# ]

# puntero.executemany('INSERT INTO CATALOGO VALUES (NULL,?,?,?)', productos)

#puntero.execute('INSERT INTO CATALOGO VALUES (NULL,"CINTA TRANSPARENTE", 54, "CINTA EMPAQUE")') # Con esta linea obtenemos un error ya que le hemos definido al campo ARTICULO de la tabla que sea de tipo unique, esto quiere decir que el valor dado a los registros en este campo no pueden repetirse, ser el mismo,de ahi el termino unique, tienen que ser valores unicos. Por lo tanto lo tendre que comentar

# Aqui vamos a probar haciendo una nueva insercion en la tabla de la base de datos pero esta vez cambiando un poco el nombre del articulo para que corroboremos que al momento de asignarle un nombre diferente este registro se agrega sin ningun problema

# puntero.execute('INSERT INTO CATALOGO VALUES (NULL,"CINTA TRANSPARENTE JANEL", 55, "CINTA EMPAQUE")')

# Porque no dio error con los otros campos aun siendo iguales? Porque el valor unique solo afecta en donde se ponga, en este caso como tenemos el unique solo en el campo de ARTICULO, este no afecta a los campos de precio y categoria, es por eso que aunque en estos campos no cambia la informacion, podemos hacer la incersion del registro sin problema alguno. Podemos poner la instruccion unique donde queramos, cuantas veces queramos o necesitemos

# --------------- Read -------------------

""" 
        -SELECT * FROM significa "selecciona de donde" seguido del nombre de la tabla. Esta instruccion se ocupa en el execute()
        
        - WHERE tambien significa "donde" pero este va enfocado y apuntando a los valores de la tabla, se pone where seguida del nombre del valor igualando este valor al valor que hay dentro, es decir en este caso un valor de la tabla como podria ser id, articulo etc igualando este a un valor dentro de este que puede ser el id de un articulo, el nombre de un articulo, su categoria etc. Esta instruccion tiene que ir definida en el execute()
        
        EL WHERE ES IMPORTANTE UTILIZARLO Y SABER DONDE, YA QUE ESTE APUNTA DE FORMA DIRECTA A LOS REGISTROS. SI ESTE NO SE OCUPA COMO SE DEBE O EN EL MOMENTO QUE SE DEBE PODRIA SER PERJUDICIAL, YA QUE SI NO LO LLEGAMOS A OCUPAR AL MOMENTO DE QUERER ELIMINAR O ACTUALIZAR UN REGISTRO, ESTARIAMOS ELIMINANDO O ACTUALIZANDO TODOS LOS REGISTROS DE LA TABLA, ASI QUE ES IMPORTANTE PRESTAR ATENCION AL MOMENTO DE HACER ALGO Y SABER SI LO TENEMOS QUE OCUPAR O NO
        
        fetchall() --> Con esta instruccion generamos la lectura y esta va definida y de la mano del puntero o curso, es por esto que se ocupa con este """

print('-------- Instruccion READ ---------')

puntero.execute('SELECT * FROM CATALOGO') # Con esta instruccion le estamos diciendo que queremos leer

catalogo = puntero.fetchall() # Y esta instruccion es la que se encarga de hacer la lectura, en este caso la estamos almacenando en una variable para despues imprimirla en consola

for c in catalogo:
        print(c)
        
print('-------- Catalogo por Seccion ---------')
        
puntero.execute('SELECT * FROM CATALOGO WHERE CATEGORIA = "PAPEL"') # Con esta instruccion tambien le decimos que queremos leer pero agregamos parametros adicionales para hacer una lectura especifica, diciendo en concreto que queremos leer, en este caso los productos de la categoria papel de la base de datos catalogo
        
catalogo = puntero.fetchall()

print(catalogo)

for c in catalogo:
        print(c)
        
# --------------- Update -------------------

# Vamos a actualizar el precio de la cinta de empaque janel. Actualmente el precio de esta cinta es de 55

print('-------- Instruccion UPDATE ---------')

puntero.execute('UPDATE CATALOGO SET PRECIO = 47 WHERE ARTICULO = "CINTA TRANSPARENTE JANEL"')

# --------------- Delete -------------------

# Vamos a eliminar un articulo de la tabla perteneciente a la base de datos

# De entrada debemos definir el criterio que utilizaremos para hacer la eliminacion, con esto me refiero a que valor de la tabla vamos a ocupar para hacer, es decir por medio del articulo, el id, la categoria y el precio. Hay que tener en cuenta que si utilizamos algun valor que no este definido como clave o codigo y como unique al momento de hacer el delete se borrarian todos los registros que tengan el mismo valor o parametro, es decir, si elegimos borrar por precio o categoria y este precio lo tienen varios articulos, se estaria borrando todos los registros que tengan el mismo precio, al igual que la categoria, si nos definidos por esta al hacer un delete, todos los registros que esten dentro de la categoria definida se estarian eliminando, con articulo esto no pasaria al menos en este archivo ya que esta definido como unique, pero de no estarlo podria pasar lo mismo si uno o varios prodcutos tienen el mismo nombre o valor en este campo de articulo. Esto tampoco pasaria con el id ya que esta definido como primary key

# Para este ejemplo haremos uso del ID

puntero.execute('DELETE FROM CATALOGO WHERE ID = 4')

conexion.commit()

conexion.close()