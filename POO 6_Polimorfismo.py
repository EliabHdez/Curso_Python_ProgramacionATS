# Polimorfismo

# El polimorfismo en la programacion se da cuando un objeto cambia de forma dependiendo del contexto en el que se utilice y por lo tanto al cambiar de forma, el objeto cambia de comportamiento

# Si trasladamos este concepto del polimorfismo al ejemplo que hemos estado viendo en el tema del POO, quiere decir que los objetos vehiculos, ya sea coche, moto, camion etc pueden cambiar de forma, es decir pasar de ser un camion y ser una moto y de una moto pasar a ser un coche y por lo tanto ese objeto cambiaria su comportamiento

class Moto():
    def num_ruedas(self):
        print('Tiene 2 ruedas')
    def cambio_velocidades(self):
        print('El cambio se realiza con el pie izquierdo')
        
class Coche():
    def num_ruedas(self):
        print('Tiene 4 ruedas')
    def cambio_velocidades(self):
        print('El cambio se realiza con la mano')
        
class Camion():
    def num_ruedas(self):
        print('Tiene 8 ruedas')
    def cambio_velocidades(self):
        print('El cambio se realiza con la mano y los dedos')
        
# Para hacer uso del polimorfimso creamos una funcion o un metodo el cual recibe un parametro y este parametro es el que se va encargar de almacenar el tipo de vehiculo u objeto que se esta creando para que asi tenga la forma y el comportamiento adecuado

# OJO: No confundir las funciones o metodos generales con los metodos de las clases, los cuales son metodos pertenecientes unica y exclusivamente a estas

def ruedas_vehiculos(numRuedas): # El parametro de esta funcion es el que se encarga de hacer la funcion del polimorfismo ya que almacenara el objeto que es generico, que puede ser de cualquier tipo o clase al momento de asignarlo a la funcion cuando la llamemos, pero antes este objeto ya va a estar definido con una clase a la que pertence para asi poder llamar a los metodos correspondientes
    numRuedas.num_ruedas()
    
def cambio_velocidades(cambioVelocidades):
    cambioVelocidades.cambio_velocidades()
    
    
miVehiculo = Camion()
ruedas_vehiculos(miVehiculo) # Este parametro se almacena en el parametro de la funcion, y despues de esto evalua a donde pertence y es lo que llama o ejecuta
cambio_velocidades(miVehiculo)

miVehiculo2 = Coche()
ruedas_vehiculos(miVehiculo2)
cambio_velocidades(miVehiculo2)

miVehiculo3 = Moto()
ruedas_vehiculos(miVehiculo3)
cambio_velocidades(miVehiculo3)

# Tal vez en los 3 ej anteriores no veamos con nitidez esto del polimorfismo, ya que estamos creando 3 objetos diferentes, pero a continuacion si que podemos ver la magia del polimorfismo ya que el ultimo objeto creado que es el vehiculo 3 que es una moto lo estamos cambiando a ser un camion y gracias al polimorfismo veemos que cambia su forma y su comportamiento sin problema alguno. Y como nos damos cuenta de esto? Bueno que al momento de cambiarlo, le estamos asignado que pertenezca a una clase diferente y esto hace que cambie su forma y comportamiento y lo comprobamos imprimiento los metodos ruedas y velocidades donde podemos ver que ahora arroja los resultados correspondientes al comportamiento y las propiedades de un camion tanto en el cambio de velocidades como en el numero de ruedas que tiene y es el mismo objeto 'miVehiculo3'

miVehiculo3 = Camion()
ruedas_vehiculos(miVehiculo3)
cambio_velocidades(miVehiculo3)

# Y esto mismo lo podemos hacer con los otros dos objetos para hacer un poco mas de enfasis al tema tratado que es el polimorfismo

miVehiculo = Coche()
ruedas_vehiculos(miVehiculo)
cambio_velocidades(miVehiculo)

miVehiculo2 = Moto()
ruedas_vehiculos(miVehiculo2)
cambio_velocidades(miVehiculo2)

# Como podemos ver al principio el vehiculo 1 era un camion y despues paso a ser un coche, el vehiculo 2 era un coche y paso a ser una moto y el vehiculo 3 era una moto y paso a ser un camion. Esto es el polimorfismo, hacer que un mismo objeto cambie de forma y por ende su comportamiento