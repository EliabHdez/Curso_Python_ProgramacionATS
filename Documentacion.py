# Documentacion

""" Documentar un programa

    Que es la documentacion?

        - Es incluir comentarios en clases, metodos, modulos etc
    
    Para que sirve?
    
        - Para ayudar en el trabajo en equipo. Especialmente util en aplicaciones complejas 
        
        - No solo ayuda al trabajar en equipo, tambien es util aun cuando el unico desarrollador del programa sea uno mismo, ya que sirve de ayuda y guia cuando se vuelva a trabajar en la aplicacion o programa meses  años despues """
        
# Para documentar un programa es necesario forsozamente usar las tres comillas (''' <comentario> '''), ya que son estas las que Python toma como validas para un comentario al momento de documentar y tomar este comentario como un comentario de documentacion. En otras palabras hay posibilidad de poder imprimir los comentarios que generamos para documentar nuestro codigo, si estos comentarios estan entre las comillas triples, pero NO es posible hacerlo si generamos estos comentarios con el simbolo de almohadilla o gato

# Ejemplo abajo donde estamos documentando la funcion areaCuadrado, a esta le agregamos un comentarios especificano que hace esta funcion, si ejecutamos el programa de forma normal este comentarios no sera visible ni aparecera en ningun lado ni en ningun momento, pero tenemos la opcion de imprimirlo si asi lo deseamos con el metodo .__doc__ despues del nombre de la funcion. Esta impresion en consola del comentario es posible ya que este comentario se genero mediante las comillas triples, de no ser asi, Python no lo reconoceria y por lo tanto no lo imprimiria, como es el caso del comentario generado mediante la almohadilla donde no tenemos ningun resultado en consola, ya que Python no toma como valida la almohadilla para un comentario documentativo

# No es necesaio ejecutar o llamar a la funcion antes de imprimir la documentacion o el comentario, podemos hacerlo de forma independiente

from modulos import funciones_matematicas
        
def areaCuadrado(lado):
    '''Cálcula el area de un cuadrado. Elevando al cuadrado el valor pasado como parametro'''
    # Comentario adicional de prueba con almohadilla
    lado_cuadrado = lado
    return f'El area del cuadrado es: {lado_cuadrado * lado_cuadrado}'
    
def areaTriangulo(base, altura):
    base_triangulo = base
    altura_triangulo = altura
    return f'El area del triangulo es: {(base_triangulo * altura_triangulo) / 2}'

def funcionPrueba():
    
    """ Comentario de prueba para confirmar que no es necesario llamar a la funcion antes de imṕrimir o llamar a la documentacion o comentario de la funcion en cuestion """
    
    nombre = 'Moises Hernandez'
    
    if len(nombre) > 0 and len(nombre) < 50:
        print('El nombre es válido')
    else:
        print('El nombre es inválido')
        
    return f'El nombre es: {nombre}'
    
print(areaCuadrado(5))
print(areaTriangulo(3,8))

print(areaCuadrado.__doc__)

print('')
print('------- Documentacion/Comentario Funcion Prueba antes de llamarla -------')

print(funcionPrueba.__doc__)

print('')
print('--- Funcion Prueba ---')

funcionPrueba()

# Tenemos otra instruccion que nos permite imprimir la documentacion sin la necesidad de utilizar la funcion print, y esta es la funcion help

# help() --> dentro de los parentesis la funcion de la que quieres obtener la ayuda

help(areaCuadrado)
help(funcionPrueba)

# Con la funcion help se abre la ayuda de Python y nos ofrece una informacion mas detallada, donde nos muestra a que modulo pertenece la funcion que tiene la documentacion, nos muestra la funcion y dentro de esta el comentario o la documentacion generada. Hago incapie en que nos muestra la funcion y el modulo donde pertenece esta funcion ya que es donde puse el comentario documentativo, pero supongo que si esta en una clase, metodo, etc sera lo mismo pero cambiando los detalles en la ayuda con respecto a donde se encuentre dicha documentacion

# La funcion help la visualizamos de forma independiente, no se imprime en la consola junto con lo demas como si lo hicieramos con un print

# Si queremos obtener ayuda de una funcion que se encuentra de una clase, tenemos que especificar en el help primero la clase a la que pertenece la funcion seguido de la nomenclatura del punto y a continuacion el nombre de la funcion de la cual queremos obtener la ayuda

print('')
print('-------- Obteniendo ayuda de una funcion dentro de una clase --------')

class Areas:
    """ Clase para calcular areas de figuras geometricas """
    
    def areaCuadrado(lado):
        '''Calculando area de un cuadrado'''
        # Comentario adicional de prueba con almohadilla
        lado_cuadrado = lado
        return f'El area del cuadrado es: {lado_cuadrado * lado_cuadrado}'
    
    def areaTriangulo(base, altura):
        """ Calculando el area de un triangulo """
        base_triangulo = base
        altura_triangulo = altura
        return f'El area del triangulo es: {(base_triangulo * altura_triangulo) / 2}'
    
help(Areas.areaCuadrado)

# Tambien podemos obtener una ayuda mas general de una clase, donde nos brindara toda la documentacion o comentarios que contenga esta clase ya sea en la clase misma, en sus funciones o en su codigo en general

help(Areas)

# De igual manera podemos documentar modulos y solicitar la ayuda de la documentacion o comentarios establecidos en los modulos que hayamos importado. Al solicitar la documentacion de los modulos nos aparece la documentacion o comentarios generados en el modulo o archivo como tal como los comentarios o la documentacion generados en las clases, funciones etc que contenga este modulo

help(funciones_matematicas)