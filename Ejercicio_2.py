# Determinar la solución lógica de la siguiente operación (Imagen de referencia de la operacion en la carpeta referencias)

a = float(input("Digite el valor de a: "))
b = float(input("Digite el valor de b: "))

resultado = ((3+5*8)<3 and ((-6/3*4)+2<2)) or (a>b) # Solucion propia

print(f"El resultado es: {resultado}")

resultado = ((3+5*8)<3 and (-6/3*4)+2<2) or (a>b) # Solucion Alejandro. No puso un par de parentesis, pero al parecer no afectan al resultado, ya que eventualmente se estaran eliminando al ser parentesis internos y ser de los primeros en resolverse. De todos modos, podemos hacer un ejercicio despues similar para saber con mas certeza si afecta o no al resultado