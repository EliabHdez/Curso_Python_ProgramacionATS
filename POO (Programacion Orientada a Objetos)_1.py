# POO - Programacion Orientada a Objetos - Pildoras Informaticas

""" En que consiste???
        Trasladar la naturaleza de los objetos de la vida real al codigo de programacion
     
    Cual es la naturaleza de un objeto de la vida real???
        Los objetos tienen un estado, un comportamiento (que puede hacer?), y unas propiedades
        
    Pongamos un ejemplo: El objeto coche
        Cual es el estado de un coche? Un coche puede estar parado, circulando, aparcado etc...
        Que propiedades tiene un coche? Un coche tiene un color, un peso, un tamaño etc...
        Que comportamiento tiene un coche? Un coche puede arrancar, frenar, acelerar, girar, etc..."""
        
""" Ventajas de la POO
    - Programas dividos en 'trozo', 'partes', 'modulos' o 'clases'. Modularizacion
    - Muy reutilizable. Herencia
    - Si existe fallo en alguna linea de codigo, el programa continuara con su funcionamiento. Tratamiento de excepciones
    - Encapsulamiento """
    
""" Vocabulario de la POO
    - Clase
    - Objeto
    - Ejemplar de clase o Instancia de clase. Ejemplarizar una clase o Instanciar una clase
    - Modularizacion
    - Encapsulamiento / encapsulacion
    - Herencia
    - Polimorfismo """
    
# Clase - Modelo donde se redactan las caracteristicas comunes de un grupo de objetos. Creando 'metodos de acceso' se consigue conectar clases entre si, una clase a otra para que funcionen en conjunto, como una unidad o equipo. Los metodos de acceso solo tienen acceso a ciertas caracteristicas de cada una de las clases

# Ejemplar, intancia u objeto de clase es lo mismo, son sinonimos - Esto es un objeto o ejemplar perteneciente a una clase

# Modularizacion - En parte son las clases que contiene un programa, la modularizacion hace referencia a trozos o partes del programa que como su nombre lo indica son modulos por decirlo de alguna manera. Esto sirve para reutilizar trozos de codigo. Esto de la modularizacion es como un amplificador gradiente, el cual se compone de varios modulos (tornamesa, amplificador, equalizador etc) los cuales tienen funciones diferentes pero que a su vez juntando todos los modulos forman el amplificador como tal, pero que a su vez si uno fallaba los demas modulos seguian funcionando

# La encapsulacion es muy parecida en ciertos aspectos a la modularizacion y se podria decir que van de la mano, ya que la encapsulacion hace referencia a lo que contiene cada clase en particular y que no tiene relacion de forma directa con otra clase, no obstante el que no tenga relacion de forma directa no quiere decir que no tenga nada que ver, ya que todas en conjunto forman el programa entero. Si regresamos al ejemplo del amplificador, la encapsulacion seria lo que cada modulo que conforman el amplificador contiene en su interior y aunque cada modulo tiene su electronica de forma independiente dentro de su gabinete correspondiente y la electronica de los demas modulos no tengan nada que ver con la electronica de los demas funcionan en conjunto para hacer lo que seria todo el amplificador como tal, conectandose estos modulos entre si. Lo mismo es en la programacion, todas las clases aunque son modulos independientes y estan encapsuladas tambien estan conectadas entre si para trabajar en conjunto y asi formar el programa como tal. Otra forma de ver la encapsulacion es que no hay forma de llegar a algo desde fuera

""" Para acceder a las propiedades y comportamientos del objeto se usa lo que se conoce como 'nomenclatura del punto'
Objeto - miCoche
    Para acceder a las propiedades:
        nombreObjeto.propiedad = 'valor'
        
        
        miCoche.color = 'rojo'
        miCoche.peso = 1500
        
Objeto - miCoche
    Para acceder a los comportamientos:
        nombreObjeto.comportamiento()
        
        miCoche.arranca()
        miCoche.frena()
        miCoche.acelera()"""
        
# La clase es la base para despues crear objetos, instancias o ejemplares que pertenezcan a una clase

# El nombre de la clase la primera letra debe ser mayuscula

class Coche(): # Esta clase tiene 4 propiedades y 2 comportamientos
    # Propiedades
    # Todos los objetos, intancias o ejemplares que pertenezcan a esta clase van a tener estas propiedades
    largoChasis = 250
    anchoChasis = 120
    numRuedas = 4
    encendido = False
    
    # Comportamientos
    
    # Los comportamientos vienen determinados por lo que se denominan 'metodos'. Es decir se tienen que establecer metodos para los comportamientos, un metodo para cada comportamiento
    
    # Un metodo es una funcion que pertenece a la clase en la que se esta creando, es de la clase. Mientras que una funcion no pertenece a ninguna clase
    
    # Los metodos se crean con la palabra reservada 'def' (misma palabra reservada para las funciones), las diferencias entre una funcion y un metodo, es que la funcion no pertenece a ninguna clase, mientras que el metodo si pertenece a la clase en la cual se esta creando, ademas el metodo lleva el parametro 'self' de forma obligatoria que hace referencia al objeto mismo, es decir hace referencia al objeto que creemos que va a pertenecer a la clase que tiene ese metodo, mientras que a la funcion le damos como parametro el que nosotros queramos o necesitemos
    
    # Algunas editores al momento de crear un metodo y hacerlo mediante la ayuda del editor al escribir codigo y crear la estructura del metodo pone un pass de forma predeterminada para que si no agregamos codigo dentro del metodo este no genere un conflicto o error al momento de correr el codigo
    
    def arrancar(self):
        self.encendido = True
        
    def estado(self):
        # Podemos omitir el True y solo poner if(self.encendido:). Al momento de omitir el True Python interpetra que es True, si fuera False si lo tendriamos que poner, sin embargo y aunque puedo omitirlo, lo escribo para evitar confusiones
        if(self.encendido) == True:
            return 'El coche esta encendido'
        else:
            return 'El coche esta apagado'
    
# Para construir un objeto debemos salir de la clase y esto lo hacemos igual que todo lo demas, no dando identacion al momento de crear el codigo que hace referencia al objeto, es decir el codigo creador del objeto tiene que estar al mismo nivel de linea que la clase

coche1 = Coche() # Con esto hemos creado un objeto perteneciente a la clase Coche. A esto se le conoce como instancia una clase

# Nomencatura del punto

# Para saber las propiedas, conocer o cambiar el comprtamiento del objeto utilizamos la nomenclatura del punto

# Podemos hacerlo de forma directa desde un print o bien almacenando la propiedad o comportamiento en una variable y despues imprimir esta variable

largoCoche1 = coche1.largoChasis

print('El largo del coche es:',coche1.largoChasis,'cms')
print('El ancho del coche es:', coche1.anchoChasis, 'cms')
print(f'El numero de ruedas que tiene el coche es: {coche1.numRuedas}')
print(f'El coche tiene {coche1.numRuedas} ruedas')

# Como podemos observar en los prints de arriba podemos concatenar textos con codigo de diferente forma, ya sea utilizando el metodo de la 'f' o bien separando por comas el texto del codigo. Con el metodo de la f todo va dentro de las comillas y es necesario darle el espaciado normal si es que lo necesitamos para que al momento de imprimirlo tenga espaciado, mientas que si lo hacemos de la otra forma no es necesario dar espacios, ya que la coma que podemos para separar texto del codigo nos genera dicho espacio, aun asi podemos darle espacio, sin embargo no es necesario adenas de que no habra cambio alguno al momento de imprimirlo en la consola

print(coche1.estado()) # Aqui no hemos llamado al metodo arrancar, por lo tanto la propiedad encendido esta en False, esto nos da como resultado el mensaje que definimos en el if del metodo estado si es que la propiedad encendido no cambia a True

coche1.arrancar() # Aqui hemos llamado al metodo arrancar el cual hace que la propiedad encendido cambie a True
print(coche1.estado()) # Y por ultimo volvemos a imprimir el estado del coche despues de haber llamado al metodo arrancar y podemos ver que ahora nos arroja como mensaje el que pusimos en el if del metodo estado si es que la propiedad encendido cambiaba a True