# Paquetes --> Son los directorios que almacenan los modulos relacionados entre si

# Los paquetes sirven para organizar y reutilizar los modulos

# Los paquetes se crean a partir de una carpeta la cual tiene que contener un archivo con el nombre __init__.py

# Con esto podemos decir que estamos reutilizando codigo, ya que en ves de crear nuevamente el codigo, estamos reutilizando un modulo que ya lo contiene

# Si vamos a hacer uso de subpaquetes lo unico que tenemos que hacer es anotar la ruta completa donde se encuentran estos subpaquetes seguido de igual manera que en los paquetes del nombre del modulo a importar

# Eso de la ruta tambien se puede simplificar, sim embargo es algo que se vera mas adelante, de momento hay que tener en cuenta que hay que anotar la ruta completa!!!

from calculos.calculos_generales import * # Paquete
from calculos.basicos.operaciones_basicas import * # Subpaquete
from calculos.potencia_porcentaje.potencia_porcentaje import * # Subpaquete

suma(5,2)
multiplicacion(9,9)

# Se pueden tener paquetes dentro de paquetes, o subpaquetes como se les podria conocer, estos de igual manera deben contener el archivo __init__.py

# Hemos agregado subpaquetes al paquetes calculos, estos subpaquetes son las carpetas que tienen dentro de estas un archivo __init__.py, las cuales son basicos y potencia_porcentaje, asi como el modulo que utilizaremos para importar y estarlo reutilizando

print('-----Paquete basicos-----')

op_resta(10,7)
op_division(50,5)

print('-----Paquete potencia_porcentaje-----')

op_potencia(5,5)
op_porcentaje(100,15)