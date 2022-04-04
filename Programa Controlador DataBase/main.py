# CONTROLADOR DE BASE DE DATOS

# INTERFAZ GRAFICA

import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText # Libreria para importar cuadros de texto pero con la barra de desplazamiento integrada dentro del mismo cuadro de texto y configurada para que trabaje de forma normal y adecuada, como conoces que trabajan estas barras de desplazamiento

root = Tk()
root.title('DATABASE CONTROLLER')
root.resizable(0,0)

# ----------- Imagen ico a mostrar en Windows ----------

root.iconbitmap('Imagenes/eclog2.ico')

# ---------- Variables contenedoras de la informacion proporcionada por el cliente en los campos de la entrada de datos ----------

id_cliente = StringVar()
nombre_cliente = StringVar()
apellido_cliente = StringVar()
telefono_cliente = StringVar()
email_cliente = StringVar()
empresa_cliente = StringVar()

# ------------ Funciones menu -------------

def crearBaseDatos():
    
    establecer_conexion = sqlite3.connect('Clientes')
    
    puntero = establecer_conexion.cursor()
    
    # Yo habia puesto la conexion a la base de datos y el puntero dentro del try, pero no es necesario ya que el error se generaria al querer crear la base de datos si esta ya existe, pero la conexion y la creacion del puntero no dan error alguno, al contrario, se necesitan hacer para poder trabajar con la base de datos, por lo tanto no es necesario que esten dentro del try y pueden quedar fuera sin problema alguno
        
    try:
        puntero.execute('''
                            CREATE TABLE CLIENTES (
                                ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                                NOMBRE VARCHAR(20), 
                                APELLIDOS VARCHAR(30), 
                                TELEFONO VARCHAR(15) UNIQUE, 
                                EMAIL VARCHAR(50) UNIQUE, 
                                EMPRESA VARCHAR(30),
                                COMENTARIOS VARCHAR(100))
                        ''')
        
        messagebox.showinfo('Base de Datos', 'Base de Datos creada con éxito')
        
    except: # sqlite3.OperationalError --> Yo habia puesto el error que generaba la creacion de la base de datos si esta ya existia, pero no es necesario ya que el except se estaria ejecutando si o si tenga declarado o no el error, siempre y cuando el try no se cumpla o se ejecute
        messagebox.showwarning('Advertencia', 'La Base de Datos "Clientes" ya existe')
    
    establecer_conexion.close()
    
def salir():
    exit = messagebox.askquestion('Salir', '¿Desea salir del programa?')
    
    if exit == 'yes':
        root.destroy()
        
def crearRegistro():
    
    resultado_bd_texto.delete('1.0', END)
    
    establecer_conexion = sqlite3.connect('Clientes')
    
    puntero = establecer_conexion.cursor()
    
    # ------- Registros agregados mediante concatenacion de la instruccion SQL a los valores de la base de datos
    
    # puntero.execute("INSERT INTO CLIENTES VALUES(NULL, '" + nombre_cliente.get() + 
    #                 "','" + apellido_cliente.get() + 
    #                 "','" + telefono_cliente.get() + 
    #                 "','" + email_cliente.get() + 
    #                 "','" + empresa_cliente.get() + 
    #                 "','" + info_adicional.get("1.0", END) + "')")
    
    # -------- Registros agregados mediante la creacion de una lista, la cual nos permite eliminar la concatenacion del ejemplo anterior
    
    # clientes = [
    #     nombre_cliente.get(),
    #     apellido_cliente.get(),
    #     telefono_cliente.get(),
    #     email_cliente.get(),
    #     empresa_cliente.get(),
    #     info_adicional.get('1.0', END)
    # ]
    
    # puntero.execute('''INSERT INTO CLIENTES VALUES (NULL,?,?,?,?,?,?)''', clientes)
    
    # CONSULTAS PARAMETRIZADAS
    
    # Las consultas parametrizadas son las que en lugar de criterios utilizan interrogantes y estas las podemos utilizar en instrucciones SQL de tipo insert y update. Con estas nos evitamos el el engorroso codigo de ir concatenando la instruccion sql con los criterios
    
    # Para hacer uso de las consultas parametrizadas necesitamos almacenar en una variable la informacion de los campos que estarian conformando la instruccion sql y que seran relacionados con los interrogantes
    
    # Es muy similar a hacerlo mediante una lista, sin embargo esto solo es para la creacion de registros, pero para el update es mejor y mas sencillo, ya que para el update la creacion de una lista y actualizar mediante esta lista es mas lioso
    
    datos_clientes = nombre_cliente.get(), apellido_cliente.get(), telefono_cliente.get(), email_cliente.get(), empresa_cliente.get(), info_adicional.get('1.0', END)
    
    puntero.execute("""INSERT INTO CLIENTES VALUES (NULL,?,?,?,?,?,?)""", (datos_clientes))
    
    establecer_conexion.commit()
    
    establecer_conexion.close()
    
    resultado_bd_texto.insert(END, f'Se agrego el siguiente cliente\n{nombre_cliente.get()} | {apellido_cliente.get()} | {telefono_cliente.get()} | {email_cliente.get()}')
    
    messagebox.showinfo('Base de Datos', 'Registro insertado con éxito')
    
    id_cliente.set('')
    nombre_cliente.set('')
    apellido_cliente.set('')
    telefono_cliente.set('')
    email_cliente.set('')
    empresa_cliente.set('')
    info_adicional.delete('1.0', END)
    
def mostrarRegistro():
    
    name = f"'{nombre_cliente.get()}'"
    
    establecer_conexion = sqlite3.connect('Clientes')
    
    puntero = establecer_conexion.cursor()
    
    puntero.execute(""" SELECT * FROM CLIENTES WHERE NOMBRE = """ + name)
    
    usuario = puntero.fetchall()
    
    for i in usuario:
        
        info_adicional.delete('1.0', END)
        id_cliente.set(i[0])
        nombre_cliente.set(i[1])
        apellido_cliente.set(i[2])
        telefono_cliente.set(i[3])
        email_cliente.set(i[4])
        empresa_cliente.set(i[5])
        info_adicional.insert(1.0, i[6])
        
    establecer_conexion.commit()
    
    resultado_bd_texto.delete('1.0', END)
    
    resultado_bd_texto.insert(END, f'Cliente:\n{id_cliente.get()} - {nombre_cliente.get()} - {apellido_cliente.get()} - {telefono_cliente.get()} - {email_cliente.get()} - {empresa_cliente.get()}')
    
    if len(usuario) > 1:
        messagebox.showinfo('Clientes', f'Tiene 2 o mas clientes con el nombre de "{name}"\n\n {usuario}')
        
def borrarRegistro():
    
    resultado_bd_texto.delete('1.0', END)
    
    establecer_conexion = sqlite3.connect('Clientes')
    
    puntero = establecer_conexion.cursor()
    
    puntero.execute(""" DELETE FROM CLIENTES WHERE ID = """ + id_cliente.get())
    
    establecer_conexion.commit()
    
    messagebox.showinfo('Base de Datos', 'Registro borrado con éxito')
    
    resultado_bd_texto.insert(END, f'Se elimino el registro asociado al ID: {id_cliente.get()}')
    
    id_cliente.set('')
    nombre_cliente.set('')
    apellido_cliente.set('')
    telefono_cliente.set('')
    email_cliente.set('')
    empresa_cliente.set('')
    info_adicional.delete('1.0', END)
    
def actualizarRegistro():
    
    resultado_bd_texto.delete('1.0', END)
    
    establecer_conexion = sqlite3.connect('Clientes')
    
    puntero = establecer_conexion.cursor()
    
    # puntero.execute("UPDATE CLIENTES SET NOMBRE = '" + nombre_cliente.get() + 
    #                 "', APELLIDOS ='" + apellido_cliente.get() + 
    #                 "', TELEFONO ='" + telefono_cliente.get() + 
    #                 "', EMAIL ='" + email_cliente.get() + 
    #                 "', EMPRESA ='" + empresa_cliente.get() + 
    #                 "', COMENTARIOS ='" + info_adicional.get("1.0", END) + 
    #                 "'WHERE ID = " + id_cliente.get())
    
    # ------ Actualizacion de un registro mediante consulta parametrizada
    
    datos_clientes = nombre_cliente.get(), apellido_cliente.get(), telefono_cliente.get(), email_cliente.get(), empresa_cliente.get(), info_adicional.get('1.0', END)
    
    puntero.execute('''UPDATE CLIENTES SET NOMBRE=?, APELLIDOS=?, TELEFONO=?, EMAIL=?, EMPRESA=?, COMENTARIOS=? WHERE ID = ''' + id_cliente.get(),(datos_clientes))
    
    establecer_conexion.commit()
    
    establecer_conexion.close()
    
    resultado_bd_texto.insert(END, f'Se actualizo el cliente\n\nDatos nuevos:\n{id_cliente.get()} | {nombre_cliente.get()} | {apellido_cliente.get()} | {telefono_cliente.get()} | {email_cliente.get()}')
    
    messagebox.showinfo('Base de Datos', 'Registro actualizado con éxito')
    
    id_cliente.set('')
    nombre_cliente.set('')
    apellido_cliente.set('')
    telefono_cliente.set('')
    email_cliente.set('')
    empresa_cliente.set('')
    info_adicional.delete('1.0', END)
        
def borrarCampos():
    id_cliente.set('')
    nombre_cliente.set('')
    apellido_cliente.set('')
    telefono_cliente.set('')
    email_cliente.set('')
    empresa_cliente.set('')
    # Para borrar el texto de un Text() se hace de la siguiente manera: Variable asignada al Text(), (cuadro de texto) mas la funcion delete() usando la nomenclatura del punto
    info_adicional.delete('1.0', END) # Con el delete borramos la informacion del cuadro de texto y con los parametros entre parentesis (1.0 y END) le estamos diciendo que borre desde el primer caracter hasta el final del texto
    
def resaltarCampos():
    id_entry.config(bg='#92D6FF')
    nombre_entry.config(bg='#92D6FF')
    apellido_entry.config(bg='#92D6FF')
    telefono_entry.config(bg='#92D6FF')
    email_entry.config(bg='#92D6FF')
    
def ayudaUsuario():
    messagebox.showinfo('Ayuda', 'El Controlador de Base de Datos - DBC es un programa sencillo y facil de usar al igual que muy útil, eficiente y bastante potente para su propósito.\n\nEn el menú superior encontraras 5 pestañas: BBDD, Campos, Acciones y Ayuda.\n\n< BBDD >\n  Conectar: Crea y conecta con una Base de Datos nueva denomida "Clientes"\n  Salir: Cierra la aplicación.\n\n< CAMPOS >\n  Borrar campos: Borra la información ingresada en los campos.\n  Campos obligatorios: Resalta los campos que son obligatorios para su llenado.\n\n< ACCIONES >\n  Crear registro: Crea un registro nuevo.\n  Mostrar registro: Muestra en los campos un registro existente en la Base de Datos.\n  Borrar registro: Borra un registro ya existente en la Base de Datos.\n  Actualizar registro: Actuliza la información y/o datos de un registro existente.\n\n< AYUDA >\n  Ayuda: Despliega una ventana con la ayuda referente al uso del programa DBC.\n  Licencia: Muestra el tipo de Licencia de DBC.\n  Acerca de: Informa del propósito, ventajas y forma en la que se rige DBC.')
    
def licencia():
    messagebox.showinfo('Licencia', 'Licencia GNU\n\nSoftware libre y de codigo abierto, registrado bajo el usuario que lo instala y registra')
    
def acercaDe():
    messagebox.showinfo('Acerca de DBC','Creador DBC: Moises Eliab Hernandez Lopez\n\nProgramado y escrito en: Python 3.10.1\n\nVersion: v1.0\n\nEl programa Controlador de Base de Datos - DBC tiene como finalidad brindar al usuario una forma rapida y sencila de crear base de datos sencilas pero útiles que le permitan controlar y organizar los clientes que tiene registrados en su empresa o corporación.\n\nTeniendo como principios el software libre, con el propósito de que este al alcance de cualquiera, sin la necesidad de un gasto monetario. Este se sostiene de apoyos y donaciones.\n\nSi te interesa colaborar con el proyecto de forma economica para continuar con su desarrollo y mejora, puedes hacerlo poniendote en contacto al número telefónico 55-5555-5555, o bien donando a nuestra cuenta de PayPal')
    
def mostrarBaseDatos():
    
    resultado_bd_texto.delete('1.0', END)
    
    resultado_bd_texto.insert('1.0', 'ID | NOMBRE | APELLIDO | TELEFONO | EMAIL | EMPRESA\n\n')
    
    establecer_conexion = sqlite3.connect('Clientes')
    
    puntero = establecer_conexion.cursor()
    
    puntero.execute('SELECT * FROM CLIENTES')
    
    extraer_Bd = puntero.fetchall()
    
    
    for c in extraer_Bd:
        clientes = c
        id_db, nombre_db, apellido_db, telefono_db, email_db, empresa_db, comentario_db = clientes
        # resultado_bd_texto.insert('1.0', f'{clientes[0:6]}\n')
        resultado_bd_texto.insert(END, f'{id_db}, {nombre_db}, {apellido_db}, {telefono_db}, {email_db}, {empresa_db}\n')
    
# ----------- Menu principal ------------

main_menu = Menu(root, relief='flat', bg='#333333', fg='#85C1E9')
root.config(menu=main_menu)
root.config(bg='#333333')

# ------------ Contenido botones menu -------------

bbdd = Menu(main_menu, tearoff=0)
bbdd.add_command(label='Conectar', command=crearBaseDatos)
bbdd.add_separator()
bbdd.add_command(label='Salir', command=salir)

acciones = Menu(main_menu, tearoff=0)
acciones.add_command(label='Crear registro', command=crearRegistro)
acciones.add_command(label='Mostrar registro', command=mostrarRegistro)
acciones.add_command(label='Borrar registro', command=borrarRegistro)
acciones.add_command(label='Actualizar BBDD', command=actualizarRegistro)

campos = Menu(main_menu, tearoff=0)
campos.add_command(label='Borrar campos', command=borrarCampos)
campos.add_command(label='Campos Obligatorios', command=resaltarCampos)

ayuda = Menu(main_menu, tearoff=0)
ayuda.add_command(label='Ayuda', command=ayudaUsuario)
ayuda.add_separator()
ayuda.add_command(label='Licencia', command=licencia)
ayuda.add_command(label='Acerca de', command=acercaDe)

main_menu.add_cascade(label='BBDD', menu=bbdd)
main_menu.add_cascade(label='Acciones', menu=acciones)
main_menu.add_cascade(label='Campos', menu=campos)
main_menu.add_cascade(label='Ayuda', menu=ayuda)
# main_menu.config(bg='#333333', fg='#85C1E9')

# ----------- Frame principal -----------

main_frame = Frame(root)
main_frame.pack()
main_frame.config(bg='#333333')

# ---------- Entrada de Datos -------------

id_label = Label(main_frame, text='ID Cliente', bg='#333333', fg='#DCDCDC')
id_label.grid(row=1, column=1, padx=10, pady=2, sticky='w')

id_entry = Entry(main_frame, textvariable=id_cliente)
id_entry.grid(row=2, column=1, padx=20, pady=2)
id_entry.config(justify='center')

nombre_label = Label(main_frame, text='Nombre(s)', bg='#333333', fg='#DCDCDC')
nombre_label.grid(row=1, column=2, padx=10, pady=2, sticky='w')

nombre_entry = Entry(main_frame, textvariable=nombre_cliente, )
nombre_entry.grid(row=2, column=2, padx=20, pady=2)
nombre_entry.config(justify='center')

apellido_label = Label(main_frame, text='Apellidos', bg='#333333', fg='#DCDCDC')
apellido_label.grid(row=1, column=3, padx=10, pady=2, sticky='w')

apellido_entry = Entry(main_frame, textvariable=apellido_cliente)
apellido_entry.grid(row=2, column=3, padx=20, pady=2)
apellido_entry.config(justify='center')

telefono_label = Label(main_frame, text='Teléfono', bg='#333333', fg='#DCDCDC')
telefono_label.grid(row=3, column=1, padx=10, pady=2, sticky='w')

telefono_entry = Entry(main_frame, textvariable=telefono_cliente)
telefono_entry.grid(row=4, column=1, padx=20, pady=2)
telefono_entry.config(justify='center')

email_label = Label(main_frame, text='Email', bg='#333333', fg='#DCDCDC')
email_label.grid(row=3, column=2, padx=10, pady=2, sticky='w')

email_entry = Entry(main_frame, textvariable=email_cliente)
email_entry.grid(row=4, column=2, padx=20, pady=2)
email_entry.config(justify='center')

empresa_label = Label(main_frame, text='Empresa', bg='#333333', fg='#DCDCDC')
empresa_label.grid(row=3, column=3, padx=10, pady=2, sticky='w')

empresa_entry = Entry(main_frame, textvariable=empresa_cliente)
empresa_entry.grid(row=4, column=3, padx=20, pady=2)
empresa_entry.config(justify='center')

comentarios_label = Label(main_frame, text='Información Adicional', bg='#333333', fg='#DCDCDC')
comentarios_label.grid(row=1, column=4, padx=10, pady=2, sticky='nswe')

#info_adicional = Text(main_frame, width=15, height=5, font=('Z003', 10))
info_adicional = ScrolledText(main_frame, width=15, height=4, font=('Z003', 10)) # Cuadro de texto con barra de desplazamiento integrada
info_adicional.grid(row=2, rowspan=4, column=4, padx=10, pady=5)

# barra_desp = Scrollbar(main_frame, command=info_adicional.yview)
# barra_desp.grid(row=7, column=3, sticky='ns', pady=10)

# info_adicional.config(yscrollcommand=barra_desp.set)

# --------- Frame contenedor botones -----------

frame_botones = Frame(root, width=320, height=40, bg='#333333', pady=6)
frame_botones.pack()

# --------- Botones inferiores ------------

# campos_botones = Label(frame_botones, text='Campos Formulario', bg='#333333', fg='#DCDCDC', font=('Z003', 12))
# campos_botones.grid(row=1, column=1, columnspan=4, padx=2, pady=5)

# borrar_campos = Button(frame_botones, text='Resetear campos', bg='#333333', highlightthickness=0, fg='#F9F850', padx=8, pady=2, command=borrarCampos)
# borrar_campos.grid(row=2, column=1, columnspan=2, padx=2, pady=5)

# campos_obligatorios = Button(frame_botones, text='Campos obligatorios', bg='#333333', highlightthickness=0, fg='#F9F850', padx=8, pady=2, command=resaltarCampos)
# campos_obligatorios.grid(row=2, column=3, columnspan=2, padx=2, pady=5)

# registros_botones = Label(frame_botones, text='Registros', bg='#333333', fg='#DCDCDC', font=('Z003', 12))
# registros_botones.grid(row=3, column=1, columnspan=4, padx=2, pady=5)

# crear_registro = Button(frame_botones, text='Crear', bg='#333333', highlightthickness=0, fg='#85C1E9', padx=8, pady=2, command=crearRegistro)
# crear_registro.grid(row=4, column=1, padx=2)

# mostar_registro = Button(frame_botones, text='Mostrar', bg='#333333', highlightthickness=0, fg='#85C1E9', padx=8, pady=2)
# mostar_registro.grid(row=4, column=2, padx=2)

# borrar_registro = Button(frame_botones, text='Borrar', bg='#333333', highlightthickness=0, fg='#F7441D', padx=8, pady=2)
# borrar_registro.grid(row=4, column=3, padx=2)

# update_BBDD = Button(frame_botones, text='Actualizar', bg='#333333', highlightthickness=0, fg='#2AEE4D', padx=8, pady=2)
# update_BBDD.grid(row=4, column=4, padx=2)

registros_botones = Label(frame_botones, text='REGISTROS', bg='#333333', fg='#DCDCDC', font=('Z003', 10), width=20)
registros_botones.grid(row=1, column=1, columnspan=4, padx=2, pady=10, sticky='nswe')

crear_registro = Button(frame_botones, text='Crear', bg='#333333', highlightthickness=0, fg='#85C1E9', padx=8, pady=2, width=10, command=crearRegistro)
crear_registro.grid(row=2, column=1, padx=2)

mostar_registro = Button(frame_botones, text='Mostrar', bg='#333333', highlightthickness=0, fg='#85C1E9', padx=8, pady=2, width=10, command=mostrarRegistro)
mostar_registro.grid(row=2, column=2, padx=2)

borrar_registro = Button(frame_botones, text='Borrar', bg='#333333', highlightthickness=0, fg='#F7441D', padx=8, pady=2, width=10, command=borrarRegistro)
borrar_registro.grid(row=2, column=3, padx=2)

update_BBDD = Button(frame_botones, text='Actualizar', bg='#333333', highlightthickness=0, fg='#2AEE4D', padx=8, pady=2, width=10, command=actualizarRegistro)
update_BBDD.grid(row=2, column=4, padx=2)

separador_botones = Label(frame_botones, text='', bg='#333333', highlightthickness=0, fg='#DCDCDC', padx=8, pady=2, width=2)
separador_botones.grid(row=2, column=5, padx=2)

campos_botones = Label(frame_botones, text='CAMPOS', bg='#333333', fg='#DCDCDC', font=('Z003', 10), width=20)
campos_botones.grid(row=1, column=6, columnspan=7, padx=2, pady=10, sticky='nswe')

borrar_campos = Button(frame_botones, text='Resetear', bg='#333333', highlightthickness=0, fg='#F9F850', padx=8, pady=2, width=10, command=borrarCampos)
borrar_campos.grid(row=2, column=6, padx=2, pady=5)

campos_obligatorios = Button(frame_botones, text='Resaltar C/O', bg='#333333', highlightthickness=0, fg='#F9F850', padx=8, pady=2, width=10, command=resaltarCampos)
campos_obligatorios.grid(row=2, column=7, padx=2, pady=5)

# --------- Frame contenedor interaccion Base de Datos -----------

frame_bd = Frame(root, width=200, height=100, bg='#333333', pady=6)
frame_bd.pack()

base_datos = Label(frame_bd, text='BASE DE DATOS', bg='#333333', fg='#DCDCDC', font=('Z003', 15))
base_datos.grid(row=1, column=3, padx=10, pady=10, sticky='nswe')

resultado_bd_texto = Text(frame_bd, bg='#222222', fg='#F7441D', width=90, height=13, font=('Z003', 10))
resultado_bd_texto.grid(row=2, rowspan=5, column=3, padx=15, pady=10)
resultado_bd_texto.insert('1.0', 'ID | NOMBRE | APELLIDO | TELEFONO | EMAIL | EMPRESA')
# resultado_bd_texto.index(END)

base_de_datos = Button(frame_bd, text='Mostar Base de Datos', bg='#333333', fg='#DCDCDC', font=('Z003', 10), width=30, command=mostrarBaseDatos)
base_de_datos.grid(row=7, column=3, padx=5, pady=5)

main_frame.mainloop()