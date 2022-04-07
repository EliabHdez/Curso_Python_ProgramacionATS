# Funcion Map

# La funcion map aplica una funcion a cada elemento de una lista iterable (listas, tuplas, etc...) devolviendo una lista con los resultados

class Empleado():
    
    def __init__(self, nombre, puesto, sueldo):
        self.nombre = nombre
        self.puesto = puesto
        self.sueldo = sueldo
        
    def __str__(self):
        return f'Nombre: {self.nombre} / Puesto: {self.puesto} / Sueldo: {self.sueldo}'
    
lista_empleados = [
    Empleado('Moises', 'Jefe de Logistica', 15000),
    Empleado('Efrain', 'Jefe de Mercadotecnia', 15000),
    Empleado('Nahun', 'Jefe de Proyectos', 15000),
    Empleado('Lilia', 'Jefa de Ventas', 8000),
    Empleado('Arnulfo', 'Jefe de Envios y Repartos', 8000)
]

lista_empleados2 = [
    Empleado('Moises', 'Jefe de Logistica', 15000),
    Empleado('Efrain', 'Jefe de Mercadotecnia', 15000),
    Empleado('Nahun', 'Jefe de Proyectos', 15000),
    Empleado('Arnulfo', 'Jefe de envios y repartos', 8000),
    Empleado('Lilia', 'Jefa de Ventas', 8000)
]

def comision(empleado):
    empleado.sueldo = empleado.sueldo * 1.05
    
    return empleado

# En la funcion map el primer parametro que se pone es una funcion (la funcion que queremos que se ejecute con ese map)

lista_comisionEmpleados = map(comision, lista_empleados)

for empleado in lista_comisionEmpleados:
    print(empleado)
    
# Con la funcion map se pueden hacer muchas mas cosas y cosas mas complejas en comparacion con la funcion filter, ya que la  funcion map si bien no se le pone como tal funciones dentro de esta si trabaja con funciones ya creadas y estas solo se le pasan a la funcion map

# En el siguiente caso vamos a hacer mediante la funcion map que solo empleados con sueldos abajo de los 10000 tengan el beneficio de la comision

print()
print('----- Comision a salarios por debajo de 10,000 -----')

def comisionSalariosBajos(empleado):
    if empleado.sueldo <= 10000:
        empleado.sueldo = empleado.sueldo * 1.03
    return empleado

comision_sueldosBajos = map(comisionSalariosBajos, lista_empleados2)

# print(comision_sueldosBajos) Si solo dejo este print veremos que nos arroja como resultaodp un objeto de tipo map, tal vez de primeras pensemos que esto es un error o algo por el estilo por la forma en que lo presenta y sobre todo por lo ultimo que aparece en el print que parece no tener sentido, pero en realidad el codigo se esta ejecutando correctamente, solo que no arroja la lista que guarda, para esto tenemos que hacer que la imprima, de lo contario solo nos estaria imprimiend el tipo de objeto que en este caso en un objeto de tipo map, esto mismo pasa con la funcion filter

for empleado in comision_sueldosBajos:
    print(empleado)