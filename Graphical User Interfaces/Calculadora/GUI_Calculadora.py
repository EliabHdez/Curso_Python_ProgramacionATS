# Calculadora - Interfez Grafica

from tkinter import *

from matplotlib.pyplot import text

# Ventana Raiz

root = Tk()
root.title('Calculadora')

# Ventana frame 1

frame1 = Frame()
frame1.pack()

# Ventana tipo de calculadora

tipoCalculadora = Label(frame1, text='Estandar')
tipoCalculadora.grid(row=1, columnspan=6, padx=5, sticky='w')

# Pantalla de Digitos

pantallaDigitos = Entry(frame1)
pantallaDigitos.grid(columnspan=6, pady=10, padx=5, sticky='we')
pantallaDigitos.config(bg='#333333', fg='#03f943', justify='right')

# Teclado numerico

# Fila 1

boton7 = Button(frame1, text='7', width=3)
boton7.grid(row=3, column=1)
boton8 = Button(frame1, text='8', width=3)
boton8.grid(row=3, column=2)
boton9 = Button(frame1, text='9', width=3)
boton9.grid(row=3, column=3)
botonDiv = Button(frame1, text='/', width=3)
botonDiv.grid(row=3, column=4)
botonBorrar = Button(frame1, text='Del', width=3)
botonBorrar.grid(row=3, column=5)

# Fila 2

boton4 = Button(frame1, text='4', width=3)
boton4.grid(row=4, column=1)
boton5 = Button(frame1, text='5', width=3)
boton5.grid(row=4, column=2)
boton6 = Button(frame1, text='6', width=3)
boton6.grid(row=4, column=3)
botonMult = Button(frame1, text='x', width=3)
botonMult.grid(row=4, column=4)
botonC = Button(frame1, text='C', width=3)
botonC.grid(row=4, column=5)

# Fila 3

boton1 = Button(frame1, text='1', width=3)
boton1.grid(row=5, column=1)
boton2 = Button(frame1, text='2', width=3)
boton2.grid(row=5, column=2)
boton3 = Button(frame1, text='3', width=3)
boton3.grid(row=5, column=3)
botonResta = Button(frame1, text='-', width=3)
botonResta.grid(row=5, column=4)
botonCe = Button(frame1, text='CE', width=3)
botonCe.grid(row=5, column=5)

# Fila 4

botonPunto = Button(frame1, text='.', width=3)
botonPunto.grid(row=6, column=1)
boton0 = Button(frame1, text='0', width=3)
boton0.grid(row=6, column=2)
botonPorc = Button(frame1, text='%', width=3)
botonPorc.grid(row=6, column=3)
botonSuma = Button(frame1, text='+', width=3)
botonSuma.grid(row=6, column=4)
botonIgual = Button(frame1, text='=', width=3)
botonIgual.grid(row=6, column=5)

root.mainloop()