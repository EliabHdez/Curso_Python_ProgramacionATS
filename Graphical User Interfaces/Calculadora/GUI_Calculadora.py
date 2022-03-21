# Calculadora - Interfez Grafica

from tkinter import *

# Ventana Raiz

root = Tk()
root.title('Calculadora')
root.iconbitmap('Imagenes_Ico/calc.ico')

# Ventana frame 1

frame1 = Frame(root)
frame1.pack()
frame1.config(bg='#222222')

# Variables globales

operacion = ''

resultado = 0

resetPantalla = False

numApoyo = 0

punto = ''

# Ventana tipo de calculadora

tipoCalculadora = Label(frame1, text='Estandar')
tipoCalculadora.grid(row=1, columnspan=6, padx=5, sticky='w')
tipoCalculadora.config(bg='#222222', fg='#DCDCDC')

# Pantalla de Digitos Pulsados

numero = StringVar()

pantallaDigitos = Entry(frame1, textvariable=numero, font=('Z003', 13))
pantallaDigitos.grid(row=3, columnspan=6, pady=10, padx=5, sticky='we')
pantallaDigitos.config(bg='#333333', fg='#03f943', justify='right')

# Pantalla Almecenamiento de Digitos y Operaciones

pantallaAlmacenamiento = Label(frame1, textvariable=numero, font=('Z003', 10))
pantallaAlmacenamiento.grid(row=2, columnspan=6, padx=5, sticky='we')
pantallaAlmacenamiento.config(bg='#DCDCDC', fg='#222222')

# Teclado numerico

def botonPulsado(num):
    global resetPantalla
    
    if resetPantalla != False:
        numero.set(num)
        resetPantalla = False
    else:
        numero.set(f'{numero.get()}{num}')
        # numero.set(numero.get()+num) Esto es lo mismo de arriba, solo que con diferente sintaxis

def reset():
    global resetPantalla
    global resultado
    
    resultado = 0
    numero.set('')
    resetPantalla = False

# def borrar():
#     numero.set()
        
# Suma
    
def suma(num):
    global operacion
    global resultado
    global resetPantalla
    
    resultado = int(num)
    
    operacion = 'suma'
    
    numero.set(resultado)
    
    resetPantalla = True
    
# Resta

contador_resta = 0
    
def resta(num):
    global operacion
    global resultado
    global numApoyo
    global resetPantalla
    global contador_resta
    
    if contador_resta == 0:
        numApoyo = int(num)
        resultado = numApoyo
        
    else:
        if contador_resta == 1:
            resultado = numApoyo - int(num)
            
        else:
            resultado = resultado - int(num)
            
        numero.set(resultado)
        resultado = numero.get()
            
    contador_resta = contador_resta + 1
    
    operacion = 'resta'
    
    resetPantalla = True
    
# Multiplicacion

contador_mult = 0
    
def multiplicacion(num):
    global operacion
    global resultado
    global numApoyo
    global resetPantalla
    global contador_mult
    
    if contador_mult == 0:
        numApoyo = int(num)
        resultado = numApoyo
        
    else:
        if contador_mult == 1:
            resultado = numApoyo * int(num)
            
        else:
            resultado = resultado * int(num)
            
        numero.set(resultado)
        resultado = numero.get()
            
    contador_mult = contador_mult + 1
    
    operacion = 'multiplicacion'
    
    resetPantalla = True
    
# Division

contador_div = 0

def division(num):
    global operacion
    global resultado
    global numApoyo
    global resetPantalla
    global contador_div
    
    if contador_div == 0:
        numApoyo = float(num)
        resultado = numApoyo
        
    else:
        if contador_div == 1:
            resultado = numApoyo / float(num)
            
        else:
            resultado = resultado / float(num)
            
        numero.set(resultado)
        resultado = numero.get()
            
    contador_div = contador_div + 1
    
    operacion = 'division'
    
    resetPantalla = True
    
# Porcentaje

numSacarPorc = 0
contador_porc = 0

def porcentaje(num):
    global operacion
    global resultado
    global numApoyo
    global resetPantalla
    global contador_porc
    global numSacarPorc
    
    if contador_porc == 0:
        numSacarPorc = float(num)
        numApoyo = float(num)
        resultado = numApoyo
        
    else:
        if contador_porc == 1:
            resultado = numApoyo * float(num) / 100
            numSacarPorc = numSacarPorc - resultado
            resultado = numSacarPorc
            
        else:
            resultado = int(resultado) * float(num) / 100
            numSacarPorc = numSacarPorc - resultado
            resultado = numSacarPorc
            
        numero.set(resultado)
        resultado = numero.get()
            
    contador_porc = contador_porc + 1
    
    operacion = 'porcentaje'
    
    resetPantalla = True
    
def resultadoTotal():
    global resultado
    global operacion
    global contador_resta
    global contador_mult
    global contador_div
    global numSacarPorc
    
    if operacion == 'suma':
        numero.set(resultado + int(numero.get()))
        resultado = 0
        
    elif operacion == 'resta':
        numero.set(resultado - int(numero.get()))
        resultado = 0
        contador_resta = 0
        
    elif operacion == 'multiplicacion':
        numero.set(resultado * int(numero.get()))
        resultado = 0
        contador_mult = 0
        
    elif operacion == 'division':
        numero.set(resultado / float(numero.get()))
        resultado = 0
        contador_div = 0
        
    elif operacion == 'porcentaje':
        print(resultado)
        numSacarPorc = resultado * float(numero.get())
        numSacarPorc = numSacarPorc / 100
        resultado = resultado - numSacarPorc
        numero.set(resultado)
        resultado = 0
        
# Fila 1

boton7 = Button(frame1, text='7', width=5, height=2, command=lambda:botonPulsado('7'))
boton7.grid(row=4, column=2)
boton7.config(bg='#222222', fg='#FE3131')
boton8 = Button(frame1, text='8', width=5, height=2, command=lambda:botonPulsado('8'))
boton8.grid(row=4, column=3)
boton8.config(bg='#222222', fg='#FE3131')
boton9 = Button(frame1, text='9', width=5, height=2, command=lambda:botonPulsado('9'))
boton9.grid(row=4, column=4)
boton9.config(bg='#222222', fg='#FE3131')
botonDiv = Button(frame1, text='/', width=5, height=2, command=lambda:division(numero.get()))
botonDiv.grid(row=4, column=5)
botonDiv.config(bg='#444444', fg='#DCDCDC')
botonBorrar = Button(frame1, text='Del', width=5, height=2)
botonBorrar.grid(row=4, column=1)
botonBorrar.config(bg='#444444', fg='#DCDCDC')

# Fila 2

boton4 = Button(frame1, text='4', width=5, height=2, command=lambda:botonPulsado('4'))
boton4.grid(row=5, column=2)
boton4.config(bg='#222222', fg='#FE3131')
boton5 = Button(frame1, text='5', width=5, height=2, command=lambda:botonPulsado('5'))
boton5.grid(row=5, column=3)
boton5.config(bg='#222222', fg='#FE3131')
boton6 = Button(frame1, text='6', width=5, height=2, command=lambda:botonPulsado('6'))
boton6.grid(row=5, column=4)
boton6.config(bg='#222222', fg='#FE3131')
botonMult = Button(frame1, text='x', width=5, height=2, command=lambda:multiplicacion(numero.get()))
botonMult.grid(row=5, column=5)
botonMult.config(bg='#444444', fg='#DCDCDC')
botonC = Button(frame1, text='C', width=5, height=2, command=lambda:reset())
botonC.grid(row=5, column=1)
botonC.config(bg='#444444', fg='#DCDCDC')

# Fila 3

boton1 = Button(frame1, text='1', width=5, height=2, command=lambda:botonPulsado('1'))
boton1.grid(row=6, column=2)
boton1.config(bg='#222222', fg='#FE3131')
boton2 = Button(frame1, text='2', width=5, height=2, command=lambda:botonPulsado('2'))
boton2.grid(row=6, column=3)
boton2.config(bg='#222222', fg='#FE3131')
boton3 = Button(frame1, text='3', width=5, height=2, command=lambda:botonPulsado('3'))
boton3.grid(row=6, column=4)
boton3.config(bg='#222222', fg='#FE3131')
botonResta = Button(frame1, text='-', width=5, height=2, command=lambda:resta(numero.get()))
botonResta.grid(row=6, column=5)
botonResta.config(bg='#444444', fg='#DCDCDC')
botonCe = Button(frame1, text='CE', width=5, height=2)
botonCe.grid(row=6, column=1)
botonCe.config(bg='#444444', fg='#DCDCDC')

# Fila 4

botonPunto = Button(frame1, text='.', width=5, height=2, command=lambda:botonPulsado('.'))
botonPunto.grid(row=7, column=2)
botonPunto.config(bg='#444444', fg='#DCDCDC')
boton0 = Button(frame1, text='0', width=5, height=2, command=lambda:botonPulsado('0'))
boton0.grid(row=7, column=3)
boton0.config(bg='#222222', fg='#FE3131')
botonPorc = Button(frame1, text='%', width=5, height=2, command=lambda:porcentaje(numero.get()))
botonPorc.grid(row=7, column=1)
botonPorc.config(bg='#444444', fg='#DCDCDC')
botonSuma = Button(frame1, text='+', width=5, height=2, command=lambda:suma(numero.get()))
botonSuma.grid(row=7, column=5)
botonSuma.config(bg='#444444', fg='#DCDCDC')
botonIgual = Button(frame1, text='=', width=5, height=2, command=lambda:resultadoTotal())
botonIgual.grid(row=7, column=4)
botonIgual.config(bg='#444444', fg='#DCDCDC')

root.mainloop()