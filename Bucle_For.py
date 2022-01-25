# Bucle For

# Al igual que el bucle While, el bucle For es un ciclo donde mientras se cumpla la condicion asignada este se ejecutara las veces que sea necesario, al momento de que se deje de cumplir la condicion, este se detendra y dejara de ejecutarse

# El Bucle For es un bucle con un numero determinado de iteraciones, ya que de antemano vamos a saber cuantas veces se va a repetir

# El bucle for trabaja en conjunto con colecciones, ya que son estas las que ocupara para recorrer y hacer las iteraciones o repeticiones. Este bucle esta conformado por un iterador o variable iteradora (i, o cualquier otro nombre, sin embargo normalmente se ocupa la letra i para este un iterador) seguido de la palabra in y posteriormente la coleccion a recorrer

for i in [1,'Moises',3,4,'Hernandez',True]:
    print('Hola Mundo')
    
# Y bueno que fue lo que hizo el bucle for en lo anterior? Lo que hizo fue que recorrio la lista elemento por elemento, y al momento de que el iterador (i) fue recorriendo elemento por elemento, por cada elemento que recorria imprimia el Hola Mundo, es por eso que decimos que en el bucle for sabemos cuantas iteraciones va a hacer

# La variable iteradora toma el valor de cada elemento que recorre

# La coleccion a recorrer se puede poner de forma directa o bien estar en una variable y ser esta variable la que se ponga en el bucle for

coleccion = [1,'Eliab',2,3,'Lopez',4]

for i in coleccion:
    print(f'Elemento del iterador {i}')
    
# El ciclo for funciona con cualquier tipo de coleccion, listas, tuplas e incluso diccionarios donde tenemos dos elementos por posicion, clave y valor. En este ultimo veremos que el comportamiento del bucle for trabaja un poco diferente

print('***Diccionarios***')

personas = {'Moises':31, 'Susett':29, 'Efrain':33}

for i in personas:
    print(f'Elemento del iterador {i}') # Aqui solo nos muestra la clave del diccionario
    
#  Si lo que queremos no es la clave si no los valores de las claves necesitamos tomar el diccionario y entre corchetes como parametros ponemos la clave, y esto al estar en un bucle for hay que recordar que la variable iteradora toma las claves, por lo tanto es el parametro que tenemos que poner entre los corchetes

for i in personas:
    print(personas[i]) # Con esto lo que conseguimos son los valores
    
# Pero que pasa si lo que queremos es tanto la clave como el valor pero desglosado por medio del bucle, pues tenemos que solicitar la clave por medio de la variable iteradora seguido del valor por medio del diccionario con la clave que en este caso es el iterador

for i in personas:
    print(f'{i} --> {personas[i]}')
    
# Para lo anterior hay otro metodo, el cual puede ser el mas visto, ademas de que es mas entendible y visualmente mejor. Este metodo es ocupar dos variables iteradoras, una para la clave y otra para el valor, para que al momento de llamar a cada elemento lo hagamos mediante su variable junto con el metodo intems() para el diccionario

print('***Forma 2, con dos variables iteradoras y metodo items()***')

for clave,valor in personas.items():
    print(f'{clave} --> {valor}') # Como podemos observar el resultado es el mismo que el anterior, sin embargo este es como mas directo, mas claro e incluso mas sencillo, ya que es mas entendible de alguna manera
    
# Con el bucle for tambien se pueden recorrer cadenas, esta la estara recorriendo elemento por elemento o letra por letra de la cadena

persona = 'Eliab'

for i in persona:
    print('Hola') # Esta imprimiendo el mensaje una vez por cada letra que contiene la cadena

for i in persona:
    print(i)
    
# Podemos modificar el print para que cuando recorramos una cadena por ejemplo, todas las letras nos salgan en una sola linea, de forma normal cada letra se imprime en una linea diferente, se imprimen con un salto de linea y esto es debido a que el print de forma predeterminada cada vez que se termina de ejecutar uno genera un salto de linea, pero eso lo podemos modificar

for i in persona:
    print(i, end='.') # Con el end= cambiamos este comportamiento cada vez que el print se ejecuta a cada vuelta del ciclo y podemos ponerle como parametro un espacio, un punto, un guion etc