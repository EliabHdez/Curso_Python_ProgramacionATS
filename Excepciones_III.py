# Excepciones III - Pildoras Informaticas

# Lanzamiento de excepciones

# Con lanzamiento de excepciones no nos referimos a la excepciones que lanza el programa cuando ocurre un error. Mas bien nos referimos a que nosotros como programadores seamos quienes de forma intencional provoquemos y lancemos excepciones cuando ocurra alguna circunstancia en nuestro codigo. En pocas palabras que no sea el programa si no nostros de forma intencionada.

# Lo anteriormente mencionado lo hacemos con la instruccion Raise. Esta intruccion sera la base para que en un futuro creemos excepciones propias y con esto es donde adquiere la verdadera utilidad (Esto ultimo lo veremos mas adelante cuando veamos la programacion orientada a objetos - POO)

import math

def evaluaEdad(edad):
    edad = int(input('Introduzca su edad: '))
    if edad < 0:
        raise TypeError('No se permiten numeros negativos para la edad') # Es importante recordar que si hacemos uso del raise necesitamos ponerle a este el error que queremos que arroje, puede ser cualquiera como el TypeError, ZeroDivisioError, NameError etc...
    
    # Con el raise estamos generando un error, una excepcion nosotros mismos cuando asi lo deseemos, en este caso lo estamos haciendo cuando el usuario al momento de ingresar su edad introduzca un numero negativo. Tiene sentido ya que al momento de ingresar un dato erroneo lo mas factible es que el programa se caiga, nos arroje un error y nos diga cual es el error. Adicionalmente el raise como podemos ver nos permite ingresar un texto o algo adicional con lo cual podemos especificar cualquier cosa, en este caso el error que esta comentiendo el usuario al ingresar su edad
    if edad < 10:
        return 'Eres un niño'
    elif edad < 18:
        return 'Eres menor de edad y eres un joven'
    elif edad < 60:
        return 'Eres mayor de edad y ya eres un adulto maduro'
    elif edad >= 60:
        return 'Eres una persona de la tercera edad. Cuidate...'

print(evaluaEdad(31))

print('Fin del programa 1')

def calculaRaiz(num):
    if num < 0:
        raise ValueError('No se aceptan numeros negativos')
    else:
        return math.sqrt(num)
        
digito = int(input('Introduce un numero --> '))

try:
    print(calculaRaiz(digito))
except ValueError as ErrorNumeroNegativo: # Podemos darle un nombre o un alias al error con la instruccion 'as'. Esto es como crear una variable y que el alias sea el nombre de la variable y el tipo de error que especificamos en este caso ValueError sera el valor de dicha variable. Si el error tiene un mensaje este se imprimira junto con el tipo de error. Y en el print ponemos el alias que le dimos al error, esto seria como poner el nombre de la variable para que nos imprima su valor
    print(ErrorNumeroNegativo)

print('Fin del programa 2')

# Al momento de generar el error y este aparecernos en consola, en esta ultima nos aparecen las lineas donde se esta generando dicho error, tanto la linea donde salta la excepcion como la linea que la esta provocando, que en el ejemplo anterior la linea que nos arroja la excepcion es la 'linea 32' y las que esta generando el error es la 'linea 38', antes de hacer uso del try, ya que el print sin el try se recorre una linea para arriba, si comentamos el try la linea que genera el problema seria la linea 39. En otras palabras seria la linea que contiene el llamado de la funcion donde se almacena el digito ingresado por el usuario y que este digito es el que se va a ocupar en la funcion para calcular la raiz cuadrada