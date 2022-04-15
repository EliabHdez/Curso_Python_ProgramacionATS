# Funciones Decoradoras

# Son funciones que añaden funcionalidades a otras funciones

""" Estructura de un decorador
    
    - Una funcion decoradora esta conformado por 3 funciones (A, B y C) donde A recibe como parametro a B para devolver C
    
    - Un decorador devuelve una funcion 
    
    def funcion_decoradora(funcion):
        def funcion_interna():
            < codigo de la funcion interna >
        return funcion_interna
"""

def funcion_decoradora(funcion_externa):
    
    def funcion_interna():
        
        print('El resultado de la operacion es: ')
        
        funcion_externa()
        
        print('¡El cálculo se ha realizado con éxito!')
        
    return funcion_interna

# Para que esta funcion decoradora surta efecto en las demas funciones, hay que decorar, decirle al programa las funciones que queremos que lleve esta decoracion o esta funcion decoradora, y esto lo hacemos mediante la nomenclatura @nombre_funcion_decoradora, esta nomenclatura debe de ir encima de la funcion que queremos que lleve la funcion decoradora

@funcion_decoradora
def suma():
    print(15 + 20)
    
def resta():
    print(30 - 10)

@funcion_decoradora    
def multiplicacion():
    print(5 * 12)
    
print('--- Funcion suma ---')
suma()

print('--- Funcion resta ---')
resta()

print('--- Funcion multiplicacion ---')
multiplicacion()

# Funciones decoradoras con parametros en funciones externas

def funcionDecoradoraUno(funcion_externa):
    
    def funcion_interna(*args): # Con la nomenclatura *args (que 'args' es un estandar, una convencion, se le puede dar cualquier nombre), le estamos diciendo que la funcion externa a la cual le vamos a agregar la funcion decoradora va a recibir o tiene que recibir parametros
        
        print('El resultado del cálculo es:')
        
        funcion_externa(*args) # Aqui le agregamos ese parametro ya que aqui es donde estamos llamamando por decirlo de alguna manera a la funcion externa
        
    return funcion_interna

@funcionDecoradoraUno
def suma_uno(num1, num2):
    print(num1 + num2)

@funcionDecoradoraUno
def resta_uno(num1, num2):
    print(num1 - num2)

@funcionDecoradoraUno  
def mult_uno(num1, num2):
    print(num1 * num2)
    
@funcionDecoradoraUno
def opLibre(num1, num2, num3, num4):
    print(num1 + num2 * num3 / num4)
    
print('--- Funcion suma con parametros ---')
suma_uno(13,5)

print('--- Funcion resta con parametros ---')
resta_uno(7,1)

print('--- Funcion multiplicacion con parametros ---')
mult_uno(9,8)

print('--- Funcion operacion libre con parametros ---')
opLibre(9.2, 8, 1.5, 7)

# Adicionalmente podemos agregarle otro parametros a la funcion interna, el cual hace referencia a keywords, que es esto de keywords? Es lo que se conoce como clave-valor y esto es cuando especificamos que un valor corresponde a algo en especifico, este parametro se suele definir con kwargs que es como la abreviacion y conjuncion de keywords con arguments. Veamoslo en un ejemplo practico para que sea mas entendible

print('--- Parametro kwargs ---')

def funcionDecoradoraDos(funcion_externa):
    
    def funcionInterna(*args, **kwargs):
        
        print('El resultado de la potencia es:')
        
        funcion_externa(*args, **kwargs)
        
    return funcionInterna

def potencia(base, exponente):
    print(pow(base, exponente))
    
potencia(5, 3)

# La clave-valor es cuando especificamos que corresponde a que, en otras palabras cuando ocupamos una clave y a esa clave le damos un valor, esto a modo de identificacion por decirlo de alguna manera, veamos un ejemplo

def potenciaClaveValor(base, exponente):
    print(pow(base, potencia))
    
    potenciaClaveValor(base=5, exponente=3) # Esto es clave-valor, donde al valor de 5 le estamos dando la clave 'base' y al valor de 3 le estamos dando la clave 'exponente'. Si en la funcion interna quitamos el parametro **kwargs al momento de llegar a esta parte del codigo nos daria un error, ya que el parametro *args solo sirve para dar o asignar varios parametros, pero no cuando estos parametros o valores tiene una clave, para eso agregamos el parametro **kwargs