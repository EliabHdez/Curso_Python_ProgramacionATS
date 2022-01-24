# Ejercicio 2

""" Escribe un programa que tenga dos listas y que, a continuación, cree las siguientes listas (en las que no debe haber repeticiones)

    - Lista de palabras que aparecen en las dos listas
    - Lista de palabras que aparecen en la primera lista, pero no en la segunda
    - Lista de palabras que aparecen en la segunda lista, pero no en la primera
    - Lista de palabras que aparecen en ambas listas """


famHdez = ['Moises', 'Nahun', 'Efrain', 'Lilia', 'Arnulfo', 'Susett', 'Brenda', 'Zully']
famNoDirecta = ['Susett', 'Brenda', 'Zully', 'Angelita']

print('*****Nombres en las dos listas*****')

lista1 = famHdez + famNoDirecta
print(lista1)

lista1 = list(set(lista1))
print(lista1)
print(len(lista1))

print('*****Nombres en la primera lista, que no estan en la segunda*****')

conjunto1 = set(famHdez)
conjunto2 = set(famNoDirecta)

lista2 = list(conjunto1 - conjunto2)
print(lista2)

print('*****Nombres en la segunda lista, que no estan en la primera*****')

conj1 = set(famHdez)
conj2 = set(famNoDirecta)

lista3 = list(conj2 - conj1)
print(lista3)

print('*****Nombres que aparecen en ambas listas*****')

conjA = set(famHdez)
conjB = set(famNoDirecta)

lista4 = list(conjA & conjB)
print(lista4)

""" Forma de resolver el ejercicio de Alejandro """

famMoy = ['Moises', 'Nahun', 'Efrain', 'Lilia', 'Arnulfo', 'Susett', 'Brenda', 'Zully']
famNoDir = ['Susett', 'Brenda', 'Zully', 'Angelita']

# Primero eliminio los elementos duplicados creando conjuntos

a = set(famMoy)
b = set(famNoDir)

# Seguido unio los conjuntos para formar la primera lista del ejercicio

# Lista 1
union = list(a | b)

# Lista 2
soloFamMoy = list(a - b)

# Lista 3
soloFamNoDir = b - a

# Lista 4
interseccion = list(a & b)

print('***Lista 1***')
print(union)
print('***Lista 2***')
print(soloFamMoy)
print('***Lista 3***')
print(soloFamNoDir)
print('***Lista 4***')
print(interseccion)