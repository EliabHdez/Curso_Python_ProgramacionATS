# Entrada de Datos

# La entrada de datos se hace mediante el metodo input(), sin embargo este metodo solo almacena y permite datos de tipo string, si queremos ingresar un dato de tipo numerico ya sea entero o flotante no no lo va a permitir hasta cierto aspecto y por que digo hasta cierto aspecto? Porque si bien si lo vamos a poder almacenar en ingresar el dato no sera como tal de tipo numerico, si no de tipo string

#nombre = input("Digite su nombre: ")

#print(f"Hola {nombre}")

edad = input("Digite su edad: ") # Lo que estamos haciendo en ingresar un numero, sin embargo este numero para Python no es un dato de tipo numerico, es de tipo string

print(f"Su edad es {edad}") # Por lo tanto aqui vemos que nos permite generar la entrada de datos aunque este sea un numero, pero no lo podemos tratar como tal, si dentro de la variable numero ejecutamos una suma {numero + 1} veremos que nos arroja un error, esto es debido a que para Python este numero es de tipo string y no se pueden sumar numeros con strings

# Para poder trabajar con numeros en las entradas necesitamos añadir los metodos int o float (segun sea el caso) antes del input

numEnt = int(input("Digite un numero: "))
print(f"El numero ingresado es: {numEnt}. Si sumamos 31 el resultado final es: {numEnt + 31}") # Como podemos observar aqui ya nos permite hacer una suma o cualquier operacion matematica con el valor de la variable ya que nos encargamos de cambiar el tipo de dato de string a number con el metodo int, sin embargo el resultado siempre sera un entero debido a que el metodo es de tipo numerico entero

numFloat = float(input("Digite el valor de PI: "))
print(f"El valor de PI es: {numFloat}. Multiplicado por 5, el resultado final es {numFloat * 5}") # Al igual que en el caso anterior aqui pudimos ejecutar una operacion matematica, solo que esta vez fue con numeros flotantes debido a que utilizamos el metodo float()