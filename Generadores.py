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