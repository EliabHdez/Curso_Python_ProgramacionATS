# POO - Programacion Orientada a Objetos 2da Parte - Pildoras Informaticas / Video 27 del Curso

# En esta segunda parte veremos la encapsulación y el constructor

class Coche():
    largoChasis = 250
    anchoChasis = 120
    numRuedas = 4
    encendido = False
    
    def arrancar(self):
        self.encendido = True
        
    def estado(self):
        # Podemos omitir el True y solo poner if(self.encendido:). Al momento de omitir el True Python interpetra que es True, si fuera False si lo tendriamos que poner, sin embargo y aunque puedo omitirlo, lo escribo para evitar confusiones
        if(self.encendido):
            return 'El coche esta encendido'
        else:
            return 'El coche esta apagado'
        
    def arrancarEnMarcha(self, arrancamos): # El parametro adicional que le estamos pasando al metodo lo declaramos al momento de llamar al metodo, estamos obligados a pasarle un valor al parametro, si no lo hacemos el programa dara error
        self.arrancarEnMarcha = arrancamos
        
        if(self.arrancarEnMarcha) == True:
            return 'El carro esta prendido y en marcha'
        
        else:
            return 'El coche esta apagado y parado'
        
    def propiedades(self):
        print(f"""El carro tiene las siguientes propiedades 
              Largo: {self.largoChasis} cms
              Ancho: {self.anchoChasis} cms
              Ruedas: {self.numRuedas}""")

print('-------Coche 1------')

coche1 = Coche()

print(f'El largo del coche es {coche1.largoChasis} cms')
print(f'El ancho del coche es {coche1.anchoChasis} cms')
print(f'El coche tiene {coche1.numRuedas} ruedas')
coche1.arrancar()
print(coche1.estado())

print('-------Coche 2------')

coche2 = Coche()

print(f'El largo del coche es {coche2.largoChasis} cms')
print(f'El ancho del coche es {coche2.anchoChasis} cms')
print(f'El coche tiene {coche2.numRuedas} ruedas')
coche2.estado()
print(coche2.estado())

print('-------Coche 3------')

coche3 = Coche()

# print(f'El largo del coche es {coche3.largoChasis} cms')
# print(f'El ancho del coche es {coche3.anchoChasis} cms')
# print(f'El coche tiene {coche3.numRuedas} ruedas')
print(coche3.arrancarEnMarcha(True)) # El print en consola dependera si el metodo ya tiene un print declarado dentro de el o no, si no lo tiene hay que hacer uso del print al momento de llamar al metodo para que imprima el resultado de la llamada
coche3.propiedades() # Si el metodo ya tiene un print dentro de el, solo sera necesario llamar al metodo ya que imprimira lo que tiene almacenado dicho metodo

print('-------Coche 4------')

coche4 = Coche()

# print(f'El largo del coche es {coche4.largoChasis} cms')
# print(f'El ancho del coche es {coche4.anchoChasis} cms')
# print(f'El coche tiene {coche4.numRuedas} ruedas')
print(coche4.arrancarEnMarcha(False)) # Aqui estamos pasando el valor al parametro adicional correspondiente al asignado al metodo. Este es un parametro adicional al que recibe por defecto, el que ya viene implicito que es self
coche4.propiedades()

# Comente los print que nos dan la informacion acerca de las propiedades del coche por separado debido a que ya estan de mas, ya que el metodo propiedades nos esta dando como resultado todas las caracteristicas del carro

# Estado inicial --> Normalmente se acostumbra que al crear una instancia de clase el objeto creado tenga las caracteristicas de la clase de forma predeterminada, como de fabrica, es decir que al momento de crear un objeto o una instancia, por el hecho de haberlo creado ya tenga de forma automatica las caracteristicas comunes de la clase, para esto se usa el 'estado inicial'

# Constructor --> Es un metodo especial con el cual se les da un 'estado inicial' a los objetos. Es por medio del cual especificamos cual va a ser el estado inicial de los objetos que se creen, es decir cuales seran las caracteristicas de la clase que tendran los objetos o instancias de forma predeterminada al momento de crearlos.

""" Para utilizar un constructor es necesario crearlo y dentro de este poner las caracteristicas que llevaran los objetos de forma predeterminada

    Para crear un constructor lo hacemos de la siguiente manera
    - Palabra reservada def, seguida de dos guiones bajos, seguida de la palabra init y por ultimo otros dos guiones bajos, con sus respectivos parentesis como cualquier metodo y dentro de estos la palabra reservada self
    
        def __init__(self)
        
    Las caracteristicas dentro del constructor tienen que estar precedidas por self."""
    
print('---------Estado Inicial y Constructor--------')
        
class Coche2():
    def __init__(self):
        self.largoChasis = 250
        self.anchoChasis = 120
        self.numRuedas = 4
        self.__numRuedas1 = 4 # De esta manera con los dos guiones bajos precediendo el nombre de la caracterista la encapsulamos y protegemos de que sea accesible a modificaciones o alteraciones desde fuera de la clase. Sin embargo si sera accesible a modificaciones desde dentro de la clase. Esto provoca que donde se escriba esta caracteristica se tiene que poner con el mismo nombre, es decir con los dos guiones bajos precediendo el nombre
        self.encendido = False
        
    def arrancar(self):
        self.encendido = True
        
    def estado(self):
        # Podemos omitir el True y solo poner if(self.encendido:). Al momento de omitir el True Python interpetra que es True, si fuera False si lo tendriamos que poner, sin embargo y aunque puedo omitirlo, lo escribo para evitar confusiones
        if(self.encendido):
            return 'El coche esta encendido'
        else:
            return 'El coche esta apagado'
        
    def arrancarEnMarcha(self, arrancamos): # El parametro adicional que le estamos pasando al metodo lo declaramos al momento de llamar al metodo, estamos obligados a pasarle un valor al parametro, si no lo hacemos el programa dara error
        self.arrancarEnMarcha = arrancamos
        
        if(self.arrancarEnMarcha) == True:
            return 'El carro esta prendido y en marcha'
        
        else:
            return 'El coche esta apagado y parado'
        
    def propiedades(self):
        print(f'El carro tiene {self.numRuedas} ruedas. Un largo de {self.largoChasis} cms. Y un ancho de {self.anchoChasis} cms')
        
    def propiedades2(self):
        print(f'El carro tiene {self.__numRuedas1} ruedas, un largo de {self.largoChasis} cms y un ancho de {self.anchoChasis} cms')
        
print('--------Coche Uno-------')

cocheUno = Coche2()

cocheUno.arrancar()
print(cocheUno.estado())
print(cocheUno.arrancarEnMarcha(True))
cocheUno.propiedades()

print('--------Coche Dos-------')

cocheDos = Coche2()

cocheDos.arrancar()
print(cocheDos.estado())
print(cocheDos.arrancarEnMarcha(False))
cocheDos.numRuedas = 2 # Como podemos observar aqui estamos modificando el numero de ruedas mediante el objeto, la conotacion del punto y entrando a una de las caracteristicas de la clase, sin embargo aunque esto es posible y en algun momento nos valdra para algo y nos servira, en este caso en particular no es asi, ya que no tienes sentido debido a que ningun coche tiene 2 ruedas. Para evitar esto y que ciertas caracteristicas no puedan ser modificadas utilizamos la encapsulacion
cocheDos.propiedades()

# Encapsulación --> La encapsulacion nos sirve para que como su nombre lo indica encapsulemos caracteristicas de las clases y asi protegerlas y no poderlas modificar desde fuera de la clase y asi evitar en este caso un coche de 2 ruedas

# Para encapsular una variable o caractristica de una clase en Python, tenemos que preceder el nombre de esta con dos guiones bajos (__), con esto le estamos diciendo a python que encapsule esta caracterista y por lo tanto esta no sera accesible desde fuera de la clase. Ej __numRuedas1

print('--------Coche Tres-------')

cocheTres = Coche2()

cocheTres.__numRuedas1 = 2
cocheTres.propiedades2() # Aqui como podemos observar la caracteristica numRuedas1 no cambio su valor, aunque en la linea de codigo anterior tecnicamente lo hicimos, este cambio no surtio efecto ya que esta caracteristica esta encapsulada y protegida para que no pueda ser modificable desde fuera de la clase

# Si al hacer uso de una caracteristica o variable que esta encapsulada no ponemos los dos guiones bajos (__) el programa no fallara ni dara error por que no lo hay, porque lo que esta pasando en realidad es que se estaria hablando de dos variables diferentes, que no tienen nada que ver. Ej No es lo mismo numRuedas a __NumRuedas, esto para Python son dos variables completamente diferentes