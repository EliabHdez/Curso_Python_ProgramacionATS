# Funciones Lambda

# Las funciones lambda son funciones anonimas y sirven para abreviar la sintaxis y que el codigo sea mas ligero y menor

# Todo lo que podemos hacer con una funcion lambda se puede hacer con una funcion normal, pero NO al reves, no todo lo que se puede hacer con una funcion normal, lo podemos hacer con una funcion lambda

# Las funciones lambda no pueden contener bucles, condicionales etc...

# Se les conoce como funciones anonimas ya que no tienen nombre alguno, se generan o guardan mediante una variable, pero la funcion como tal no tiene un nombre. Si nos fijamos en los ejemplos siguientes del archivo, la funcion normal tiene un nombre 'areaTriangulo', mientras que la funcion lambda no tiene nombre, esta almacenada en una variable y el nombre corresponde a la variable, pero la funcion como tal no tiene uno

# Tambien podemos encotrar estas funciones como 'on the go', 'on demand' y/o 'online'. Son terminos con los que tambien se les conoce a las funciones lambda

# --------- Funcion normal ---------

print('------Funcione normal------')

def areaTriangulo(base, altura):
    
    return (base*altura)/2

print(areaTriangulo(5,7))

triangulo_uno = areaTriangulo(5,7)

triangulo_dos = areaTriangulo(9,6)

print(triangulo_uno)
print(triangulo_dos)

# --------- Funcion Lambda ---------

# En las funciones lambda los dos puntos es el equivalente al return de una funcion normal

print('------Funcion Lambda 1------')

area_triandulo_lambda = lambda base, altura: (base * altura) / 2

print(area_triandulo_lambda(12,35))
print(area_triandulo_lambda(3,8))

area_triangulo_uno = area_triandulo_lambda(2,4)
area_triangulo_dos = area_triandulo_lambda(17,25)

print(area_triangulo_uno)
print(area_triangulo_dos)

print('------Funcion Lambda 2------')

al_cubo = lambda numero: pow(numero, 3)

al_cubo_dos = lambda numero: numero ** 3

print(al_cubo(3))
print(al_cubo_dos(5))

print('------Funcion Lambda 3------')

destacar_comision = lambda comision: f"!$ {comision}¡ de comisión"

comision_Ana_valorString = '12,384'
comision_Ana_valorNumerico = '6,823'

print(destacar_comision(comision_Ana_valorString))
print(destacar_comision(comision_Ana_valorNumerico))