# POO - Programacion Orientada a Objetos 3ra Parte - Pildoras Informaticas / Videos 29 y 30 del Curso

# Herencia

# Herencia --> La herencia se trata de que como su nombre lo indica heredar lo que alguien mas tiene. Como suele pasar en la vida real con los bienes de las personas. Supongamos una familia donde esta el abuelo, el padre y los hijos. Cuando el abuelo fallece, el padre 'hereda' los bienes del abuelo, cuando el padre fallece, los hijos 'heredan' los bienes del padre. Este mismo concepto lo toma la programacion en las clases, donde existe la clase 1 (abuelo), la clase 2 (padre) y las clases 3, 4, 5 etc (hijos), donde las clases inferiores van 'heredando' lo de las clases superiores

# En la programacion la clase con la jerarquia mas alta (abuelo) se le conoce como 'clase padre' o 'superclase', a la clase que le sigue (padre), se le conoce como 'subclase' o 'superclase' (subclase de la clase mas alta (abuelo) y superclase de las clases que estan por debajo (hijos))

"""           Clase 1 --> superclase o clasepadre (abuelo)
              Clase 2 --> subclase o superclase (padre)
    Clase 3   Clase 4   Clase 5 (hijos)
"""

# Para que sirve la Herencia? --> Sirve para reutilizar codigo en caso de crear objetos similares. En los archivos anteriores de la Programacion Orientada a Objetos hemos creado objetos, pero estos han sido iguales o del mismo tipo... carros, pero supongamos que ahora vamos a crear un programa mas complejo donde no solo vamos a crear objetos de tipo carro si no que tambien vamos a crear objetos de tipo moto, camiones, lanchas, autobuses etc, estos aunque no son iguales si son similares, ya que todos estos van a tener caracteristicas y comportamientos en comun como por ej: caracteristicas en comun --> Marca, Modelo, un Motor / comportamientos en comun --> Acelerar, Frenar, Arrancar

# Si no existiera la herencia, tendriamos que crear cada objeto de forma individual, uno por uno con sus correspondientes caracteristicas y metodos por separado aunque fueran comunes de todos ellos

# La herencia consiste en crear todas las caracteristicas o propiedades junto con los comportamientos en comun y englobarlos en una clase la cual va a ser o se va a denominar la clase padre o superclase

# Las particularidades especficas o individuales de cada uno de los objetos las construiremos en su propia clase

class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        self.acelerar = False
        self.frenar = False
        
    def arrancar(self):
        self.encendido = True
        
    def acelerando(self):
        self.acelerar = True
        
    def frenando(self):
        self.frenar = True
        
    def propiedadesEstado(self):
        print(f'Marca: {self.marca} \nModelo: {self.modelo} \nPrendida: {self.encendido} \nAcelerando: {self.acelerar} \nFrenando: {self.frenar}')
        
class Moto(Vehiculos):
    motoCaballo = 'Caballando' # No entiendo porque se declaro antes la variable fuera del metodo. Y con un string vacio
    def caballo(self):
        self.motoCaballo = 'Caballito en proceso'
        
    def propiedadesEstado(self):
        print(f'Marca: {self.marca} \nModelo: {self.modelo} \nPrendida: {self.encendido} \nAcelerando: {self.acelerar} \nFrenando: {self.frenar} \nCaballo: {self.motoCaballo}')
        
print('-----Motorcicle-----')

moto1 = Moto('Honda', 'CBR')
# moto1.arrancar()
moto1.caballo()
moto1.propiedadesEstado()

print('-----Van-----')

# Cuando creamos metodos, al momento de crear variables dentro de estas, quererlas modificar, darles 'x' valor, utilizarlas en un if etc etc etc hay que tener cuidados y utilizar el nombre de las variables, NO el nombre del metodo, tambien no se nos debe olvidar hacer uso del self anteponiendolo al nombre de las variables

class Camioneta(Vehiculos):
    def carga(self, cargada):
        self.cargar = cargada
        if self.cargar:
            return 'La camioneta está cargada'
        else:
            return 'La camioneta no está cargada'
        
myVan = Camioneta('Chevrolet', 'Silverado')
myVan.arrancar()
myVan.propiedadesEstado()
print(myVan.carga(True))

print('-----Electric Car-----')

class ElectricCars():
    def __init__(self):
        self.autonomia = '100 kms'
        
    def chargeBattery(self, charging):
        self.chargeBat = charging
        if self.chargeBat:
            return 'The battery is charging'
        else:
            return 'The battery is not charging'
        
myElectricCar = ElectricCars()
print(myElectricCar.chargeBattery(True))
print(myElectricCar.autonomia)

print('-----Electric Bike-----')

class ElectricBike(ElectricCars, Vehiculos): # Aqui estamos haciendo uso de la Herencia Multiple, la cual nos permite heredar de mas de una clase, para hacer esto se tienen que poner todas las clases de las cuales se va a heredar separadas por comas. En la Herencia multiple, se le da prioridad/preferencia a la clase que se defina primero dentro de los parentesis
    pass

# myBike = ElectricBike('GT', 'X500') # Si descomentamos esta línea veremos que nos arroja un error, porque? Si se le estan pasando los argumentos correspondientes a marca y modelo. Esto es debido a que como se comento anteriormente al hacer uso de la herencia multiple, esta le da prioridad a la clase que se esta definiendo primero en los parentesis, la cual en el ej anterior es la clase correspondiente a ElectricsCars, por lo tanto estamos heredando el constructor correspondiente a esta clase y este constructor no nos pida marca ni modelo y por lo tanto no tiene estos argumentos definidos. Si invertimos la posicion de las clases de las que esta heredando estariamos cambiando la proiridad de la herencia y por lo tanto ya no habria error.

class ElectricBike2(Vehiculos, ElectricCars):
    pass

miBike = ElectricBike2('GT', 'X500')
miBike.propiedadesEstado()
print(miBike.chargeBattery(False))