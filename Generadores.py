# Generadores - Pildoras Informaticas

# Los Generadores son estructuras que extraen valores de la función (del mismo generador) y se almacenan en objetos iterables, esto quiere decir que lo que se extraiga se va a poder recorrer con un bucle for o while o con alguna otra estructura como iteradores o el metodo next

# Los valores extraidos se almacena de uno en uno

# Cada vez que un generador almacena un valor, este permanece en estado pausado hasta que se solicita el siguiente. Esta caracteristica es conocida como 'suspensión de estado'

""" Las utilidades que tienen por mencionar algunas son:
    
    - Son más eficientes que las funciones tradicionales
    - Muy útiles con listas de valores infinitos
    - Bajo determinados escenario, será muy útil que un generador devuelva los valores de uno en uno """
    
""" Sintaxis de un generador
    
    - Basicamente la misma que la de una funcion
    
        def --> Palabra reservada
        nombreFuncion
        codigo del cuerpo
        yield --> Palabra reservada
        
        Y tambien adicionalmente puede tener un 'return' 
        
    def miGenerador():
        codigo del cuerpo a ejecutar
        yield
    """

# La instruccion yield es la que se encarga de construir el objeto iterable que va a almacenar los valores del objeto generador 
    
# Vamos a crear un programa que nos genere una lista de numeros pares. De entrada se hara con una funcion tradicional y posteriormente vamos a copias y modificar el codigo para convertirlo en un generador y de esta manera ver la diferencia que hay entre los dos
    
print('Programa con funcion tradicional')
    
def generaPares(limite):
    num = 1
    miLista = []
    while num < limite:
        miLista.append(num * 2)
        num += 1
    return miLista

print(generaPares(10))

# Generador

print('Programa con Generador')

def generaPares2(limite):
    num = 1
    while num < limite:
        yield num*2
        num += 1
    
devuelvePares = generaPares2(10)

# Si lo que queremos es que nos arroje valor por valor, uno a la vez que es el fuerte de los generadores en comparacion con las funciones tradicionales, lo tenemos que hacer mediante el metodo next(). Este metodo lo que hace es ir extrayendo a cada llamada del generador el siguiente valor y de ahi el nombre next

print(next(devuelvePares))

print('Aqui podria ir mas codigo')

print('Despues de varias lineas de codigo de nuestro programa, volvemos a llamar al siguiente valor del generador')

print(next(devuelvePares))

print('Aqui podria ir mas codigo')

print('Volvemos a llamar una vez mas al generador para el siguiente valor y asi sucesivamente')

print(next(devuelvePares))

# for i in devuelvePares: # el bucle for nos sirve para recorrer todos los elementos del objeto generador y asi obtener el objeto en su totalidad
#     print(i)

# Como podemos ver el generador no a construido del todo el objeto con todos los numeros pares que solicitamos en el limte del generador, esto hace que no se consuman recursos de mas e innecesarios cuando no necesitamos todos los valores del objeto en su totalidad y asi optimizar recursos y velocidad solicitando solo los valores del objeto generador conforme los vayamos requiriendo

# Instruccion 'yield from'

# La instruccion yield from tiene la utilidad de simplificar el código de los generadores en el caso de utilizar bucles anidados dentro del generador

# En python cuando ponemos un asterisco (*) antes de un parametro o argumento en una funcion l estamos diciendo que va a recibir un numero indeterminado de elementos, que podrian ser 1, 2, 3, 5 o 20 y que ademas esos argumentos o elementos los va a recibir en forma de tupla

def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        yield elemento
        
ciudadesDevueltas = devuelveCiudades('Madrid', 'Barcelona', 'Valencia', 'Bilbao')

print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))

# Los elementos del generador tienen a su vez subelementos y con esto no queremos decir que cada elemento tenga otro elemento como tal dentro, si no que lo que conforma el elemento es un subelemento. En otras palabras los elementos que son ciudades por ejemplo Madrid, tiene a su vez subelementos y estos subelementos son las letras que conforman la palabra Madrid

# Para poder acceder a estos subelementos (letras) necesitariamos hacer uso de un bucle for anidado en el generador

# Sin embargo la instruccion yield from simplifica el codigo al hacer esto y con el uso de esta eliminamos el uso del bucle anidado

def devuelveCiudades2(*ciudades):
    for elemento in ciudades:
        # for subElemento in elemento: # Con este bucle for anidado accedemos a los subelementos de los elementos del generador
            yield from elemento # Con el yield from como podemos observar obtenemos el mismo resultado eliminando el uso del bucle for anidado. Basicamente le estamos diciendo 'devuelvenos desde el elemento' que se podria traducir a que el elemento es el objetivo y que nos devuelva un resultado desde este elemento
            
ciudadesDevueltas2 = devuelveCiudades2('Madrid', 'Barcelona', 'Valencia')

print(next(ciudadesDevueltas2))
print(next(ciudadesDevueltas2))
print(next(ciudadesDevueltas2))
print(next(ciudadesDevueltas2))
print(next(ciudadesDevueltas2))
print(next(ciudadesDevueltas2))
print(next(ciudadesDevueltas2))
print(next(ciudadesDevueltas2))
print(next(ciudadesDevueltas2))

# Y por ultimo el resultado de este ultimo generador utilizando tanto un bucle for anidado como la instruccion yield from que uno de los puntos de este tema es que no nos arroja como resultado el elemento del generador, si no los subelementos de un elemento del generador, que en este caso nos esta devolviendo la 'M' y la 'a' correspondientes al primer elemento que es 'Madrid' y estas dos letras corresponden al numero de veces que hemos ejecutado el print con la variable que guarda el generador, si lo imprimimos mas veces, nos ira dando las siguientes letras correspondientes al elemento 'Madrid' y asi consecutivamente, si imprimimos mas veces del numero de letras que contenga el elemento Madrid, se seguira con el siguiente elemento del generador ('Barcelona', 'Valencia' etc), pero de igual manera devolviendo los subelementos de los elementos en cuestion