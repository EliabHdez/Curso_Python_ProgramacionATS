# Paquetes distribuibles --> Los paquetes distribuibles son aquelos modulos que nosotros vamos a poder compartir mediante correo electronico o bien subiendolos a una plataforma que permita distribuir estos paquetes

# Esto nos permite crear nuestros propios modulos o scripts, empaquetarlos y enviarlos a donde o a quien queramos

""" Para hacer uso de paquetes distribuibles, es necesario dos pasos

    - Crear el paquete
        Una vez creado el paquete y que este haya sido distribuido, haya donde se haya distribuido...
        
    - Instalar el paquete """
    
""" Pasos para la creacion de un paquete distribuible
    
    - Crear un archivo en la carpeta raiz con el nombre de 'setup.py'. Con respecto a la carpeta raiz supongo que habla en el caso del video, en la ruta donde el profe esta trabajando, pero este se puede crear en cualquier sitio
        
        Este archivo llamado setup va a contener una descripcion del paquete que vamos a distribuir. Descripcion que va contener nombre del paquete, version, autor etc...
        
    - Crear el archivo distribuible --> Irnos en la consola a la ruta/directorio donde se encuentra el archivo setup.py. Ya estando en la ruta lo que sigue es escribir 'python setup.py (nombre del archivo) sdist' para crear un paquete distribuible. Si todo a ido bien y lo hemos echo correctamente nos tiene que crear en la carpeta raiz dos carpetas, una que diga nombrePaquete.egg-info para este ej en particular y otra que diga dist que es la importante que es la carpeta de distribucion y esta debe de contener un paquete comprimido en formato .tar.gz. Este ultimo es el archivo distribuible, el que deberiamos de enviar por correo o subirlo a alguna plataforma de nube en la red para asi poder distribuirlo 
    
    - Instalar el paquete --> Para instalar el paquete debemos en la consola ir a la ruta o directorio dist que es donde se encuentra el archivo empaquetado y a continuacion poner el siguiente comando 'pip3 install nombrePaquete' 
    
    Que conseguimos con esto? Al instalar paquetes conseguimos que cualquier archivo con extension de python pueda hacer uso del modulo y de su contenido este donde este el archivo de python. El instalar paquetes es algo asi como instalar un programa en la pc, el cual vas a poder ocupar libremente, y esto es lo que sucede cuando importamos el modulo math de python, este modulo fue creado como un paquete distribuible y al momento de instalar python se instala este paquete para que cuando nosotros creemos nuestro codigo de nuestras aplicaciones o programas en python, lo hagamos donde lo hagamos en la ruta que lo hagamos este modulo math este disponible para su uso """
    
# Vamos a hacer una prueba de esto creando un archivo nuevo el cual hara uso de un modulo que no este instalado y posteriormente lo moveremos dentro de la carpeta Anotaciones y comentarios para verificar que el mismo modulo no sera posible ocuparlo ya que no lo encuentra y por lo tanto a la hora de ejecutar nos da error. Posterior a esto haremos lo mismo pero con otro archivo nuevo y utilizando el paquete que contiene los modulos instalados para que veamos que con este archivo nos permite hacer uso de los modulos tengamos el archivo donde lo tengamos aunque este lo estemos moviendo de ubicacion y su ruta cambie

""" Desinstalacion de un paquete
    
    Para desinstalar un paquete lo unico que tenemos que hacer es abrir la consola o cmd (como administrador) y utilizar el siguiente comando 'pip3 unistall <nombre del archivo>'. Para la desinstalacion no es necesario irnos hasta la ruta donde se encuentra el archivo ni a ninguna otra ruta en especifico, da igual, lo podemos hacer desde cualquier ruta. Yo no lo voy a hacer hasta posiblemente despues para tener disponible la diferencia entre el archivo que utiliza el paquete instalado y el que ocupa uno NO instalado """
    
# NOTA IMPORTANTE: PROCURAR PONERLE NOMBRES FACILES DE RECORDAR A LOS PAQUETES DISTRIBUIBLES, YA QUE AL MOMENTO DE DESINSTALARLOS NECESITAREMOS HACER USO DE ESTE NOMBRE Y SI NO NOS ACORDAMOS DEL NOMBRE NO PODREMOS DESINSTALARLO Y PODRIA SER BASTANTE FRUSTANTE ESTAR TRATANDO DE ACORDARNOS DEL NOMBRE QUE LE PUSIMOS

# Nombre del paquete creado para el ejercicio 'Paquete Calculos - Potencia y Porcentaje'