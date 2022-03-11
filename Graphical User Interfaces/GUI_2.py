# Interfaces Graficas - GUI 1ra y 2da Parte - Pildoras Informaticas / Video 44

# Widget Label --> Nos permiten mostrar texto o imagenes. Tienen como unica finalidad mostrar texto, no se puede interactuar con el

""" Sintaxis del label
    
    - variableLabel = Label(contenedor, opciones)
    
    Opciones para los label (unas de las mas utilizadas) 
    
    - text --> Texto que se muestra en el label
    - anchor --> Controla la posicion del texto si hay espacio suficiente para el (center por defecto)
    - bg --> Color de fondo
    - bitmap --> Mapa de bits que se mostrara como grafico
    - bd --> Grosor del borde (2px por defecto)
    - font --> Tipo de fuente a mostrar
    - fg --> Color de la fuente
    - width --> Ancho del label en caracteres (no en pixeles)
    - height --> Altura del label en caracteres (no en pixeles)
    - image --> Muestra imagen en el label en lugar de texto
    - justify --> Justificacion del texto del label """
    
from tkinter import *

root = Tk()

root.title('GUI 2')

# root.iconbitmap('Graphical User Interfaces/kali.ico')

miFrame = Frame(root, width=600, height=400)

miFrame.pack()

# miLabel = Label(miFrame, text='Hola mundo')

#miLabel.pack() # Si ejecutamos el programa podemos ver que la ventana es pequeña, esta ajustada al contenido del label y eso se debe a que estamos empaquetando el label lo cual hace que el contenedor se adapte al tamaño del label, si queremos que esto no ocurra tenemos que cambiar el pack por el metodo llamado place

#miLabel.place(x=10, y=20) # Este metodo nos permite ubicar el label en la posicion que nosotros queramos dandole como parametros medidas en pixeles en la direccion 'x' o 'y'. Esta sintaxis junto con la de la variable miLabel se puede abreviar. Si no vamos a ocupar la variable miLabel mas adelante para algo mas podemos prescindir de declarar la variable y ponemos el metodo Label de forma directa y a este le agregamos el metodo place con la nomenclatura del punto

Label(miFrame, text='Saludos terricolas').place(x=250, y=5) # Esto es una forma de abeviar el codigo si que el label no lo vamos a ocupar mas adelante como para que sea necesario guardarlo en una variable como lo hicimos anteriormente. Ademas podemos seguir agregando opciones dentro del label y funcionara. Lo voy a hacer en una linea de codigo abajo para que se vea la diferencia

Label(miFrame, text='Venimos en paz', fg='red', font=('Z003', 18)).place(x=200, y=50)

imagen = PhotoImage('lobo_2.png')

Label(miFrame, image=imagen).place(x=20, y=20) # Lo de las imagenes lo tengo que revisar ya que tengo un problema con estas y este es que siempre me da un error ya sea con la imagen .ico al utilizar el metodo iconbitmap asi como con esta imagen que estoy tratando de colocar en el frame mediante el metodo PhotoImage y al colocarla en el frame me da igual un error, el mismo que me da cuando quiero poner una imagen en la ventana con el metodo iconbitmap

root.mainloop()

# iMPORTANTE: NO ENTIENDO PORQUE TENGO PROBLEMAS AL QUERER COLOCAR IMAGENES, YA SE EN EL FRAME, EN LA RAIZ O EN DONDE SEA, SIEMPRE ME ARROJA UN ERROR DE QUE EL ARCHIVO NO EXISTE AUNQUE ESTE EN LA MISMA CARPETA O LE PONGA LA RUTA COMPLETA, NO IMPORTA COMO DEFINA LA IMAGEN, SIN O CON RUTA, SIN O CON EXTENSION ETC ETC ETC (YA HICE DIFERETES DE PRUEBAS DE COMO PONER EL CODIGO HABAER SI CAMBIANDO LA SINTAXIS FUNCIONA PERO NO, NO FUNCIONA)