# Operadores Logicos

# Permite construir expresiones lógicas, se obtiene como resultado valores booleanos y se ponen en MINUSCULAS

# Para trabajar con los operadores logicos se requieren de dos operandos de tipo logicos/booleanos que van a ser los valores a comparar y de un operador el cual va a servir como comparador

""" Los Operadores Lógicos son:
        - And (Conjunción) --> and
        - Or (Disyunción) --> or
        - Negación --> not """
        
""" Prioridad de los Operadores Logicos --> Se evaluan en el siguiente orden
        1 - NOT
        2 - AND
        3 - OR """

# Operador AND

""" El operador AND se conoce como una multiplicacion logica donde true = 1 y false = 0 y sigue las mismas reglas matematicas donde cualquier numero multiplicado por 0 (1x0=0) el resultado es 0, por lo tanto:
         True and True = True
         True and False = False
         False and True = False
         False and False = False """

# Operador OR

""" El operador OR se conoce como una suma logica donde true = 1 y false = 0 y sigue las mismas reglas matematicas donde x numero + 0 es igual al valor de x numero (1+0=1) por lo tanto:
        True or True = True
        True or False = True
        False or True = True
        False or False = False """

# Operador Not

""" El operador NOT se conoce como negacion, por lo tanto el resultado es lo contrario u opuesto
        True = False (not True = False)
        False = True (not False = True) """

a = 10
b = 12
c = 13
d = 10

comparacion = ((a>b) or (a<c)) and ((a==c) or (a>=b)) # Resultado = False

print(comparacion)

# Prioridad de los operadores en General

""" La prioridad de los operadores en general es la siguiente:
        Se evaluaran en el siguiente orden, siendo el numero uno los primeros que se evaluan y asi consecutivamente
                
                1. ()
                2. ** (exponenciacion)
                3. *, /, mod, not
                4. +, -, and
                5. >, <, ==, >=, <=, !=, or """
                
print('***********')
                
a = 10
b = 15
c = 20

resultado = ((a<b) and (b<c))

print(resultado)

resultado = ((a>b) and (b<c))

print(resultado)

resultado = ((a<b) or (b<c))

print(resultado)

resultado = ((a<b) or (b>c))

print(resultado)

resultado = ((a>b) or (b>c))

print(resultado)

print('*****NOT******')

resultado = not True

print(resultado)

resultado = not False

print(resultado)

resultado = not ((a<b) and (b<c))

print(resultado)

resultado = not ((a>b) or (b>c))

print(resultado)