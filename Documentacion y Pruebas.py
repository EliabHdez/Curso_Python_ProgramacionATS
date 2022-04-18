# Documentacion y Pruebas

# Vamos a utilizar la documentacion para realizar pruebas. Para esto vamos a necesitar hacer uso del Módulo doctest

# Esto nos sirve para saber si el codigo que vamos escribiendo funcionara de manera correcta antes de poner el programa o aplicacion en produccion y esto lo podemos hacer mediante la documentacion

def areaTriangulo(base, altura):
    
    """ Calcula el area de un Triangulo
    
        Para hacer pruebas mediante la documentacion primero debemos situarnos entre las comillas triples de apertura y cierre del comentario y posteriormente poner tres signos de mayor, un espacio y el nombre de la funcion en este caso. Y por debajo debemos especificar el resultado que nos deberia arrojar la funcion. Si al momento de ejecutar no pasa nada quiere decir que todo va bien, de lo contrario nos arrojara un resultado donde nos especifica que el ejemplo es fallido, el resultado esperado (que es el que nosotros especificamos) y el resultado obtenido
    
        >>> areaTriangulo(3,6)
        9.0
        
        >>> areaTriangulo(5,8)
        20.0
         
    """
    return (base * altura) / 2

import doctest

doctest.testmod()

# El resultado que nosotros pongamos en nuestras pruebas debe de ser igual resultado que deberia arrojar el resultado final como tal, es decir, que si nosotros ponemos como resultado una cadena este debe ser igual tanto en el resultado obtenido como en el resultado esperado, si lleva puntos, acentos, comas, dos puntos, mayusculas etc. Veamos un ejemplo

# Se pueden realizar varias pruebas o test dentro de una misma documentacion o comentario, solo es cosa de especificarlas, si no pasa nada quiere decir que todas las pruebas han ido correctamente, si llegase a haber un error en alguna de ellas, no estaria marcando en cual esta el error concretamente

def suma(num1, num2):
    
    """ Suma dos numeros que se le pasen como parametros
    
        >>> suma(2,9)
        'La suma de los dígitos es: 11'
        
        >>> suma(4,5)
        'La suma de los dígitos es: 9'
        
        >>> suma(3,3.5)
        'La suma de los dígitos es: 6.5'
    
    """
    
    return f'La suma de los dígitos es: {num1 + num2}'

doctest.testmod()

# Dejo cometada la funcion de abajo que es la que nos arroja error abajo mencionado, meramente para que podamos confirmar las pruebas siguientes sin que esta no afecte en el proceso de verificacion

# def suma1(num1, num2):
    
#     """ Suma dos numeros que se le pasen como parametros
    
#         >>> suma1(5,3)
#         'La suma de los dígitos es: 8'
    
#     """
    
#     return f'La suma de los digitos es: {num1 + num2}'

# doctest.testmod()

# Como podemos observar en el caso anterior nos arroja un error ya que el resultado obtenido no es igual al esperado que es la cadena de texto mas la operacion matematica de la suma de los numeros. La identificaicon de los resultados es tan sutil que hasta por un acento o una letra de mas podriamos ver un error, como lo podemos observar en el ejemplo anterior donde por el acento de la i en la palabra digitos nos da como resultado un error, ya que en el esperado tiene acento y en el obtenido no

def confirmarEmail(mail):
    
    """ Comprobacion de arroba en el email del usuario. Si tiene 2 o mas, si esta al principio o final del email etc
    
        >>> confirmarEmail('moises.hdez@paperforall.com')
        True
        
        >>> confirmarEmail('@moises.hdezpaperforall.com')
        False
        
        >>> confirmarEmail('moises.hdezpaperforall.com@')
        False
        
        >>> confirmarEmail('moises.hdezpaperforall.com')
        False
        
        >>> confirmarEmail('moises.@hdez@paperforall.com')
        False
        
    """
    
    arroba = mail.count('@')
    
    if arroba != 1 or mail.rfind('@') == len(mail)-1 or mail.find('@') == 0 or mail.rfind('@') == len(mail) == 0: # Esta ultima comprobacion esta como de mas ya el primer condicional tambien la cumpliria
        return False
    else:
        return True
    
doctest.testmod()