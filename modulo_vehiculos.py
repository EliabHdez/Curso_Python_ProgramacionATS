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
        if self.acelerar == True:
            self.motoCaballo = 'Caballito en proceso'
        else:
            self.motoCaballo = 'Caballito en espera de ejecucion'
        
    def propiedades(self):
        super().propiedadesEstado()
        print(f'Caballo: {self.motoCaballo}')

class Camioneta(Vehiculos):
    def carga(self, cargada):
        self.cargar = cargada
        if self.cargar:
            return 'La camioneta está cargada'
        else:
            return 'La camioneta no está cargada'

class ElectricCars2(Vehiculos):
    def __init__(self, marca, modelo, autonomia):
        super().__init__(marca, modelo)
        self.autonomia = autonomia
        
    def chargeBattery(self, charging):
        self.chargeBat = charging
        if self.chargeBat:
            return 'The battery is charging'
        else:
            return 'The battery is not charging'
        
    def propiedades(self):
        super().propiedadesEstado()
        print(f'Autonomia: {self.autonomia}')

class ElectricBike(ElectricCars2, Vehiculos):
            
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