# BBDD I / Bases de Datos - Pildoras Informaticas / Video 57

# Campos Clave

# Los campos clave es un codigo de identificacion el cual puede estar confomado por letras, numeros o ambos que perteneces a los registros de las bases de datos para su identificacion y estos codigos o claves son unicos para cada elemento o registro

# Podemos automatizar el campo clave para que python y el gestor de base de datos asignen este codigo o clave de forma automatica y que ese vaya incrementando automaticamente con cada entrada de registros. De esta manera si se le asigna un numero, pero tenemos la ventaja de que no necesitamos estarnos acordando de los codigo o claves que ya hayamos utilizado para no cometer el error de duplicarlos

import sqlite3

# conexion = sqlite3.connect('Gestion de Productos')

conexion = sqlite3.connect('Gestion de Productos 2 - Camplo Clave Automatico')

puntero = conexion.cursor()

# Para poder definir el campo clave ocupamos la instruccion PRIMARY KEY y esta debe de ir en el campo que queremos que sea clave, en este caso en particular el codigo del articulo

# Para automatizar el campo clave podriamos dejar el nombre de Codigo_Articulo, pero normalmente por convencion a este campo se le suele denominar ID y el tipo de valor que va a recibir se le cambia a valor de tipo numerico, es decir INTEGER y ademas despues de la instruccion Primary Key agregamos la instruccion AUTOINCREMENT, la cual como su nombre lo indica es que sera de incremento automatico. Tambien a la hora de insertar registros en la base de datos ya no es necesario que nuestros registros en sus datos lleven el campo que corresponderian al campo clave. Y en el metodo clave, hay que modificar el valor de los values, en donde ira el campo clave le quitamos el signo ? y lo sustituimos por NULL

# puntero.execute("""
#                 CREATE TABLE CATALOGO (
#                     Codigo_Articulo VARCHAR(4) PRIMARY KEY,
#                     Nombre_Articulo VARCHAR(50),
#                     Precio INTEGER,
#                     Categoria VARCHAR(20))
#                 """)

# puntero.execute("""
#                 CREATE TABLE CATALOGO (
#                     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                     Nombre_Articulo VARCHAR(50),
#                     Precio INTEGER,
#                     Categoria VARCHAR(20))
#                 """)

# El campo clave que asignemos (codigo articulo para este caso debe ser unico, no se debe repetir)

# productos = [
#     ('PB01', 'CAJA PAPEL BOND T/C MARCA SCRIBE', 980, 'PAPEL BOND'),
#     ('PB02', 'CAJA PAPEL BOND T/C MARCA SCOOL', 1050, 'PAPEL BOND'),
#     ('CE01', 'CINTA DE EMPAQUE TRANSPARENTE MARCA TUK', 55, 'CINTAS DE EMPAQUE'),
#     ('CE02', 'CAJA CINTA DE EMPAQUE TRANSPARENTE MARCA TUK 36PZAS', 1900, 'CINTAS DE EMPAQUE'),
#     ('PS01', 'PLAYO TRANSPARENTE CALIBRE 60', 180, 'PLAYO'),
#     ('PS02', 'PLAYO TRANSPARENTE CALIBRE 80', 165, 'PLAYO'),
#     ('HU01', 'HIELERA UNICEL #1', 30, 'UNICEL'),
#     ('HU02', 'HIELERA UNICEL #2', 50, 'UNICEL')
# ]

# Aqui ya no es necesario indicar o agregar la informacion que iria en el campo clave como en el caso que se ve arriba de este comentario

# productos = [
#     ('CAJA PAPEL BOND T/C MARCA SCRIBE', 980, 'PAPEL BOND'),
#     ('CAJA PAPEL BOND T/C MARCA SCOOL', 1050, 'PAPEL BOND'),
#     ('CINTA DE EMPAQUE TRANSPARENTE MARCA TUK', 55, 'CINTAS DE EMPAQUE'),
#     ('CAJA CINTA DE EMPAQUE TRANSPARENTE MARCA TUK 36PZAS', 1900, 'CINTAS DE EMPAQUE'),
#     ('PLAYO TRANSPARENTE CALIBRE 60', 180, 'PLAYO'),
#     ('PLAYO TRANSPARENTE CALIBRE 80', 165, 'PLAYO'),
#     ('HIELERA UNICEL #1', 30, 'UNICEL'),
#     ('HIELERA UNICEL #2', 50, 'UNICEL')
# ]

# puntero.executemany('INSERT INTO CATALOGO VALUES (?,?,?,?)', productos)

# Aqui sustituimos el valor o signo ? por NULL. Si el campo clave sera automatico no debe llevar el simbolo el ?. Si se sigue respetando su espacio y lo seguimos declarando pero con la instruccion NULL

# puntero.executemany('INSERT INTO CATALOGO VALUES (NULL,?,?,?)', productos)

puntero.execute('INSERT INTO CATALOGO VALUES (NULL, "LIGAS DE HULE NATURAL #18", 25, "LIGAS")')

# puntero.execute('INSERT INTO CATALOGO VALUES ("LH01", "LIGAS DE HULE NATURAL #18", 25, "LIGAS DE HULE")',)

#puntero.execute('INSERT INTO CATALOGO VALUES ("HU02", "LIGAS DE HULE NATURAL #18", 25, "LIGAS DE HULE")',) # Como podemos ver con esta linea de codigo al momento de ejecutar el programa nos arroja un error, debido a que se esta utilizando un campo clave que ya existe y esto no puede ser asi, estos deben de ser unicos, no se pueden duplicar, de hecho el error es de tipo UNIQUE, que hace referencia a unico.

conexion.commit()

conexion.close()