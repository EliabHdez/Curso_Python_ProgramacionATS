# Interfaces Graficas - Pildoras Informaticas / Videos 50 y 51 - Radiobuttons y Checkbuttons

# Radiobuttons / Botones de Radio --> Son botones de seleccion, los cuales se caracterizan por aceptar una respuesta unica al poder seleccionar solo uno de ellos

# Los radiobuttons reciben dos parametros: 1.- Cual va a ser su contenedor padre. 2.- El texto que va a acompañar este radiobutton el cual va a describir lo que se va a seleccionar

# Al momento de crearlos no podemos interactuar con ellos, de hecho aparecen en la interfaz grafica todos los que hayamos puesto como seleccionados y no podemos deseleccionarlos aunque presionemos con el mouse

# Se trata de que aparezcan desactivados y sea el usuario el que seleccione uno u otro. Y esto lo hacemos por medio de una variable y un valor. La particularidad de poder seleccionar solo uno, es que al momento de seleccionar otro el que estaba seleccionado se deselecciona. Solo puede haber uno activado

# Checkbuttons / Botones de seleccion multiple --> Son botones de seleccion multiple, los cuales tienen un diseño cuadrado, permiten seleccionar uno o mas al mismo tiempo

from tkinter import *

root = Tk()
root.title('Radio & Check Buttons')

main_frame = Frame(root)
main_frame.pack()

var_opcion = IntVar()

def mostrarSeleccion():
    print('1 - Masculino \n2 - Femenino')
    print(f'Usuario selecciono {var_opcion.get()}')
    
def mostrarGenero():
    
    if var_opcion.get() == 1:
        seleccion_usuario.config(fg='#FF1414', text='Tu género es Masculino')
        seleccion_usuario2.config(fg='#DCDCDC', text='Elegiste Masculino')
        
    elif var_opcion.get() == 2:
        seleccion_usuario.config(fg='#FF1414', text='Tu género es Femenino')
        seleccion_usuario2.config(fg='#DCDCDC', text='Elegiste Femenino')
        
    else:
        seleccion_usuario.config(fg='#FF1414', text='Tu género no fue definido')
        seleccion_usuario2.config(fg='#DCDCDC', text='Elegiste no definir')
        

genero = Label(main_frame, text='Selecciona tu Género', width=45)
genero.grid(row=1, column=1)

rb = Radiobutton(main_frame, text='Masculino', variable=var_opcion, value=1, command=mostrarGenero)
rb.grid(row=2, column=1, sticky='nswe')

rb2 = Radiobutton(main_frame, text='Femenino', variable=var_opcion, value=2, command=mostrarGenero)
rb2.grid(row=3, column=1, sticky='nswe')

rb3 = Radiobutton(main_frame, text='Sin definir', variable=var_opcion, value=3, command=mostrarGenero)
rb3.grid(row=4, column=1, sticky='nsew')

seleccion_usuario = Label(main_frame)
seleccion_usuario.grid(row=5, column=1, pady=5, sticky='we')

seleccion_usuario2 = Label(main_frame)
seleccion_usuario2.grid(row=6, column=1, pady=5, sticky='we')
seleccion_usuario2.config(bg='#222222', fg='#DCDCDC')

# Con la variable creada asignandole un valor de tipo entero conseguimos que estos radiobuttons trabajen de forma adecuada y esta es permitiendo que el usuario sea quien pueda elegir uno de estos y que al momento de seleccionar uno si hay otro seleccionado este ultimo se deseleccione. Tengo que analizar porque funciona de esta manera o si solo es lo estipulado para que funcione, ya que aunque lo tengo anotado, no entendi muy bien a que se debe y porque tenemos que crear una variable de tipo entero y esta declararla en el radiobutton junto con un valor para que estos trabajen de forma adecuada

frame2 = Frame(root)
frame2.pack()

imagen_viaje = PhotoImage(file='Imagenes/avion.png')
label_imagen = Label(frame2, image=imagen_viaje)
label_imagen.grid(row=6, column=1)

seleccion_destinos = Label(frame2, text='Elige tus destinos')
seleccion_destinos.grid(row=7, column=1, padx=67, pady=10)

# Lo siguiente fue lo que yo hice tratando de lograr hacer lo que aparecera despues de este comentario incluyendo la funcion comentada

# value_destino = 0
# var_opcion_destinos = IntVar()

# def seleccionDestino(destino):
#     global value_destino
#     global var_opcion_destinos
    
#     if destino == 'playa':
#         value_destino += 1
#         var_opcion_destinos = 1
#         print('Selecciono Playa como destino')
#         print(int(value_destino))
#     elif destino == 'selva':
#         value_destino += 1
#         var_opcion_destinos = 2
#         print('Selecciono Selva como destino')
#         print(value_destino)
#     elif destino == 'desierto':
#         value_destino += 1
#         var_opcion_destinos = 3
#         print('Selecciono Desierto como destino')
#         print(value_destino)
        
#     if var_opcion_destinos == 1:
#         destinos_viaje.config(text='Has seleccionado 1 destino')
#     elif var_opcion_destinos == 2:
#         destinos_viaje.config(text='Has seleccionado 2 destinos')
#     elif var_opcion_destinos == 3:
#         destinos_viaje.config(text='Has seleccionado 3 destinos')

playa = IntVar()
selva = IntVar()
desierto = IntVar()

def seleccionDestios():
    op_elegida = 'Has seleccionado como destino(s): '
    
    if playa.get() == 1:
        op_elegida += 'Playa'
        
    if selva.get() == 1:
        op_elegida += ', Selva'
        
    if desierto.get() == 1:
        op_elegida += ', Desierto'
        
    destinos_viaje.config(text=op_elegida)

cb = Checkbutton(frame2, text='Playa', variable=playa, onvalue=1, offvalue=0, command=seleccionDestios)
cb.grid(row=8, column=1, sticky='w', padx=100)

cb2 = Checkbutton(frame2, text='Selva', variable=selva, onvalue=1, offvalue=0, command=seleccionDestios)
cb2.grid(row=9, column=1, sticky='w', padx=100)

cb3 = Checkbutton(frame2, text='Desierto', variable=desierto, onvalue=1, offvalue=0, command=seleccionDestios)
cb3.grid(row=10, column=1, sticky='w', padx=100)

destinos_viaje = Label(frame2)
destinos_viaje.grid(row=11, column=1, pady=5, sticky='we')
destinos_viaje.config(bg='red', fg='#DCDCDC')

root.mainloop()