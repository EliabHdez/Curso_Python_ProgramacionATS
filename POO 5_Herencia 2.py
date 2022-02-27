# POO - Programacion Orientada a Objetos 3ra Parte - Pildoras Informaticas / Video 31 del Curso

# Terminos super(), isinstance() y concepto de princpio de sustitucion

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
    motoCaballo = 'Caballando'
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

# En los siguientes ejemplos podemos ver la prioridad que tiene la herencia conforme a las clases cuando se ocupa herencia multiple. Esta preferencia implica que cuando hay clases con el mismo nombre en los metodos, tome el metodo que corresponde a la clase a la que se le esta dando prioridad. Esto conlleva a que si necesitamos ocupar el metodo de la otra clase pero tiene el mismo nombre no lo vamos a poder hacer, es cierto que podemos encontrar la manera de resolverlo, pero no seria la mejor forma o la mas adecuada

# En estos ejemplos tenemos herencia multiple y ambas clases que se ocupan para la herencia tienen un metodo con el mismo nombre... __init__ y aunque este es un constructor no deja de ser un metodo, por lo tanto cuando queremos ocupar el metodo o constructor de la clase que no tiene la preferencia nos arroja un error. Como dijimos anteriormente podemos solucionar esto de alguna manera, ya sea declarando otro metodo, cambiando el nombre etc, pero no siempre sera la mejor solucion o la que necesitemos. Por ej en el caso de Bike 1, a la clase ElectricsCars que es la que tiene la prioridad podemos agregarle al constructor los parametros necesarios para definir marca y modelo como en la clase Vehiculos, pero no seria la mejor solucion ni la mas elegante. Para solucionar esto tenemos el la funcion super()

print('-----Electrics Bikes-----')

class ElectricBike(ElectricCars, Vehiculos):
    pass

print('-----Bike 1-----')

myBike1 = ElectricBike()
print(myBike1.autonomia)

class ElectricBike2(Vehiculos, ElectricCars):
    pass

print('-----Bike 2-----')

myBike2 = ElectricBike2('GT', 'X500')
# print(myBike2.autonomia)
myBike2.propiedadesEstado()
print(myBike2.chargeBattery(False))

# Super() --> Esta funcion sirve para que haya donde la definidas en tu codigo va a llamar al metodo de la clase padre

class Persona():
    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugarResidencia = residencia
        
    def datosPersona(self):
        print(f'Nombre: {self.nombre}, Edad: {self.edad}, Pais de Residencia: {self.lugarResidencia}')

class Empleado(Persona):
    def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado):
        # super().__init__('Eliab', 31, 'México')
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antigüedad = antigüedad
        
    def datosPersona(self):
        super().datosPersona()
        print(f' Salario: {self.salario}, Antigüedad: {self.antigüedad}')
        
print('-----Persona-----')
        
Moises = Persona('Moises', 31, 'México')
Moises.datosPersona()

# Si el siguiente codigo lo dejamos asi como esta sin utilizar la funcion super veremos que nos da error, debido a que el metodo Empleado no nos pide 3 valores que son nombre, edad ni lugar de residencia, aunque llegasemos a cambiar estos valores por el salario y la antigüedad de igual forma nos daria error debido a que estamos llamando al metodo datosPersona y aunque este esta heredado de la clase Persona en la clase Empleado no va a reconocer las variables en su interior como nombre, edad y lugarResidencia. Para solucionar esto hacemos uso de la funcion super(), en este caso la debemos declarar en la clase empleado dentro del constructor para que jale el metodo de la clase padre que vendria siendo la clase Persona. Debemos definir en la funcion super el nombre del metodo que queremos jalar, en este caso __init__. Aunque aqui nos encontramos con un problema, el cual es que como le estamos pasando datos especificos, un nombre, una edad y una residencia, todos las instancias u objetos que creemos traeran estos datos, que no siempre sera lo que vayamos a querer. Adicional a esto en la descripcion solo nos esta arrojando los datos de la persona, pero no nos esta arrojando los datos como empleado que son el salario y la antigüedad. Este codigo hay que depurarlo y mejorar para solucionar estos detalles, lo cual haremos a continuacion

# Para solucionar el problema de los datos especificos lo que tenemos que hacer es añadir parametros dentro del constructor de la clase empleado. Los datos especificos definidos en la funcion super los vamos a sustituir por los argumentos definidos en el constructor de la clase Empleado. Esto conlleva a que al crear un objeto de la clase empleado le pasemos los parametros especificados en su constructor, los cuales en este caso en especifico son 5 y 3 de esos 5 seran utilizados para llamar al constructor de la clase padre

# Para solucionar el problema de la descripcion donde no nos dice nada del salario y de la antigüedad, lo que tenemos que hacer es crear un metodo en la clase empleado con la funcion super el cual se encargara de llamar al metodo de la clase padre Persona, para tener el metodo descripcion de la clase persona que nos da los datos de la misma y ademas agregar un print o lo que necesitemos para los datos del salario y de la antigüedad

# Eliab = Empleado('Eliab', 31, 'México')
Eliab = Empleado(8000, 5, 'Eliab', 31, 'México')
Eliab.datosPersona() # Aqui ya estamos ocupando el metodo datosPersona() de la clase Empleado y no de la clase heredada Persona()

# Que nos estamos ahorrando o en que nos esta beneficiando el uso de la funcion super??? Que en la clase Empleado tengamos que declarar todas las variables que tiene la clase Persona que son nombre, edad y residencia y en el metodo datosPersona tener que repetir toda la linea de codigo que nos da los datos de la persona que se encuentra en la clase Persona(), en este programa no pareceria ser la gran cosa, pero un programa mucho mas extenso o complejo donde hay muchas clases y estan se estan heredando entre si nos estariamos ahorrando muchas lineas de codigo y si no lineas, si repetir o escribir mucho mas codigo

# A la hora de trabajar con Herencias existe un concepto que se conoce como principio de sustitucion

# Principio de sustitucion --> Consiste en aplicar el 'es siempre un/una'. Esto quiere decir que al momento de heredar, la clase hijo que hereda a la clase padre tiene que ser algo con sentido logico de la clase padre. A que se refiere esto? A que por ejemplo en el caso de nuestras clases Persona() y Empleado(), la clase Empleado hereda de la clase Persona() y esto quiere decir que en terminos faciles de entender un empleado siempre y antes que ser empleado sera una persona, pero esto no puede ser al reves, un empleado no puede ser empleado si no es una persona, pero una persona no puede ser siempre un empleado, al igual que en ejemplos anteriores anteriores como las clases de coche(), moto() y vehiculos; una moto siempre sera un vehiculo, pero un vehiculo no siempre sera una moto, por lo tanto no tendria sentido que la clase Vehiculo herede de la clase Moto(), asi como que la clase Persona(), herede la clase Empleado(), pero si al reves. Si las clases y las herencias estan definidas con este principio quiere decir que esta bien hechas y que nuestro codigo y logica de programacion es correcto(a)

# isinstance

# La funcion isinstance() nos va a informar siempre si un objeto es instancia de una clase determinada. Esta funcion devuelve True si pertence es instancia de la clase que le pasemos o False si es lo contrario, es decir que no sea instancia de la clase.

# La funcion isinstance nos solicita dos argumentos, el primero la instancia u objeto al cual nos referimos y el segundo la clase de la que vamos a comprobar si pertenece o no

print(isinstance(Moises, Persona))
print(isinstance(Moises, Empleado))
print(isinstance(Eliab, Empleado))
print(isinstance(Eliab, Persona))

# Ahora veremos la manera de agregar marca y modelo a un vehiculo de clase electrica lo cual no nos era posible anteriormente ya que al crear un objeto perteneciente a esta clase y heredar de la clase electricCars de primera mano tomaba el metodo init de esta y no de la clase vehiculos, lo cual hacia imposible asignar una marca y modelo

# Para esto vamos a crear una clase nueva de carros electricos para ver la diferencia entre esta ultima y la anterior

print('-----Electric Car 2-----')

class ElectricCars2(Vehiculos):
    def __init__(self, marca, modelo, autonomia):
        super().__init__(marca, modelo)
        self.autonomia = autonomia
        # self.autonomia = '100 kms'
        
    def chargeBattery(self, charging):
        self.chargeBat = charging
        if self.chargeBat:
            return 'The battery is charging'
        else:
            return 'The battery is not charging'
        
    def propiedades(self):
        super().propiedadesEstado()
        print(f'Autonomia: {self.autonomia}')
        # print(f'La autonomia es de: {self.autonomia}')
        
electricCar2 = ElectricCars2('Volvo', 'C-40', '100 kms')
electricCar2.arrancar()
electricCar2.propiedades()

print('-----Electric Bike 5-----')

class ElectricBike5(ElectricCars2, Vehiculos):
            
    def cargaManual(self, cargando, porcentaje):
        self.pedalear = cargando
        self.porcentaje_carga = porcentaje
        if self.pedalear == True and self.porcentaje_carga >= 0 and self.porcentaje_carga < 100:
            return f'Bateria al {self.porcentaje_carga}% y cargando'
        elif self.pedalear == True and self.porcentaje_carga == 100:
            return f'Bateria al {self.porcentaje_carga}%. Carga completa'
        elif self.pedalear == True and self.porcentaje_carga < 0 or self.porcentaje_carga > 100:
            return f'Error de carga. Favor de llevar su bicicleta a su agencia'
        elif self.pedalear == False and self.porcentaje_carga < 0 or self.porcentaje_carga > 100:
            return f'Error de carga. Favor de llevar su bicicleta a su agencia'
        else:
            return f'Bateria descargandose. Resta {self.porcentaje_carga}%'
        
miBike5 = ElectricBike5('Benotto', 'BT-7274', '65 kms')
miBike5.propiedades()
print(miBike5.cargaManual(True, 0))
print(miBike5.cargaManual(True, 2))
print(miBike5.cargaManual(True, 99))
print(miBike5.cargaManual(True, 100))
print(miBike5.cargaManual(True, 134))
print(miBike5.cargaManual(False, 79))
print(miBike5.cargaManual(False, 101))
print(miBike5.cargaManual(False, -99))