# Ejercicio 5 Bucle for - Pildoras Informaticas

# Crea un programa que pida por teclado introducir una contraseña. La contraseña no podrá tener menos de 8 caracteres ni espacios en blanco. Si la contraseña es correcta, el programa imprime 'Contraseña OK'. En caso contrario imprime 'Contraseña incorrecta'


password = input('Introduce una contraseña: ')
contador = 0

for i in password:
    if i == ' ':
        contador = 1
        
if len(password) >= 8 and contador == 0:
    print('Contraseña OK')
else:
    print('Contraseña incorrecta')
    
print('Forma de solucion del profe con for in range')
    
for i in range(len(password)):
    if password[i] == ' ':
        contador = 1
        
if len(password) >= 8 and contador == 0:
    print('Contraseña OK')
else:
    print('Contraseña incorrecta')
    
# Cabe mencionar que no pude solucionarlo solo, la primera solucion la saque de la solucion del profe pero quite el range haber si seguia sirviendo con el for normal