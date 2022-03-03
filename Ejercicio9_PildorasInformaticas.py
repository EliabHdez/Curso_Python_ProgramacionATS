# Crea un programa que pida introducir una dirección de email por teclado. El programa debe imprimir en consola si la dirección de email es correcta o no en función de si esta tiene el símbolo ‘@’. Si tiene una ‘@’ la dirección será correcta. Si tiene más de una o ninguna ‘@’ la dirección será errónea. Si la ‘@’ está al comienzo de la dirección de email o al final, la dirección también será errónea

# la siguiente solucion al ejercicio es mi solucion, la cual abarca un poco mas que lo que se solicita en el ejercicio donde pide solo corroborar si el email tiene arroba o no y dependiendo de esto informar si el email es correcto o no. En mi solucion agregue la terminacion .com, .com.mx y .mx, ademas de que si el email es erroneo solicite volverlo a introducir

# email = input('Introduce tu correo electronico: ')
    
# while (email.startswith('@') == True or email.endswith('@') == True):
#     print('Email invalido. Error de sintaxis. Introduce un correo valido')
    
#     email = input('Introduce tu email: ')
    
# while (email.endswith('.com') == False and (email.endswith('.mx') == False)):
#     print('Direccion de correo electronico invalida. Favor de introducir un email valido')
    
#     email = input('Introduce tu email: ')
    
# while (email.count('@') != 1):
#     print('Email invalido. Introduce una direccion de email valida')
    
#     email = input('Introduce tu email: ')

# print(f'Tu direccion de correo electronico es: {email}')

# # A continuacion veremos la solucion dada al ejercicio por el profe Juan, en la cual se limita a solo hacer lo que dice el ejercicio, pero solo en parte ya que no esta evaluando si el arroba se encuentra al inicio o final del email

email_usuario = input('Introduce tu email: ')

arroba = email_usuario.count('@')

if arroba != 1 or email_usuario.rfind('@') == (len(email_usuario)) == -1 or email_usuario.find('@') == 0:
    print('Email incorrecto')
else:
    print('Email correcto')
    
# Me doy cuenta que la forma de resolver el ejercicio del profe Juan tiene una deficiencia o mas que deficiencia le falta evaluar si el arroba esta al final. Trato de entender que esto lo quizo lograr con el metodo rfind(), seguido del metodo len, sin embargo encontre un inconveniente con esto y no se si siempre ha sido asi o esto ya cambio desde que el profe hizo el curso al momento en que yo lo estoy tomando. Y este inconveniente es que el metodo rfind(), da como resultado el indice donde se encuentra la palabra, letra etc indicado dentro de los parentesis, pero que este metodo no cuenta como tal de atras para adelante o de derecha a izquierda como el en algun momento lo menciono, si no que mas bien, el indice que arroja como resultado es el correspondiente a la ultima palabra, letra etc que encuentra dentro de la cadena, es decir si cuenta de derecha a izquierda pero no el indice si no la palabra o letra que esta como parametro y esta es la que toma en cuenta para arrojar el indice como resultado. Ej 'hola cruel mundo mundo cruel'. Si utilizamos el rfind con esta cadena y pasamos como metodo el rfind y como parametro 'cruel' nos va a arojar el indice donde empieza la ultima palabra cruel que se encuentra dentro de esta cadena, es decir la ultima palabra de esta, pasaria lo mismo si como parametro ponemos mundo, indicara el indice donde comienza la ultima palabra que coincida con mundo que en el caso del ejemplo es la penultima palabra

# Para logra el objetivo del ejercicio simplificandolo a meramente lo que nos pide este quedaria de la siguiente manera. (Esta solucion la hice yo mismo)

email_usuario2 = input('Introduce tu correo electronico: ')

arroba = email_usuario2.count('@')

if arroba != 1 or email_usuario2.startswith('@') or email_usuario2.endswith('@'):
    print('Email incorrecto. Favor de verificarlo')

else:
    print('Email válido')