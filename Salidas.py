# Salidas

# Hay varias formas de poder imprimir en consola la salida de datos, si bien se tiene que hacer mediante el print(), la forma de ponerlo en este es variada, es decir que hay varias maneras en que podemos concatenar mensajes con variables

# Lo que se va a ver realmente en este tema, son las diferentes formas de concatenar variables en un mensaje al momento de imprimirlos en consola

nombre = "Moises"
edad = 31

print("Hola",nombre, "tienes", edad, "años") # Esta es una forma, sin embargo no es la unica, ademas de ser algo engrollosa y corremos el riesgo de que nos falte alguna coma, comillas, mala sintaxis etc

print("-------------------")

# La otra forma es la llamada format()

print("Hola {} tienes {} años".format(nombre,edad))

print("-------------------")

# La otra forma es de igual manera con el metodo format, pero en su version abreviada (f al inicio del todo)

print(f"Hola {nombre} tienes {edad} años")