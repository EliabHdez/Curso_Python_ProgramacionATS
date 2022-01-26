# Funciones

# Conjunto de lineas de código agrupadas (bloque de código) que funcionan como una unidad realizando una tarea específica

#Las funciones en Python pueden devolver valores

# Las funciones en Python pueden tener parámetros/argumentos

# A las funciones también se les denomina métodos cuando se encuentran definidas dentro de una clase

""" Utilidad de las funciones

    Reutilizar el codigo (si es necesario o cuando sea necesario) """
    
""" Sintaxís de las funciones (def es una palabra reservada para la creacion de funciones)
    
    def nombre_funcion():
        Instrucciones de la función
        return (opcional)
        
    def nombre_función(parámetros)
        Instrucciones de la función
        return (opcional) """
        
""" Ejecutar función
    
    nombre_funcion()
    
    nombre_funcion(parámetros) """
    
def mensajes(): # Aqui estamos declarando la funcion
    print('Aprendiendo funciones')
    print('Nueva funcion')
    print('Hola Mundo')
    
# Es importante recordar que una funcion no se ejecutara hasta que esta no sea llamada

mensajes() # Aqui estamos llamando a la funcion

# Funciones con parametros/argumentos

def suma():
    num1 = 5
    num2 = 3
    resultado = num1 + num2
    print(resultado)
    
suma()

# En el caso anterior vemos una funcion simple, sin parametros, pero que pasa si queremos reutilizar esta funcion y cada vez que la reutilicemos necesitamos o queremos que los valores de num1 y num2 sean diferentes? Pues aqui es donde entran los parametros para poder hacer esto

def suma2(num1, num2):
    resultado = num1 + num2
    print(resultado)
    
# Al momento de declarar los parametros ya no es necesario asignar los valores de num1 y num2 dentro del cuerpo de la funcion, ya que lo estariamos haciendo al momento de llamar la funcion, y asi cada vez que la llamemos o reutilicemos podemos agregar valores diferentes y estos se almacenaran en los parametros asignados a la funcion. Los valores se almacen en el orden de los parametros

# Se le pueden pasar parametros de cualquier tipo de dato, numericos enteros o flotantes, cadenas o strings y / o booleanos, de echo pueden estar mezclados

print('Llamada 1')
suma2(5,7)

print('Llamada 2')
suma2(2,6)

print('Llamada 3')
suma2(220,165)

# Con esto podemos ver de forma mas clara la utilidad de las funciones

# Return en una funcion

# Podria parecer que el utilizar el return no tiene sentido y hasta se vuelve mas engrolloso y se le da mas vuelta y ms codigo, ya que se podria poner de forma directa por ejemplo el print del resultado, sin embargo aunque asi pueda parecer, tiene gran potencial y gran utilidad tener un return ya que este se puede almacenar en una variable y despues reutilizar esta variable por poner un ejemplo practico del porque y para que nos sirve el return

# Si tenemos un return en nuestra funcion y mandamos a llamar la funcion pareciera que no hace nada y esto es porque aunque el programa se esta ejecutando correctamente el return es eso un return, esta regresando un valor, pero este no actua como un print o algo mas, por lo tanto si queremos visualizar el return tendriamos que ocupar el print al momento de llamar la funcion

""" Ejemplo llamada funcion con return
    
    def funcion(num1, num2):
        resultado = num1 + num2
        return resultado
        
    print(funcion(5,8))"""

print('Funcion con Return')

def conRegreso(num1, num2):
    resultado = num1 + num2
    return resultado

resFuncion = conRegreso(5,8)

print(resFuncion)