# Ejercicio 4

# Hacer un programa para ingresar el radio de un circulo y se reporte su area y la longitud de la circunferencia

""" area = pi * r2
    longitud = 2 * pi * r
"""
import math # Aqui estamos importando el modulo math que contiene el valor de pi, aunque ya sabemos cuanto vale pi y podriamos poner el dato de forma directa, los modulos nos sirven para este cometido y ya tiene los datos cargados en variables especificas y reservadas

# Para hacer uso del modulo math y del pi que viene en este, es necesario declarar el modulo seguido de la variable de este que queremos ocupar, ej math.pi

radio = float(input("Digite el radio del circulo -> "))

area = math.pi * (radio**2)
diametro = 2 * math.pi * radio

print(f"El area del circulo es: {area:.2f}")
print(f"El diametro del circulo es: {diametro:.4f}") # Que significa el 2 y el 4f en las variables??? Lo que estamos haciendo con esa parte de codigo es decirle a la variable cuanto numeros decimales queremos depues del punto. Si no especificamos por defecto al ser un numero flotante el resultado vendra con los 16 digitos que permiten los numeros flotantes despues del punto. Para evitar estohacemos uso de un metodo o forma para decirle a python cuanto numeros decimales queremos despues del punto en un numero flotante. Esto lo hacemos de la siguiente manera: despues de la variable agregamos dos puntos seguido de un punto normal y por ultimo el numero de decimales que queramos mas la letra f. Ej variable:.3f, lo cual hara que el resultado tenga 3 numero despues del punto decimal