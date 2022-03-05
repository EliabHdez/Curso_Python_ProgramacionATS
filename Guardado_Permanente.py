# Guardado permanente --> Guardar datos de forma permanente en ficheros externos

# Vamos a utilizar un fichero para ir guardando paulatinamente informacion dentro de el desde diferentes programas para tener esta informacion siempre disponible

import pickle


class Consolas():
    def __init__(self, nombre, marca, modelo):
        self.nombre = nombre
        self.marca = marca
        self.modelo = modelo
        print(f'Creacion nueva consola. Nombre asignado: {self.nombre}')
        
    def __str__(self):
        return f'Nombre: {self.nombre}\n Marca: {self.marca}\n Modelo: {self.modelo}\n'
    
class listaConsolas():
    consolas = []
    
    def __init__(self):
        fichero_Consolas = open('fichero_consolas', 'ab+') # Formato para agregar informacion binaria
        fichero_Consolas.seek(0)
        
        try:
            self.consolas = pickle.load(fichero_Consolas)
            print(f'Se han agregado {len(self.consolas)} consolas')
        except:
            print('El fichero esta vacio')
        finally:
            fichero_Consolas.close()
            del(fichero_Consolas)
        
    def agregarConsolas(self, consola):
        self.consolas.append(consola)
        self.guardarConsolasFicheroExterno()
        
    def mostrarConsolas(self):
        for c in self.consolas:
            print(c)
            
    def guardarConsolasFicheroExterno(self):
        fichero_Consolas = open('fichero_consolas', 'wb')
        pickle.dump(self.consolas, fichero_Consolas)
        fichero_Consolas.close()
        del(fichero_Consolas)
        
    def mostarContenidoFicheroExterno(self):
        print('El contenido del fichero externo es el siguiente: ')
        for c in self.consolas:
            print(c)

lista_Consolas = listaConsolas()

# consolaUno = Consolas('Play Station 4', 'Sony', 'Slim')
# lista_Consolas.agregarConsolas(consolaUno)
# lista_Consolas.mostarContenidoFicheroExterno()

# consolaDos = Consolas('Xbox One', 'Microsoft', 'Series S')
# lista_Consolas.agregarConsolas(consolaDos)
# lista_Consolas.mostarContenidoFicheroExterno()

# consolaTres = Consolas('WiiU', 'Nintendo', 'WiiU')
# lista_Consolas.agregarConsolas(consolaTres)
# lista_Consolas.mostarContenidoFicheroExterno()

# consolaCuatro = Consolas('Play Station 5', 'Sony', 'Fat')
# lista_Consolas.agregarConsolas(consolaCuatro)
# lista_Consolas.mostarContenidoFicheroExterno()

consolaCinco = Consolas('Xbox One X', 'Microsoft', 'Series X')
lista_Consolas.agregarConsolas(consolaCinco)
lista_Consolas.mostarContenidoFicheroExterno()

# consola2 = Consolas('Xbox', 'Microsoft', 'OneS')
# almacenar_listaConsolas.agregarConsolas(consola2)

# consola3 = Consolas('WiiU', 'Nintendo', 'Wii')
# almacenar_listaConsolas.agregarConsolas(consola3)

# almacenar_listaConsolas.mostrarConsolas()

# Podria prescindir de la clase listaConsolas y hacerlo de forma directa con el codigo escrito aqui abajo, sin embargo dejo la clase para hacerlo como en el curso, ademas que esta clase tambien se ocupa para empaquetar el archivo en un fichero externo

# almacenar_listaConsolas.append(consola1)
# almacenar_listaConsolas.append(consola2)
# almacenar_listaConsolas.append(consola3)
# for c in almacenar_listaConsolas:
#     print(c)