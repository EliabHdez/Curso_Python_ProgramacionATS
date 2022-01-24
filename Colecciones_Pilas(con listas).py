# Pilas

# Las pilas son estructuras de datos conocida como lifo. En Python no hay una manera de trabajar con pilas de forma directa como tal, no se pueden crear pilas asi como se crean listas, tuplas o diccionarios, sin embargo se pueden simular de una manera muy sencilla con listas

# A las pilas tambien se les conoce como lifo por sus siglas en ingles que significan 'last input, first output' --> 'ultimo en entrar, primero en salir', es el concepto con el que se le conoce a la forma en que trabajan las pilas

pila = [1,2,3]

# Tanto para agregar como para sacar elementos de una pila creada a partir de una lista se hace mediante le concepto lifo, esto quiere decir que al agregar tenemos que agregar el elemento nuevo al final y para eliminar el primer elemento a eliminar tiene que ser el ultimo elemento de la lista, el agregado al ultimo

# Agregando elementos al final

pila.append(4)
pila.append(5)
pila.append(6)
pila.append(7)

print(pila)

# Sacando elementos del final

pila.pop()
print(pila)

pila.pop()
print(pila)

# Hay que saber que el metodo pop() aparte de sacar el elemento, tambien lo retorna para que se pueda trabajar con el. Normalmente cuando se saca un elemento de una pila es para y porque se va a trabajar con el de alguna u otra manera, por lo tanto esta disponible este elemento al momento de sacarlo con el metodo pop()

eleRet = pila.pop()
print(f'Elemento retirado de la pila --> {eleRet}')

eleRet = pila.pop()
print(f'Elemento retirado de la pila --> {eleRet}')

print(pila)