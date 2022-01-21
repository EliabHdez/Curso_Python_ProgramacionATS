# Ejercicio 3 - Comprobar vocales

# Hacer un programa que pida un caracter e indique si es una vocal o no

letra = input("Introduzca una letra, numero o caracter --> ").lower() # Alejandro lo hizo de esta manera, donde puso el metodo lower() de forma directa en la variable despues del input, asi en cuanto el usuario digite el dato, este se convierte y ya despues se almacena en la variable

# letra = letra.lower() # Yo lo habia puesto de esta manera, donde estaba reasigando la variable

# Tambien explico porque esto --> letra.lower() que estaba haciendo no funciona. Esto es porqueel metodo lower() y upper() retornan una copia y que esta necesita ser almacenada, es por eso que necesitamos declarar o guardar el resultado de estos metodos en variables, de no ser asi es como si no estuvieramos haciendo nada, ya que la copia se queda vagando por ahi sin registro

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print(f"'{letra.upper()}' es una vocal")
else:
    print(f"'{letra.upper()}' NO es una vocal")