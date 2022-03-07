# Interfaces Graficas - GUI 1ra y 2da Parte - Pildoras Informaticas / Videos 42 y 43

from tkinter import *
from turtle import width

# El metodo mainloop tiene que estar siempre al final

raiz = Tk() # Llamamos o intancias la clase Tk() de la libreria Tkinter

raiz.title('Ventana de pruebas') # Ponemos titulo a la ventana

# raiz.resizable(True,1) # Nos permite decidir si queremos que la ventana se pueda redimensionar. Este metodo acepta valores booleanos, ya sea que pongamos 1 o 0 o bien True o False. El 1 equivale a True y 0 a False. El primer valor corresponde a width (ancho) y el segundo a height (alto)

raiz.iconbitmap("Graphical User Interfaces/kali.ico") # Asignar un icono a la ventana. Este icono debe estar en formato .ico

raiz.geometry('650x350') # Damos una medida a la ventana

raiz.config(bg='white') # Le asignamos un color de fondo a la ventana

raiz.config(relief='sunken')

raiz.config(bd='30')

raiz.config(cursor='pirate')

miFrame = Frame() # Este frame hay que meterlo dentro de la raiz. Para esto usamos el metodo pack

miFrame.pack(side='left', anchor='n') # Empaquetamos el frame dentro de la raiz. Esta dentro de la raiz. El metodo pack tambien nos sirve para definir donde queremos que este anclado el frame dentro de la raiz y esto lo hacemos con el parametro side dandole como valor una direccion (right, left, top, bottom). Si queremos utilizar dos direcciones para que quede por ejemplo a la izquierda y arriba debemos utilizar otro parametro el cual es anchor y este recibe como valor una cordenada de brujula, es decir norte, sur, este u oeste, pero en ingles y solo la inicial, es decir n=north, s=south, e=east, w=west

# Tambien existe otro parametro para el metodo pack que es el parametro fill, que lo que hace es rellenar para que el frame se expanda junto con la raiz pero que abarque por completo este ultimo, sin embargo este parametro tiene un particularidad y es que para el valor x (horizontal), si funciona solo pasando ese valor, pero para el valor y (vertical) no funciona por si solo, para este tenemos que pasar un paramtro adicional el cual es expand con el valor de true, al igual que si queremos que sea para ambos sentidos ocupamos el parametro fill con el valor both y el parametro expand con el valor true

miFrame.pack(fill='y', expand=True)

miFrame.config(bg='red') # Si ejecutamos el programa en este punto aunque ya creamos el frame, lo pusimos dentro de la raiz y le dimos un color veremos que al parecer no ha pasado nada y esto se debe a que al frame hay que darle un tamaño y hasta no asignarle un tamaño no podremos visualizarlo. Adicional a esto hay que desabilitar el metodo geometry de la raiz ya que la raiz siempre se va a adaptar al tamaño del fram, es por eso que le debemos asignar un tamaño al frame y no a la raiz

miFrame.config(width='650', height='350') # Asignamos un tamaño al frame. El frame tiene siempre el mismo tamaño, es fijo, este no se adapta si redimensionamos la raiz

miFrame.config(relief='groove') # Con esto asignamos un tipo de borde. Sin embargo con este parametro podriamos ver que no pasa nada y esto se debe a que debemos asignar un grosor de borde

miFrame.config(bd='15') # Asinamos el tamaño o grosor del borde

miFrame.config(cursor='hand2') # Cambiamos el tipo de cursor al momento en que este se posiciona sobre el frame

raiz.mainloop() # Este metodo lo que hace es mantener la ventana en un bucle infinito para que se este ejecutando y a la espera y escucha de eventos. Esto lo hacen todas las ventanas de todos los programas, lo cual nos permite a los usuarios interactuar con ellas