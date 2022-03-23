# Interfaces Graficas - Pildoras Informaticas / Videos 53 y 54 - Ventanas Emergentes

# Ventanas emergentes --> Son ventanas modales para informar, avisar o permitir realizar tareas al usuario

# Ventana emergente para abrir archivos --> Esta ventana es la tipica ventana que vemos en la mayoria de programas que nos permiten abrir archivos desde su interfaz grafica mediante la pestaña de "Archivo --> Abrir como o Abrir"

# Para hacer uso de estas ventanas emergentes de apertura de archivos es necesario importar otra libreria de tkinter de forma independiente y esta es 'filedialog'

# La libreria filedialog contiene funciones que nos permiten abrir, guardar y mas, y obviamente debemos de llamar a las funciones encargadas de cada una de estas acciones al momento de quererlas realizar. El nombre de estas funciones las podemos encontrar en la documentacion oficial de Python, mas concretamente en el apartado de tkinter, pero para efectos de este tema utilizaremos la funcion llamada 'askopenfilename', el cual nos permite desplegar la ventana emergente que nos permitira navegar entre nuestros archivos y poder abrir el que queramos. Esta funcion admite y puede recibir varios parametros, de entrada el parametro title el cual contendra el nombre de la ventana, el parametro initialdir el cual nos permite definir la ruta en la que se encontrara al abrir esta ventana, y tambien podemos definir el tipo de archivo que queremos se puedan abrir, esto ultimo lo hacemos con el parametro filetypes() y dentro de este tenemos que pasarle en forma de tuplas los tipos de archivos que queremos que se puedan abrir, debemos poner como minimos 2 tuplas para que la ventana tenga opciones y podamos tener a nuestra dispocion esta opcion. Las tuplas deben contener 2 valores, el primero sera el nombre con el que vamos a identificar el tipo de archivos y el segundo la extension de estos, estas tuplas deben de ir de forma independiente y separadas por una coma, pero todas y cada una de ellas dentro de los parentesis del parametro filetypes

# Las ventanas emergentes no forman parte de la biblioteca estandar de tkinter, por lo tanto hay que importarlas de forma independiente

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('Ventanas emergentes')

def acerca_de():
    messagebox.showinfo('Paladium', 'Programa Paladium para la automatización de sistemas de control de diferentes marcas que permitan la inteacción con audio, iluminación, redes etc...')
    
def licencia():
    messagebox.showwarning('Licencia', 'Licencia bajo la norma GUI. Licencia no reestrictiva')
    
def salir():
    valor = messagebox.askquestion('Salir', 'Deseas salir del programa?')
    
    if valor == 'yes':
        root.destroy()
        
def cerrar_sesion():
    valor = messagebox.askokcancel('Cerrar Sesión', 'Esta seguro que desea cerrar la sesión?')
    
    if valor == True:
        root.destroy()
        
def reintentarGurdado():
    valor = messagebox.askretrycancel('Reintentar guardado', 'No ha sido posible guarda el archivo. Desea reintentar?')
    
    if valor == False:
        root.destroy()
        
def reportarProblema():
    valor = messagebox.askretrycancel('Problema Reportado', 'No ha sido posible reportar el problema. Desea intentarlo de nuevo?')
    
    if valor != True:
        root.destroy()
        
def abrirArchivo():
    abrir_file = filedialog.askopenfilename(title='Abrir', initialdir='/home/eliab_hdez', filetypes=(('Archivos de Python', '*.py'), ('Archivos de texto', '*.txt'), ('Todos los archivos', '*.*')))
    
    print(abrir_file)

main_menu = Menu(root)
root.config(menu=main_menu, width=400, height=200)

boton_abrir = Button(root, text='Open file', command=abrirArchivo)
boton_abrir.grid(row=1, column=1, padx=100, pady=50)

archivo = Menu(main_menu, tearoff=0)
archivo.add_command(label='Nuevo')
archivo.add_command(label='Abrir', command=abrirArchivo)
archivo.add_command(label='Guardar', command=reintentarGurdado)
archivo.add_command(label='Cerrar Sesión', command=cerrar_sesion)
archivo.add_command(label='Salir', command=salir)

edicion = Menu(main_menu, tearoff=0)
edicion.add_command(label='Copiar')
edicion.add_command(label='Cortar')
edicion.add_command(label='Pegar')

tools = Menu(main_menu, tearoff=0)
tools.add_command(label='Seleccionar todo')
tools.add_command(label='Busqueda')
tools.add_command(label='Configuración')

ayuda = Menu(main_menu, tearoff=0)
ayuda.add_command(label='Licencia', command=licencia)
ayuda.add_command(label='Reportar un problema', command=reportarProblema)
ayuda.add_command(label='Acerca de', command=acerca_de)

main_menu.add_cascade(label='Archivo', menu=archivo)
main_menu.add_cascade(label='Edición', menu=edicion)
main_menu.add_cascade(label='Herramientas', menu=tools)
main_menu.add_cascade(label='Ayuda', menu=ayuda)

root.mainloop()

# Porque estamos haciendo uso de los nombres de las librerias importadas cada vez que las queremos utilizar como la libreria messagebox y la libreria filedialog??? Recordar que cuando importamos librerias tenemos 3 formas y cuando no importamos por medio del '*' es necesario anteponer el nombre de la libreria al metodo que vamos a ocupar de esa libreria, es decir, estamos llamando a la libreria y posteriormente a la funcion que contiene esa libreria, en el caso de estas dos librerias tenemos que hacerlo de esta manera ya que aunque la estamos importando desde la libreria tkinter estas no vienen dentro del conjunto general de librerias por lo tanto no estan disponibles con el 'from tkinter import *', asi que hay que llamarlas de forma independiente y al hacerlo estamos generando el llamado de estas librerias por su cuenta, por lo tanto ponemos from tkinter import filedialog y esto hace que cada vez que queramos ocupar una de las funciones de estas librerias tengamos que llamar a la libreria antes que a su funcion