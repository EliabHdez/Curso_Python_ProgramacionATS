# Operadores Aritméticos

# Con los operadores aritméticos podemos hacer operaciones matematicas con numeros directamente o con variables

# Los operadores aritmeticos siguen las mismas reglas de prioridad que tenemos en las matematicas (PEMDAS)

# Suma (+)

resultado = 10 + 5

print(resultado)

num1 = 25
num2 = 15

resultado2 = num1 + num2

print(resultado2)

print("*********")

# Resta (-)

resultado2 = num1 - num2

print(resultado2)

print("*********")

# Multiplicacion (*)

resultado2 = num1 * num2

print(resultado2)

print("*********")

# Division normal con decimal (/)

num1 = 10
num2 = 3

resultado2 = num1 / num2

print(resultado2)

# Division con numero entero redondeado a la baja (//)

resultado2 = num1 // num2

print(resultado2)

print("*********")

# Modulo (%) (Residuo de una division)

num1 = 12
num2 = 5

resultado2 = num1 % num2

print(resultado2)

print("*********")

# Exponenciacion (**)

num1 = 2
num2 = 5

resultado2 = num1 ** num2

print(resultado2)

print("*********")

# Operacion aritmetica compleja tomando en cuenta el PEMDAS

opArit = 3**3 * (13/5 - (2*4))

print(opArit)

# Como vemos en el resultado, Python tomo en cuenta las reglas de los signos (PEMDAS) para resolver la operacion anterior. Esto quiere decir que realizo primero las operaciones con parentesis, seguida de la exponenciacion y por ultimo la multiplicacion, dando el resultado final