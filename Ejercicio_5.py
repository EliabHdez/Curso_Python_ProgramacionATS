# Ejercicio 5

# Una tienda ofrece un descuento de 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.

# porcDescuento = 15
compra = float(input("Monto de la compra: $"))
descuento = (compra * 0.15) # Esta es la forma rapida de sacar el valor del porcentaje

""" Otra forma de hacerlo, requiere de un paso adicional y esta es la que normalmente se enseña. Basicamente es cantidad * porcentaje / 100
    (compra * 15) / 100 -> Como podemos observar con el metodo anterior no estamos ahorrando la division entre 100, ya que al hacer la multiplicacion por .15 (porcentaje descuento) nos da el resultado de una forma mas directa
"""

TotalPagar = compra - descuento

print(f"El monto total de la compra es de: ${TotalPagar:.2f}")