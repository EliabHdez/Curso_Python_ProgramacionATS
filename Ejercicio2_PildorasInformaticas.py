# Ejercicio 2 - Pildoras Informaticas

# Crea un programa que pida por teclado Nombre, Direccion y telefono. Esos tres datos deberán ser almacenados en una lista y mostrar en consola el mensaje: 'Los datos personales son: nombre, apellido, telefono' (Se mostraran los datos introducidos)

nombre = input('Escribe tu nombre --> ')
direccion = input('Escribe tu dirección completa --> ')
telefono = input('Escribe tu número telefónico --> ')

lista = list()
lista.append(nombre)
lista.append(direccion)
lista.append(telefono)

print(f'Los datos personales son: Nombre: {lista[0]}, Direccion: {lista[1]}, Teléfono: {lista[2]}')

print('***Solucion Profe***')

# Solucion profe

Nombre = input('Introduce el nombre: ')
Direccion = input('Introduce la direccion: ')
Tfno = input('Introduce el teléfono: ')

listaDatos = [Nombre, Direccion, Tfno]

print('Los datos personales son: Nombre: ' + listaDatos[0] + ' Dirección: ' + listaDatos[1] + ' Teléfono: ' + listaDatos[2])