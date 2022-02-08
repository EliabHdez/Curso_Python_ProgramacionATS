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