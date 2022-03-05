# Serialización de colecciones, objetos

# Serializacion --> Consiste en un guardar un fiche externo una coleccion, un diccionario e incluso un objeto. Pero la particularidad de la serializacion es que vamos a guardarlo en un fichero externo codificado en codigo binario

# El objetivo de guardar un fichero en este formato puede ser diversa. Por ej si queremos distribuir un objeto que hemos construido en python por internet, viene muy bien que este objeto este codificado en codigo binario ya que la distribucion se hace mas facil, asi como cuando queremos guardarlo en un dispositivo de almacenamiento externo o bien cuando queremos guardar un objeto, coleccion o diccionario en una base de datos

""" Para llevar a cabo este proceso de serializacion es necesario hacer uso de una biblioteca de Python, la cual es la biblioteca Pickle. Esta biblioteca tiene toda una coleccion de metodos, de los cuales destacan 2 que son los que vamos a ocupar en este tema 

    Estos 2 metodos son los siguientes: 
    
        - dump(): Nos permite hacer un volcado de datos al fichero binario externo 
        
        - load(): Nos permite cargar los datos del fichero binario externo """
        
# Serializacion de colecciones

import pickle

lista_nombres = ['Pedro', 'Ana', 'Maria', 'Isabel']

fichero_listaBinaria = open('lista_nombres', 'wb') # Creando el fichero binario

pickle.dump(lista_nombres, fichero_listaBinaria) # Volcando el fichero binario

fichero_listaBinaria.close()

del(fichero_listaBinaria) # Aqui lo que estamos haciendo es borrarlo de la memoria virtual pero no estamos borrando el archivo fisico que se creo

ficheroBinario = open('lista_nombres', 'rb') # Abriendo el fichero binario en modo lectura

lista_1 = pickle.load(ficheroBinario) # Cargando y guardando el fichero binario en una variable mediante el metodo load() de la biblioteca pickle

print(lista_1)

# Serializacion de objetos

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
        
coche1 = Vehiculos('Chrysler', 'Stratus RT')
coche2 = Vehiculos('Chevrolet', 'Cavalier')
coche3 = Vehiculos('Chevrolet', 'Chevy Nova')

coches = [coche1, coche2, coche3]

fichero_Coches = open('Mis_Coches', 'wb')

pickle.dump(coches, fichero_Coches)

fichero_Coches.close()

del(fichero_Coches)

# Recuperacion de archivo binario Mis_Coches

ficheroCoches = open('Mis_Coches', 'rb')

misCoches = pickle.load(ficheroCoches)

ficheroCoches.close()

for c in misCoches:
    c.propiedadesEstado()
    print('')
    
""" En este archivo estamos generando tanto la creación como la apertura del archivo y es por eso mismo que no tenemos ningun error al momento de ejecutar el programa. Pero que pasa si queremos abrir el fichero binario desde otro archivo? Bueno lo logico dicta que en el nuevo archivo pongamos los siguiente:

    import pickle
    
    ficheroCoches = open('Mis_Coches', 'rb')

    misCoches = pickle.load(ficheroCoches)

    ficheroCoches.close()

    for c in misCoches:
        c.propiedadesEstado()
        print('') 
        
Pero esto nos daria un error, el cual seria que no encuentra Vehiculos() y esto se debe a que al momento de generar la apertura del archivo, los objetos son de tipo Vehiculo, pero tanto la clase Vehiculo como el metodo propiedadesEstado no estan definidos en el nuevo archivo, y como el nuevo archivo no tiene relacion ninguna con el archivo donde se creo el fichero binario no tiene ni idea de que es Vehiculos(), ni tampoco lo que es propiedadesEstado(), asi que nos estaria arrojando un error. Esto se soluciona de una forma rapida y practica y es poner el codigo de la clase Vehiculos en el nuevo archivo, asi cuando se haga la apertura este archivo va a tener Vehiculos() y propiedadesEstado() por lo que el archivo ahora si sabra que son esos dos a los que hacen referencias los objetos del fichero binario y podra ejecutarse el programa sin problema o error alguno """