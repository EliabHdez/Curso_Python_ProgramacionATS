# Interfaces Graficas - Pildoras Informaticas / Video 52 - Menus y submenus

# Menus y submenus

from tkinter import *

root = Tk()
root.title('Menus y submenus')

main_menu = Menu(root) # Creamos la variable que albergara el menu, por lo tanto esta variable sera el menu de forma directa como tal
root.config(menu=main_menu, width=350, height=200) # Creamos el menu en la interfaz grafica, es decir lo ponemos ahi para que sea visible en la IG

archivo_menu = Menu(main_menu, tearoff=0) # Determinamos que sera un submenu y a que menu va a pertenecer este submenu y con tearoff=0 quitamos la franja de lineas intercaladas que viene por defecto
archivo_menu.add_command(label='Nuevo') # Creamos los submenus y los agregamos a la pestaña correspondiente del menu principal, asi como tambien le damos un nombre a cada elemento del submenu
archivo_menu.add_command(label='Abrir')
archivo_menu.add_command(label='Guardar')
archivo_menu.add_command(label='Guardar Como')
archivo_menu.add_separator() # Agregamos separadores que se ven comunmente en los submenus que sirven para separar bloques de elementos que son similares o que pertenecen a un grupo de acciones en comun
archivo_menu.add_command(label='Cerrar')
archivo_menu.add_command(label='Salir')
archivo_menu.add_command(label='Salir')

edicion_menu = Menu(main_menu, tearoff=0)
edicion_menu.add_command(label='Deshacer')
edicion_menu.add_command(label='Rehacer')
edicion_menu.add_separator()
edicion_menu.add_command(label='Copiar')
edicion_menu.add_command(label='Cortar')
edicion_menu.add_command(label='Pegar')

herramientas_menu = Menu(main_menu, tearoff=0)
herramientas_menu.add_command(label='Seleccionar Todo')
herramientas_menu.add_command(label='Expandir Seleccion')
herramientas_menu.add_command(label='Recortar Seleccion')
herramientas_menu.add_separator()
herramientas_menu.add_command(label='Búsqueda')
herramientas_menu.add_separator()
herramientas_menu.add_command(label='Apariencia')
herramientas_menu.add_command(label='Configuracion')

ayuda_menu = Menu(main_menu, tearoff=0)
ayuda_menu.add_command(label='Licencia')
ayuda_menu.add_separator()
ayuda_menu.add_command(label='Comenzar')
ayuda_menu.add_command(label='Documentación')
ayuda_menu.add_separator()
ayuda_menu.add_command(label='Reportar un problema')
ayuda_menu.add_separator()
ayuda_menu.add_command(label='Acerca de')

ir_menu = Menu(main_menu, tearoff=0)

main_menu.add_cascade(label='Archivo', menu=archivo_menu) # Agregamos el submenu al menu al que pertenecera, el menu padre, asi mismo le asignamos un nombre al submenu o a la pestaña que representara a este mismo
main_menu.add_cascade(label='Edición', menu=edicion_menu)
main_menu.add_cascade(label='Herramientas', menu=herramientas_menu)
main_menu.add_cascade(label='Ayuda', menu=ayuda_menu)
main_menu.add_cascade(label='Ir a', menu=ir_menu)

root.mainloop()