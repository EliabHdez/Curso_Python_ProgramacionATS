# Interfaces Graficas - Pildoras Informaticas / Video 45

# Widget Entry --> Cuadro de texto (Introducir texto)

# Clases... Todas las clases que declaremos para crear widgets en la interfaz grafica deben de llevar dentro de los parentesis como parametro cual va a ser su contenedor padre y el los parametros adicionales que le queramos dar

# Entry() --> Creamos un cuadro de texto con el cual el usuario puede interactuar escribiendo en el

# Text() --> Creamos un cuadro de texto amplio, al igual que el entry el usuario puede escribir en este widget pero de forma mas amplia y extensa ya que este widget esta pensado y diseñado para muchos mas caracteres. De forma predeterminada este se crea muy grande, pero podemos darle un tamaño en especifico con width y height

# Scrollbar() --> Creamos una barra de desplazamiento para cuando haya mucho texto podamos hacer scroll y deplazarnos por todo el texto, esta barra se crea de forma independiente al Text por lo tanto hay que asignarle un espacio en la grilla (grid) al igual que como cualquier otro widget, ademas de eso de forma predeterminada aparece muy pequeña y su compotamiento no es el mejor, asi como la barra con la que nos podemos desplazar sin la necesidad de las flechas no viene por defecto activada, asi que nosotros debemos activarla, esta y varias configuraciones adicionales se le tiene que dar para que tenga un aspecto como se les ve mas comunmente, asi como indicarle la direccion en la que se va a desplazar. Es importante tener en cuenta que el objeto Scrollbar() debemos declarar a donde va a pertenecer como el frame o la raiz y tambien que es lo que va a controlar por decirlo de alguna manera, este ultimo lo hacemos con el parametro command y dentro de este definimos el cuadro de texto (Text) a controlar. Sin embargo para activar la barra de desplazamiento es necesario hacer una configuracion no en el Scrollbar si no en el Text que va a manejar esta barra de desplazamiento y lo hacemos con el parametro yscrollcommand seguido del Text en cuestion seguido del parametro set utilizando la nomenclatura del punto, esta declaracion del codigo debe de ir despues de el codigo donde definamos la scrollbar, de lo contrario nos arrojara un error, Ej: yscrollcommand=barraDesp.set. Ej2: linea de codigo 68

# Buttom() --> Creamos un boton con el cual el usuario puede interactuar y con el que podemos ejecutar alguna accion en la interfaz grafica

# Veremos dos metodos los cuales son grid y sticky

# Grid es como en CSS, nos permite acomodar elementos dentro de una grilla ficticia la cual estara definida en el metodo, este metodo a diferencia de css donde se define la grilla de forma general en toda pagina y despues vamos acomodando los elementos aqui en python se estipula directamente sin crear como tal una grilla antes, esta se va creando conforme vamos agregando y acomodando los elementos, es decir no estamos diviendo la interfaz grafica de manera anticipada con una grilla con filas y columnas determinadas. Tanto las filas como las columnas empiezan a contar desde 0

# Sticky nos permite ubicar el contenido en cualquier punto dentro de los puntos cardinales de una brujula, norte, sur, este, oeste y tambien noreste, sureste, noroeste y suroeste, estos estan definidos en ingles y para definirlos solo ocupamos las iniciales... n, s, e, w, ne, se, nw y sw 

# pady y padx nos permiten definir paddings como en css para darle un espaciado entre el contenido que tiene definido el padding de su contenedor padre (raiz, frame etc...). Con pady controlamos el padding de superior e inferior y con el padx controlamos el padding de la derecha e izquierda

from tkinter import *

root = Tk()

root.title('Velkan')

frame1 = Frame(root, width=400, height=300)

frame1.pack()

nombreUsuario = StringVar() # Con el stringvar le indicamos a la variable que su contenido o valor seran una serie de caracteres. Esta variable y su valor la tenemos que asociar al entry nombre para que al pulsar el boton imprima en este cuadro el valor de esta variable que sera un nombre. Y como asociamos esta variable al Entry(? Esto lo hacemos directamente en el Entry con el valor de textvariable

contacto = StringVar()

nombreLabel = Label(frame1, text='Nombre')
nombreLabel.grid(row=0, column=0, sticky='w', pady=10, padx=10)

apellidoLabel = Label(frame1, text='Apellido')
apellidoLabel.grid(row=1, column=0, sticky='w', pady=10, padx=10)

emailLabel = Label(frame1, text='Email')
emailLabel.grid(row=2, column=0, sticky='w', pady=10, padx=10)

passLabel = Label(frame1, text='Password')
passLabel.grid(row=3, column=0, sticky='w', pady=10, padx=10)

comentarioLabel = Label(frame1, text='Comentarios')
comentarioLabel.grid(row=4, column=0, sticky='w', pady=10, padx=10)

contactoLabel = Label(frame1, text='Datos de Contacto')
contactoLabel.grid(row=5, column=0, padx=10, pady=10)

contactoCuadroMensaje = Label(frame1, textvariable=contacto)
contactoCuadroMensaje.grid(row=5, column=1, padx=10, pady=10)

nombreCuadro = Entry(frame1, textvariable=nombreUsuario)
nombreCuadro.grid(row=0, column=1, pady=10, padx=10)
nombreCuadro.config(justify='center')

apellidoCuadro = Entry(frame1)
apellidoCuadro.grid(row=1, column=1, pady=10, padx=10)
apellidoCuadro.config(justify='center')

emailCuadro = Entry(frame1)
emailCuadro.grid(row=2, column=1, pady=10, padx=10)
emailCuadro.config(justify='center')

passCuadro = Entry(frame1)
passCuadro.grid(row=3, column=1, pady=10, padx=10)
passCuadro.config(fg='red', show='*', justify='center')

comentarioCuadro = Text(frame1, width=18, height=6)
comentarioCuadro.grid(row=4, column=1, pady=10, padx=10)

barraDesp = Scrollbar(frame1, command=comentarioCuadro.yview)
barraDesp.grid(row=4, column=3, sticky='ns', pady=10)

comentarioCuadro.config(yscrollcommand=barraDesp.set)

def codigoBoton():
    nombreUsuario.set('Moises')
    
def mensajeContacto():
    contacto.set('Si lo prefieres puedes ponerte en contacto con nostros por telefono o via email \nTelefonos: 55-5555-5555\n                55-6666-6666\nEmail: contacto.soporte@miemail.com')

botonEnviarDatos = Button(root, text='Enviar', command=codigoBoton)
botonEnviarDatos.pack()

botonContacto = Button(root, text='Contactanos', pady=7, command=mensajeContacto)
botonContacto.pack()

# cuadroNombre.place(x=5, y=5)

root.mainloop()