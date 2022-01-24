# Ejercicio 3

""" Escribe un programa donde cree una lista con los siguientes personajes del Señor de los Anillos

    Nombre: Aragorn
    Clase: Guerrero
    Raza: Dúnadan del Norte
    
    Nombre: Gandalf
    Clase: Mago
    Raza: Istar
    
    Nombre: Legolas
    Clase: Arquero
    Raza: Elfo Sindar """
    
personajes = [{'Aragorn':{'Nombre':'Aragorn', 'Clase':'Guerrero', 'Raza':'Dúnadan del Norte'},'Gandalf':{'Nombre':'Gandalf', 'Clase':'Mago', 'Raza':'Istar'}, 'Legolas':{'Nombre':'Legolas', 'Clase':'Arquero', 'Raza':'Elfo Sindar'}}]

print(personajes)
print(type(personajes))

# Forma de resolverlo de Alejandro

personajes1 = []

p = {'Nombre':'Aragorn', 'Clase':'Guerrero', 'Raza':'Dúnadan del Norte'}
personajes1.append(p)

p = {'Nombre':'Gandalf', 'Clase':'Mago', 'Raza':'Istar'}
personajes1.append(p)

p = {'Nombre':'Legolas', 'Clase':'Arquero', 'Raza':'Elfo Sindar'}
personajes1.append(p)

print(personajes1)

# La diferencia entre como lo hice yo a como lo hizo Alejandro fue que yo lo hice de forma mas directa, creando la lista y dentro de esta el diccionario con los personajes, mientras que Alejandro creo la lista vacia, posteriormente fue creando personaje por personaje en forma de diccionario y agregandolo a la lista vacia que previamente habia creado. En su metodo solo ocupa una variable para la creacion de los 3 personajes, debido a que conforme los iba creando los iba agregando a la lista por lo tanto cuando el valor de la variable con el siguiente personaje, no se veia afectado el personaje creado con anterioridad debido a que ya estaba almacena como un elemento de la lista