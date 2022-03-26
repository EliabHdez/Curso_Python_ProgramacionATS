# CONTROLADOR DE BASE DE DATOS

# INTERFAZ GRAFICA

from tkinter import *

root = Tk()
root.title('EC-LOG')

# ----------- Imagen ico a mostrar en Windows ----------

# root.iconbitmap('Imagenes/Logo.jpeg')

# ----------- Menu principal ------------

main_menu = Menu(root, relief='flat', bg='#333333', fg='#85C1E9')
root.config(menu=main_menu)
root.config(bg='#333333')

# ----------- Frame principal -----------

main_frame = Frame(root, width=400, height=400)
main_frame.pack()
main_frame.config(bg='#333333')

# ------------ Contenido botones menu -------------

bbdd = Menu(main_menu, tearoff=0)
bbdd.add_command(label='Conectar')
bbdd.add_separator()
bbdd.add_command(label='Salir')

campos = Menu(main_menu, tearoff=0)
campos.add_command(label='Borrar campos')
campos.add_command(label='Campos Obligatorios')

acciones = Menu(main_menu, tearoff=0)
acciones.add_command(label='Crear registro')
acciones.add_command(label='Mostrar registro')
acciones.add_command(label='Borrar registro')
acciones.add_command(label='Actualizar BBDD')

ayuda = Menu(main_menu, tearoff=0)
ayuda.add_command(label='Ayuda')
ayuda.add_separator()
ayuda.add_command(label='Licencia')
ayuda.add_command(label='Acerca de')

main_menu.add_cascade(label='BBDD', menu=bbdd)
main_menu.add_cascade(label='Campos', menu=campos)
main_menu.add_cascade(label='Acciones', menu=acciones)
main_menu.add_cascade(label='Ayuda', menu=ayuda)
# main_menu.config(bg='#333333', fg='#85C1E9')

# ---------- Variables contenedoras de la informacion proporcionada por el cliente en los campos de la entrada de datos ----------

id_cliente = StringVar()
nombre_cliente = StringVar()
apellido_cliente = StringVar()
telefono_cliente = StringVar()
email_cliente = StringVar()
pass_cliente = StringVar()
comentarios_cliente = StringVar()

# ---------- Entrada de Datos -------------

id_label = Label(main_frame, text='ID', bg='#333333', fg='#DCDCDC')
id_label.grid(row=1, column=1, padx=10, pady=10, sticky='w')

id_entry = Entry(main_frame, textvariable=id_cliente)
id_entry.grid(row=1, column=2, padx=20, pady=10)
id_entry.config(justify='center')

nombre_label = Label(main_frame, text='Nombre(s)', bg='#333333', fg='#DCDCDC')
nombre_label.grid(row=2, column=1, padx=10, pady=10, sticky='w')

nombre_entry = Entry(main_frame, textvariable=nombre_cliente)
nombre_entry.grid(row=2, column=2, padx=20, pady=10)
nombre_entry.config(justify='center')

apellido_label = Label(main_frame, text='Apellidos', bg='#333333', fg='#DCDCDC')
apellido_label.grid(row=3, column=1, padx=10, pady=10, sticky='w')

apellido_entry = Entry(main_frame, textvariable=apellido_cliente)
apellido_entry.grid(row=3, column=2, padx=20, pady=10)
apellido_entry.config(justify='center')

telefono_label = Label(main_frame, text='Teléfono', bg='#333333', fg='#DCDCDC')
telefono_label.grid(row=4, column=1, padx=10, pady=10, sticky='w')

telefono_entry = Entry(main_frame, textvariable=telefono_cliente)
telefono_entry.grid(row=4, column=2, padx=20, pady=10)
telefono_entry.config(justify='center')

email_label = Label(main_frame, text='Email', bg='#333333', fg='#DCDCDC')
email_label.grid(row=5, column=1, padx=10, pady=10, sticky='w')

email_entry = Entry(main_frame, textvariable=email_cliente)
email_entry.grid(row=5, column=2, padx=20, pady=10)
email_entry.config(justify='center')

passwors_label = Label(main_frame, text='Password', bg='#333333', fg='#DCDCDC')
passwors_label.grid(row=6, column=1, padx=10, pady=10, sticky='w')

password_entry = Entry(main_frame, textvariable=pass_cliente)
password_entry.grid(row=6, column=2, padx=20, pady=10)
password_entry.config(justify='center', show='*')

comentarios_label = Label(main_frame, text='Comentarios', bg='#333333', fg='#DCDCDC')
comentarios_label.grid(row=7, column=1, padx=10, pady=10, sticky='w')

comentarios_texto = Text(main_frame, width=18, height=5)
comentarios_texto.grid(row=7, column=2, padx=20, pady=10)

# --------- Frame contenedor botones -----------

frame_botones = Frame(root, width=320, height=40, bg='#333333', pady=6)
frame_botones.pack()

# --------- Botones inferiores ------------

crear_registro = Button(frame_botones, text='Crear', bg='#333333', highlightthickness=0, fg='#85C1E9')
crear_registro.grid(row=1, column=1, padx=2)

mostar_registro = Button(frame_botones, text='Mostrar', bg='#333333', highlightthickness=0, fg='#85C1E9')
mostar_registro.grid(row=1, column=2, padx=2)

borrar_registro = Button(frame_botones, text='Borrar', bg='#333333', highlightthickness=0, fg='#F7441D')
borrar_registro.grid(row=1, column=3, padx=2)

update_BBDD = Button(frame_botones, text='Update', bg='#333333', highlightthickness=0, fg='#2AEE4D')
update_BBDD.grid(row=1, column=4, padx=2)

main_frame.mainloop()