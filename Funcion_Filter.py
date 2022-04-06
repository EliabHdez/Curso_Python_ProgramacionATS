# Funcion Filter

# La funcion filter forma parte de un grupo de funciones que se les denomina funciones de orden superior. Nos permiten utilizar un paradigma que se denomina programacion funcional

# La funcion filter verifica que los elementos de una secuencia cumplen una condicion devolviendo un iterador con los elementos que cumplen dicha condicion


def numeroPar(num):
    
    if num % 2 == 0:
        return True
    
numeros = {17, 24, 7, 39, 8, 51, 92}

print(list(filter(numeroPar, numeros)))

numero_par = lambda num: num % 2 == 0

print(list(filter(numero_par, numeros)))

# Podemos hacer la funcin lambda directamente en el print

print(list(filter(lambda num : num % 2 == 1, numeros))) # Al hacerlo mediante la funcion lambda estamos prescindiendo de la declaracion de la funcion como tal, ya que esta la podemos declarar de forma directa en el print

print('----- Salarios Empleados -----')

class Empleados:

    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

    def __str__(self):

        return f'Nombre: {self.nombre} - Puesto: {self.puesto} - Sueldo: {self.salario}'

lista_empleados = [
    Empleados('Moises Hernandez', 'Presidente', 60000),
    Empleados('Nahun Fernandez', 'Director', 55000),
    Empleados('Efrain Hernandez', 'Subdirector', 45000),
    Empleados('Sandra Arzate', 'Contadora', 30000),
    Empleados('Lilia Lopez', 'Jefa de Ventas', 20000),
    Empleados('Arnulfo Hernandez', 'Jefe de Repartos y Entregas', 20000)
]

salariosSocios = filter(lambda empleado: empleado.salario > 50000, lista_empleados)

for mayoresSalarios in salariosSocios:
    print(mayoresSalarios)