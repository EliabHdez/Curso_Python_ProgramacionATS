# Módulos --> Son archivos con extensión .py .pyc (Python compilado) o archivo escrito en C para Python, que posee su propio espacio de nombres y que puede contener variables, funciones, clases e incluso otro módulos. En otras palabras es el archivo donde escribimos el codigo de nuestro programa

# Los modulos sirven para organizar y reutilizar el codigo (modularizacion y reutilizacion)

# Reutilizacion --> En la programacion orientada a objetos siempre hay que reutilizar el codigo ya que es una de las maximas ventajas que nos ofrece. Con reutilizar no queremos decir que copiemos y peguemos codigo que hayamos hecho con anterioridad, si no que utilicemos los modulos de otros programas o aplicaciones que ya tienen cierto codigo y que nos pueden servir para el nuevo programa que estamos creando

# Modularizacion --> Como su nombre lo indica es dividir el codigo en modulos, es decir en pequeñas partes. En la creacion de una aplicacion siempre es mejor y mas facil manejar una aplicacion que esta divida en pequeñas piezas que una que esta hecha en un solo mega archivo con miles de lineas de codigo. Ya sea para implementar, corregir, añadir, quitar etc codigo en la aplicacion es mejor tenerla divida en pequeños modulos, que en un solo archivo que contenga todo el codigo el cual podria ser demasiado. La modularizacion implica que nuestros programas o aplicaciones funcionen como un tipo de puzzle donde un monton de piezas trabajan de forma conjunta para dar como resultado un todo, en este caso una aplicacion o programa en su totalidad

# Para crear un modulo es tan sencillo como crear un archivo con extension .py (o .pyc o archivo C) y guardarlo donde nos interese

# A CONTINUACION EMPEZAREMOS A HACER USO DE LOS MODULOS EXTERNOS A ESTE COMO EL MODULO DE FUNCIONES MATEMATICAS, EL MODULO DE VEHICULOS ETC

# Para utilizar un modulo en Python lo primero que hay que hacer es importarlo, para eso hacemos uso de la palabra reservada import seguido del nombre del modulo a importar

""" Cuando importamos modulos no solo basta con importarlos para poder ocuparlos, para esto ultimo tenemos que definir ciertas acciones o codigos los cuales nos permitiran utilizar los modulos importados

    Formas de utilizar los modulos importados
    
    - import - Nomenclatura del punto: Este se ocupa cuando solo se utiliza la directiva import. Al igual que en la programacion orientada a objetos es necesario hacer uso del punto para llamar a la funcion del modulo. Ej. modulo_funcionesMatematicas.sumar(). Este forma tiene un inconveniente hasta cierto aspecto y es que cada vez que quieras utilizar una funcion del modulo hay que llamar al modulo seguido de la funcion con el punto entre ambos, esto no viene bien si lo que se busca es hacer uso del modulo completo, esto viene bien si solo se va a ocupar alguna funcion o codigo en concreto, ya que consume menos recursos que llamar y tener disponible el modulo completo
    
    - from: Para evitar el tener que llamar al modulo cada vez que se ocupe una funcion de este o cualquier otro fragmento de codigo cambiamos la directiva import por from seguida del nombre del modulo añadiendo el import y la funcion o codigo a ejecutar. Este al igual que el anterior (directiva import) tiene el inconveniente que tienes que definir que funcion o codigo vas a utilizar, por lo tanto si quieres hacer uso de codigo diferente o alguna otra funcion el programa arrojara un error. Este al igual que el anterior sirve para economizar recursos y viene bastante bien cuando vas a ocupar algo en especifico y no todo lo que contiene el modulo como tal
    
    - from... import *: La directiva from con el import * nos sirve para ocupar en su totalidad y tener disponible sin restriccion alguna todo lo que tenemos en el modulo que estamos importando. Esto viene bastante bien cuando vamos a hacer uso de todo o de varias funciones o codigo que vienen en el modulo y asi evitar el inconveniente que se tiene con las 2 formas anteriores. Sin embargo esto consume mas recursos, ya que almacena un espacio considerable en memoria para tener disponible todo el contenido del modulo """
    
# IMPORTANTE: Para efectos practivos y entendibles yo estoy importando los modulos en la seccion donde estoy haciendo referencia a cada uno de estos, pero esto no debe de ser asi, los modulos se tienen que importar al inicio del archivo, por encima de todo nuestro codigo
    
print('-----Directiva From-----')

# Directiva import
import modulo_funcionesMatematicas

modulo_funcionesMatematicas.suma(7, 5)
modulo_funcionesMatematicas.resta(9, 5)

print('-----Directiva From-----')

# Directiva from
from modulo_funcionesMatematicas import suma

suma(7,5)
# resta(9,5)

print('-----Directiva From... import *-----')

# Directiva from... import *
from modulo_funcionesMatematicas import *

suma(7,5)
resta(9,5)
multiplicacion(6,3)
division(8,4)

# Esto puede que nos haga pensar que entonces cual es la diferencia de utilizar solo el import, el from o el from... import *, si poniendo este ultimo te quitas de problemas al tener todo disponible... Y esta diferencia son los recursos, es un tema de optimizacion, donde al ocupar el * para tener disponible el modulo completo se esta reservando un espacio muy grande en memoria para tener el modulo completo disponible y esto en estos programas de ejercicios y pequeños no resulte ser un problema ya que no vemos el consumo excesivo de recursos, pero si el programa es grande, el modulo sera grande y podra tener miles de lineas de codigo y es aqui donde los recursos a ocupar son muchos y el espacio en memoria para reservar este modulo seria bastante grande, mientras que cuando ocupas el import o el from solo estamos generando que se reserve un espacio de memoria pequeño para la funcion, clase o codigo que vamos a ocupar y no para todo el modulo completo

print('-----Vehiculos-----')

from modulo_vehiculos import *

print('---Coches---')

cocheUno = Vehiculos('Chevrolet', 'Camaro')
cocheUno.arrancar()
cocheUno.propiedadesEstado()

print('---Motos---')

motoUno = Moto('HONDA', 'CBR600RR')
motoUno.caballo()
motoUno.propiedades()

print('')

motoDos = Moto('KAWASAKY', 'H2R')
motoDos.arrancar()
motoDos.acelerando()
motoDos.caballo()
motoDos.propiedades()

# Cuando se importan modulos, el interprete de Python busca estos modulos en la misma ruta en la que se encuentra el modulo o script que lo esta llamando, si el modulo a importar no se encuentra en esta ruta Python procedera a buscarlo en la ruta 'syspath' que es la ruta donde se encuentra instalado Python y si el modulo no se encuentra en ninguna de estas dos rutas el programa dara error. Si que hay una forma de importar modulos se encuentren en rutas diferentes, vaya se encuentren donde se encuentren los modulos los podemos importar, pero esto lo hacemos mediante lo que se denominan 'paquetes' un tema que veremos en el siguiente capitulo...