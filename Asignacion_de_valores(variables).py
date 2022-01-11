# La asignacion de valores tambien se conoce como la creacion de variables

"""
    En python existen tres tipos de datos:
        - Numericos
        - Texto
        - Booleanos
"""

# En Python no es necesario especificar el tipo de variable que queremos declarar, solo basta con crearla dandole el nombre y valor correspondiente

print("***********")

# Datos numericos (enteros y flotantes)

numero = 10

print(numero)
print(type(numero)) # La funcion type() nos permite saber el tipo de dato que asignamos a una variable. Python lo hace de forma automatica

print("***********")

# Datos textuales (strings)

nombre = "Moises Hernandez"
cadena = 'Estoy "estudiando"' # Se pueden combinar las comillas para que si es necesario podamos tener mensajes entre comillas, es importante que las comillas sean diferentes, ya que de ser iguales las internas como las externas, python interpretara como apertura y cierre las primeras que encuentre en lugar de interpretar que dicha letra, palabra o texto tiene que ir entre comillas

print(nombre)
print(type(nombre))
print(cadena)
print(type(cadena))

print("***********")

# Datos booleanos

# Los datos booleanos son 2: True y False

valor = True
valor2 = False

print(valor)
print(valor2)

print("***********")

# Podemos hacer operaciones matematicas con variables, concatenar variables o hacer las operaciones de forma directa. Hay que tener en cuenta que las operaciones en python tambien respetan el orden de los signos (PEMDA)

numero1 = 10
numero2 = 6.7

suma = numero1+numero2

print(suma)

resultado = numero1 + numero2 * 10 / 6
resultado2 = (numero1 + numero2) * 10 / 6

print(resultado)
print(resultado2)

# Como podemos ver, los resultados son diferentes debido a que esta ealizando las operaciones matematicas de acuerdo al PEMDA (jerarquia de los signos)

print("***********")

# Tipado dinamico

# Python es un lenguaje de tipado dinamico, esto quiere decir que una variable puede cambiar su valor o incluso su tipo de dato conforme transcurre el programa y a lo largo del codigo

valor = 10

print(valor)

valor = "Eliab"

print(valor)

# Como podemos observar tenemos la misma variable y como sabemos que es la misma variable, porque tiene el mismo nombre, no puede haber dos variables diferentes que se llamen igual, por lo tanto si el nombre no cambia quiere decir que es la misma variable. Entonces en este caso la variable valor empezo con el valor de 10 y posteriormente cambio a Eliab. No solo cambio su valor, si no que tambien cambio su tipo de dato, paso de ser un dato numerico a un string, y asi podria ser con cualquier otro tipo de dato