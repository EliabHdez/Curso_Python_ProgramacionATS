# Las instucciones continue, pass y else se pueden utilizar tanto con los bucles for como con los while

""" 
    - continue --> Salta a la siguiente iteracion del bucle. Supongamos que hay un bucle con 10 repeticiones y en la quinta esta la instruccion continue, lo que hace es saltar, brincar o ignorar esa quinta vuelta y brinca a la sexta 
    
    - pass --> Devuelve null en cuanto se le en el interior del bucle. El bucle devolveria null, es como si no ejecutara el bucle. Esta instruccion se utiliza en casos muy especificos
    
    - else --> Tiene la misma funcion y el mismo proposito que el else en el condicional if, es decir, si la condicion previa al else no se cumple, se ejecutara el else """
    
# Lo que estamos viendo a continuacion es que gracias a la instruccion continue, no se esta imprimiendo la h y esto se debe no a que este ignorando a la h, si no que el continue lo que hace es ignorar el codigo que se tendria que ejecutar que se encuentre despues del continue, en este caso el print, se lo brinca y vuelve a ejecutar el bucle de forma normal
    
for i in 'Python':
    if i == 'h':
        continue
    print(i)
    
# Un ejemplo del para que nos pueda servir el continue es para que si queremos contar las letras de un string podamos ignorar los espacios en blanco para NO contar los caracteres si no las letras del string

nombre = 'Curso Pildoras Informaticas'
contador = 0

for i in nombre:
    if i == ' ':
        continue
    contador += 1
    
print(contador) # El string almacenado en la variable nombre tiene 27 caracteres y 25 letras, con el codigo anterior podemos confirmar que ignoramos los espacios en blanco y solo contabilizamos el numero de letras en el string

# La instruccion pass se utiliza en casos muy concretos que por el momento no hay algun ejemplo practico donde ocuparlo, pero se puede ocupar en funciones o clases para dejarla como nula por si se requiere o se va a implementar despues

class miClase:
    pass # Para programar mas adelante

def miFuncion():
    pass # Para programar mas adelante

# La instruccion pass no se suele utilizar mucho ni es muy comun verla debido a su objetivo, su funcionamiento y lo que conseguimos con esta

# La instruccion else dentro de un bucle for o while cambia un poco en cuestion de como funciona en comparacion con un condicional. Y este cambio es que mientras el else pertenece a un condicional, este se ejecuta cuando la condicion del condicional no se cumple, mientras que en los bucles, se va a ejecutar en el momento en que el bucle termina de hacer su ejecucion o recorrido por completo, si este no termina y por alguna razon se queda a medias el else no se ejecutara en ningun momento

email = input('Introduce tu email: ')

for i in email:
    if i == '@':
        arroba = True
        break
else:
    arroba = False
    
print(arroba)