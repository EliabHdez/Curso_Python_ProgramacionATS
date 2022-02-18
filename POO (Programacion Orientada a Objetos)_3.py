# POO - Programacion Orientada a Objetos 3ra Parte - Pildoras Informaticas / Video 28 del Curso

# En esta 3ra parte veremos la encapsulación de métodos

# Para encapsular un método lo hacemos de la misma manera que con las variables, anteponiendo al nombre del método dos guiones bajos (__)

# Para que nos sirve encapsular un método? Pues para la mismo que sirve encapsular una variable. Que no pueda ser accesible desde fuera de la clase. Y Esto para que nos sirve? Para que el programa no haga cosas que no debe o que no tiene sentido alguno. Ej: que en el programa que estamos haciendo aqui el metodo revisionInicial no se ejecute una vez que el carro ya esta encendido y vuelva a ejecutar este metodo, esto no tiene sentido ya que este chequeo se debe hacer antes de arrancar el coche, o peor aun que ejecute el metodo revisionInicial al carro que esta parado y que ni siquiera estamos intentado arrancar, este todavia tendria menos sentido que el anterior

class Coche():
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__encender = False
        self.color = 'rojo'
        
    def arrancar(self, arrancamos):
        self.__encender = arrancamos
        
        if self.__encender:
            chequeo = self.revisionInicial()
            
        if self.__encender and chequeo:
            return 'Revision inicial existosa. El vehiculo a sido arrancado'
        elif self.__encender and chequeo == False:
            return 'Revision inicial fallida. Revise el estado del vehiculo'
        else:
            return 'El vehiculo esta parado y parqueado'
        
    def propiedades(self):
        print(f'El vehiculo es de color {self.color}, tiene un largo de {self.__largoChasis} cms, un ancho de {self.__anchoChasis} cms y un total de {self.__ruedas} ruedas.')
        
    def revisionInicial(self):
        print('***Realizando revision inicial***')
        
        self.gasolina = 'ok'
        self.aceite = 'ok'
        self.puertas = 'close'
        
        if self.gasolina == 'ok' and self.aceite == 'ok' and self.puertas == 'close':
            return True
        
        else:
            return False
        
print('------Carro 1------')
        
carro1 = Coche()
print(carro1.arrancar(True))
carro1.propiedades()
print(carro1.revisionInicial()) # Aqui estamos llamando al metodo revisionInicial y esta haciendo este chequeo una vez que el carro esta encendido y esto eventualmente no deberia pasar ya que esta revision la debe hacer unica y exclusivamente antes de encender el carro

print('------Carro 2------')

carro2 = Coche()
print(carro2.arrancar(False))
carro2.color = 'negro'
carro2.propiedades()
print(carro2.revisionInicial()) # De igual manera aqui estamos ejecutando el metodo revisionInicial y este todavia tiene menos sentido que el anterior ya que aqui el carro esta parado y ni siquiera estamos haciendo el intento de encenderlo y aun asi esta haciendo la revision que se supone debe hacer solamente antes de querer encender en carro

# Para eso sirve la encapsulacion de metodos, para evitar cosas como las anteriores donde el programa hace cosas que no debe hacer, que no tienen sentido etc

# A diferencia de las variables donde podemos intentar modificarlas y estar el codigo escrito con la modificacion aunque esta no surta efecto, en los metodos no es asi. Los metodos con el simple hecho de llamarlos si estan encapsulados el programa nos dara error, por lo tanto estos si a estos los estamos llamando y estan encapsulados hay que comentarlos o mejor aun eliminarlos.

class Coche2():
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__encender = False
        self.color = 'rojo'
        self.presionNeumaticos = 'ok'
        
    def arrancar(self, arrancamos):
        self.__encender = arrancamos
        
        if self.__encender:
            chequeo = self.__revisionInicial() # Al igual que las variables encapsuladas los metodos encapsulados al momento de llamarlos o utilizarlos en otra parte de nuestro codigo los tenemos que poner tal cual como esta, con los dos guiones bajos (__)
            
        if self.__encender and chequeo and self.presionNeumaticos == 'ok':
            return 'Revision inicial existosa. El vehiculo a sido arrancado'
        elif self.__encender == True and chequeo == False or self.presionNeumaticos != 'ok':
            return 'Revision inicial fallida. Revise el estado del vehiculo'
        else:
            return 'El vehiculo esta parado y parqueado'
        
    def propiedades(self):
        print(f'El vehiculo es de color {self.color}, tiene un largo de {self.__largoChasis} cms, un ancho de {self.__anchoChasis} cms y un total de {self.__ruedas} ruedas.')
        
    def __revisionInicial(self):
        print('***Realizando revision inicial***')
        
        self.gasolina = 'ok'
        self.aceite = 'ok'
        self.puertas = 'close'
        
        if self.gasolina == 'ok' and self.aceite == 'ok' and self.puertas == 'close':
            return True
        
        else:
            return False
        
print('------Carro 3------')
        
carro3 = Coche2()
print(carro3.arrancar(True))
carro3.propiedades()
# print(carro3.revisionInicial()) # Si dejamos estas linea de codigo establecida el programa dara un error, ya que el metodo revisionInicial esta encapsulado, por lo tanto no es posible acceder a el desde afuera de la clase y con acceder a el me refiero a llamarlo para quererlo ejecutar

print('------Carro 4------')

carro4 = Coche2()
print(carro4.arrancar(False))
carro4.color = 'verde'
carro4.propiedades()
# print(carro4.revisionInicial()) # Si dejamos estas linea de codigo establecida el programa dara un error, ya que el metodo revisionInicial esta encapsulado, por lo tanto no es posible acceder a el desde afuera de la clase y con acceder a el me refiero a llamarlo para quererlo ejecutar

print('------Carro 5------')

carro5 = Coche2()
carro5.presionNeumaticos = 'low'
print(carro5.arrancar(True))
carro5.color = 'blanco'
carro5.propiedades()