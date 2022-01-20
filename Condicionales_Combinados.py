# Condicionales Combinados y Anidados

# Los condicionales pueden trabajar en conjunto con otros condicionales ademas de que pueden tener otros condicionales dentro, a estos se les conocen como condicionales anidados

edad = int(input("Digite su edad: "))

if edad >= 18:
	print("Es mayor de edad")
else:
	print("NO es mayor de edad")

# Pero que pasa si el usuario nos pasa un valor negativo? Pues como no se esta cumpliendo la primera condicion no arojaria que es menor de edad, pero no es posible que una edad se un numero negativo, por lo tanto tendriamos que usar condicionales anidados (un condicional dentro de otro condicional)

# Tambien queremos que si el usuario nos pasa un numero bastante alto, que si bien es valido, no seria creible como para una edad, ej 150 o 200, ya no hay persona que tenga esa edad, asi que necesitamos marcar un limite. Para esto hay 2 maneras. La primera es con los Operadores Logicos y la segunda con los Operadores Relacionales, esta segunda es la mas rapida y practica forma de hacerlo. Veamos ambas maneras

# La siguiente forma es una manera de combinar condicionales utilizando operadores logicos

edad2 = int(input("Digite su edad: "))

if edad2 > 0 and edad2 < 100:
	print('Edad correcta')
	if edad2 >= 18:
		print('Es mayor de edad')
	else:
		print('NO es mayor de edad')
elif edad2 == 0:
    print('El numero 0 no es valido')
else:
	print('El valor ingresado no es valido')

# La siguiente forma es una manera de combinar condicionales utilizando operadores relacionales combinado. Ademas de ser la forma mas practica y rapida. En esta forma lo que estamos haciendo es una comparacion de valores de forma consecutiva. En teoria es lo mismo que el ejemplo anterior, solo que este es mas practico y directo

edad3 = int(input('Digite la edad del sujeto #3: '))

if 0 < edad3 < 100:
    print('Edad valida')
    if edad3 >= 18:
        print('El sujeto #3 es mayor de edad')
    else:
        print('El sujeto #3 NO es mayor de edad')
elif edad3 == 0:
    print('El numero "0" no es válido')
elif edad3 < 0:
    print('Error: Edad incorrecta')
else:
    print('El dato ingresado no es válido')
    
# En python no existen los condicionales multiples, tambien conocidos como switch (tal es el caso como en JavaScript), podemos llegar al mismo resultado pero de diferente manera, por medio de otra ruta