# Colas (con listas)

# Las colas son una estructuras que funcionan bajo el concepto 'fifo', por su siglas en ingles 'first input, first output' --> 'el primero en entrar, el primero en salir'

# Para crear colas en Python se puede importar el modulo collections con el deque, sin embargo se pueden simular colas con listas de la misma forma que con las pilas, al igual que las pilas los elementos que se agreguen iran al final pero con la diferencia de que en las colas al sacar elementos, el primero en salir tiene que ser el primer elemento de la cola

# from collections import deque # Este es el modulo a importar para la creacion de colas

filaBanco = ['Moises', 'Nahun', 'Efrain', 'Arnulfo']

print(filaBanco)

# Agregando elementos al final de la cola
filaBanco.append('Lilia')
filaBanco.append('Susett')

print(filaBanco)

# Sacando elemento de la cola por el principio

# De igual manera para sacar elementos utilizamos el metodo pop(), pero a este le pasamos el indice del elemento que queremos sacar, al ser una cola siempre tiene que ser el primer elemento de esta, por lo tanto el indice que pasemos como parametro del metodo pop(), siempre tendra que ser el indice 0

firstPerson = filaBanco.pop(0)
print(f'Atendiendo a {firstPerson}')
print(filaBanco)

firstPerson = filaBanco.pop(0)
print(f'Atendiendo a {firstPerson}')
print(filaBanco)