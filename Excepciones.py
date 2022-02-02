# Excepciones - Pildoras Informaticas

# Las excepciones son errores que ocurren durante la ejecución del programa. La sintaxís del código es correcta pero durante la ejecución ha ocurrido 'algo inesperado'

# def suma(num1, num2):
#     return num1 + num2

# def resta(num1, num2):
#     return num1 - num2

# def multiplicacion(num1, num2):
#     return num1 * num2

# def division(num1, num2):
#     return num1 / num2

# numeroUno = int(input('Ingrese el primer número: '))

# numeroDos = int(input('Ingrese el segundo número: '))

# operacion = input('Digite la operación matematica a realizar: ')

# if operacion == 'suma':
#     print(suma(numeroUno, numeroDos))
    
# elif operacion == 'resta':
#     print(resta(numeroUno, numeroDos))
    
# elif operacion == 'multiplicacion':
#     print(multiplicacion(numeroUno, numeroDos))
    
# elif operacion == 'division':
#     print(division(numeroUno, numeroDos))
    
# else:
#     print('La operacion ingresada no es válida')
    
# print('Continuación de la ejecución del programa')

# Una excepcion clara es dividir un numero entre 0. Ya que la division de un número entre 0 es infinita, esta considerada como una indefinicion. En otras palabras no podemos dividir un numero entre 0. Si corremos el programa actual y hacemos esta division, veremos que el programa nos arroja un error, y esto es un ejemplo claro de una excepcion, ya que no hay error de sintaxis, error de identado, error de tipo etc etc etc, no hay ningun tipo de error en el codigo, sin embargo al generar esta division el programa genera un error y se detiene en esa linea de codigo

# Podemos controlar este tipo de ejecucion de errores, para que la ejecucion del programa continue. A esto se le conoce como 'manejo o control de excepciones'. Y esto nos sirve para que si nuestro codigo tiene lineas vitales para la ejecucion del programa despues de donde arroja una excepcion, el programa no se caiga ni se detenga por estas excepciones, si no que intente realizar la ejecucion de esa linea que marca la excepcion y si no lo consigue que continue con la ejecucion del codigo que sigue y asi proceder con la ejecucion del codigo y del programa

# Para controlar las excepciones lo hacemos mediante las instrucciones try y except. Estas instrucciones funcionan de una manera muy similar al if - else. Donde si el try se cumple o se logra ejecutar ignora el except y continua con la ejecucion del programa y viceversa, si el try no se logra ejecutar, pasa al except lo ejecuta y continua con la ejecucion del programa

# Para controlar la excepcion es necesario utilizar el try y el except en la linea del codigo que nos genera el error. En el try ponemos el codigo que queremos que intente ejecutar y el except es importante que pongamos el error que nos arroja cuando no estamos controlando la excepcion seguido del codigo que queramos que ejecute en el except, este codigo va en el cuerpo

# Si el error que nos a generado la linea coincide con el error que hemos descrito o estipulado en el except ejecutara el codigo descrito en el cuerpo del except, de no coincidir los errores el programa se detendra y se caera de igual manera que lo hace cuando no estamos controlando la excepcion. En otras palabras si el error generado en la linea no es el mismo descrito en el except el control de excepciones con el try y el except no funcionara

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print('No se puede dividir entre 0')
        return 'Operación no válida'

# Aun con el control de excepciones tenemos dos inconvenientes. El primero es que aun funcionando el try el programa seguira corriendo, lo cual hara que nos pida la operacion matematica y no tiene caso alguno la operacion matematica si no tenemos valores numericos ingresados. Y el segundo es que lo anterior nos lleva a otro error que nos genera una excpecion, ya que al no haber valores numericos el programa no sabe que hacer y por ende no puede hacer ninguna operacion matematica, lo cual nos arroja el error NameError, el cual hace referencia a que al no tener la variable el valor correcto esta variable la toma como no definida. Esto (tanto la excepcion como el que pida la operacion matematica a realizar si el dato ingresado NO es un numero) lo podemos solucionar generando un bucle infinito para que mientras el usuario nos ingrese un dato que no sea numerico, se lo vuelva a solicitar y asi no permitir que el programa avance a la linea de codigo que pide la operacion. Este bucle tiene que encerrar el control de excepciones

while True:
    try:
        numeroUno = int(input('Ingrese el primer número: '))

        numeroDos = int(input('Ingrese el segundo número: ')) # Que pasa si en esta linea al momento de que el usuario tenga que ingresar un valor numerico, ingresa algun otro valor? Pues tambien tendriamos una excepcion, ya que nuestro codigo esta bien, no hay errores de sintaxis ni de ningun otro tipo, pero el usuario puede ingresar cualquier valor y si este no es numerico estaria generando un error que esta fuera de nuestro alcance y que tampoco es generado por estar mal el codigo, en este caso tendriamos que controlar esta excepcion de igual manera con un try y un except
        break
    except ValueError:
        print('Los valores ingresados no son válidos. Se requieren valores numericos. Intentalo de nuevo')

operacion = int(input('''Operaciones matematicas disponibles:
    1 - Sumar
    2 - Restar
    3 - Mulltiplicar
    4 - Dividir
    Selecciona la opcion con la operacion a realizar: '''))

while operacion < 1 or operacion > 4:
    try:
        operacion = int(input('''Opción no válida. Opciones válidas:
    1 - Sumar
    2 - Restar
    3 - Mulltiplicar
    4 - Dividir
    Inténtalo de nuevo. Selecciona la opción deseada: '''))
    except ValueError:
        print('Solo se acepta un valor numerico indicando la operacion deseada')
        

if operacion == 1:
    print(suma(numeroUno, numeroDos))
elif operacion == 2:
    print(resta(numeroUno, numeroDos))
elif operacion == 3:
    print(multiplicacion(numeroUno, numeroDos))
elif operacion == 4:
    print(division(numeroUno, numeroDos)) 
# else:
#     print('La operacion ingresada no es válida')
    
print('Continuación de la ejecución del programa')

# Podemos programar varias excepciones en un mismo try. Ademas tambien podemos hacer una excepcion general, esto quiere decir que no ponemos un error en concreto, si no que con cualquier error sea del tipo que sea estara saltando la excepcion general

# Y tenemos otra instruccion que es 'finally' esta se ejecuta si o si, aunque haya errores esta se estara ejecutando. Esta instruccion puede ir de forma directa en un try, prescindiendo de los except y esta se ejecutara de igual manera, haya errores o no en el try, finally se ejecutara. Lo que no se puede es tener un try solo, sin excepts o finally porque esto generara un error de sintaxis

# Vamos a ver lo antes mencionado en otro ejemplo de codigo ya mas breve y abarcando todo en un solo ejemplo

# Este ejemplo sera diferente al anterior, ya que todo el codigo quedara dentro de una funcion, por lo tanto la funcion sera la encargada de hacerlo todo

def divide():
    try:
        numero1 = float(input('Ingrese el primer numero --> '))
        numero2 = float(input('Ingrese el segundo numero --> '))
        resultado = numero1 / numero2
        print(f'El resultado es: {resultado}')
    except ValueError:
        print('Error: Solo se acpetan valores numericos')
    except ZeroDivisionError:
        print('Error: No se puede dividir entre 0')
        
    # En este ejemplo estamos haciendo uso de varios except en el mismo try, ya que como tal el codigo de la funcion nos puede dar varios posibles errores, por lo tanto para simplificarlo y hacer excepciones de todos ellos podemos hacerlo de generando todas las excepciones posibles dentro del mismo try
    
    print('Calculo finalizado')
    
divide()

def divide2():
    try:
        numero1 = float(input('Ingrese el primer numero --> '))
        numero2 = float(input('Ingrese el segundo numero --> '))
        resultado = numero1 / numero2
        print(f'El resultado es: {resultado}')
    except:
        print('Ha ocurrido un error. Verifica los datos ingresados') # Esto seria una excpecion general, la cual ocurra el error que ocurra, ya sea en este caso en especifico un ValueError o un ZeroDivisionError ejecutara una sola excepcion y nos imprimira siempre el mismo mensaje de error sea cual sea el error generado
    
    print('Calculo finalizado')
    
divide2()

print('*****Intruccion finally*****')

def divide3():
    try:
        numero1 = float(input('Ingrese el primer numero --> '))
        numero2 = float(input('Ingrese el segundo numero --> '))
        resultado = numero1 / numero2
        print(f'El resultado es: {resultado}')
    finally:
        print('Este es el print del finally. Este se ejecuta siempre si o si')
        
    # Como lo mencionamos anteriormente el finally puede ir solamente con el try, y lo que hara es que si el try da error o no el finally se ejecutara, de echo el finally se ejecutara antes de marcar el error del try en caso de haberlo
    
    # Con except puede ser que no veamos la diferencia de tener un finally o no, sin embargo si la hay y se ocupa en muchos casos, donde tener o no tener finally marca la diferencia, puede que mas tarde en el curso veamos algun ejemplo, sin embargo en nuestro ejemplo tan sencillo podemos ver la diferencia de tenerlo o no, ya que no hay except de por medio y esto provoca que si tenemos el finally y ejecutamos la funcion el try se ejcutara y sin importar el resultado del try se ejecutara el print del finally, a diferencia de que si no lo tenemos y solo queremos imprimir el print con el try solo veremos que nos arroja un error de sintaxis, debido que no puede haber un try sin except o finally
    
    print('Calculo finalizado')
    
divide3()