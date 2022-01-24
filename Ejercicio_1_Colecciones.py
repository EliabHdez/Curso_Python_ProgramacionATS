# Ejercicio 1 - Eliminar duplicados de una lista

# Escribe un programa que contenga una lista y que, a continuación, elimine los elementos duplicados y por último mostrar la lista

print('***Lista***')

lista1 = [1,2,3,4,5,1,3,5,'Moises','Hernandez','Eliab','Hernandez']
print(lista1)

# No hay manera de detectar y eliminar elementos duplicados de forma directa en una lista, por lo tanto, lo que se tiene que hacer es convertir esta lista en una coleccion que no permita elementos duplicados como los conjuntos y ya que no haya elementos duplicados regresarla nuevamente a ser una lista

print('***Conjunto***')

conjunto = set(lista1) # 1
print(conjunto)

print('***Lista nuevamente***')

lista1 = list(conjunto) # 2
print(lista1)

# De esta manera estamos generando el codigo necesario para el cometido en dos lineas de codigo, sin embargo los podemos hacer de una forma mas directa y en una sola linea de codigo

print('***Forma 2***')

lista2 = [1,2,3,4,'Moises','Hernandez','Eliab','Hernandez',1,3,5]

lista2 = list(set(lista2)) # Esta seria la forma rapida y abreviada, donde lo hacemos todo mas compacto y de un solo tajo, en lugar de ir desglosando el proceso lo hacemos de forma mas directa

print(lista2)