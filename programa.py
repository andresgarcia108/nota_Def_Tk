# Programa que recibe los datos de un estudiante y calcula la nota definitiva de una materia y su IMC

# Se importa tkinter y sus funciones
import tkinter
from tkinter import messagebox, ttk
from tkinter import *

# Se declara la variable correspondiente a la ventana principal

ventana__Principal = Tk()

ventana__Principal.title("Nota defintiva e IMC - Sistemas")
ventana__Principal.geometry("600x700")
ventana__Principal.resizable(False, False)
ventana__Principal.config(bg ="cyan3")

# Frame correspondiente a los datos del estudiante

frameDat = Frame(ventana__Principal)
frameDat.config(bg = "white" ,height=275, width=560)
frameDat.place(x=20, y =20)

# Texto correspondiente al frame de datos

labDat = Label(frameDat, text="Datos Personales")
labDat.config(font=("Arial", 16), bg="white")
labDat.place(x =200, y =20)

# Texto antes de la caja de datos (nombre)
labNombre = Label(frameDat, text="Nombre:")
labNombre.config(font=("Arial", 12), bg="white")
labNombre.place(x =20, y =60)

# Caja de datos (nombre)
nombre = Entry(frameDat)
nombre.config(bg="white", font=("Arial",12,) ,width=15)
nombre.focus_set()
nombre.place(x=90, y=60)

# Texto antes de la caja de datos(edad)
labEdad = Label(frameDat,text = "Edad:")
labEdad.config(font=("Arial", 12), bg="white")
labEdad.place(x=20 ,y=95)

# Caja de datos (edad)
edadent = Entry(frameDat)
edadent.config(bg="white", font=("Arial",12,) ,width=10)
edadent.focus_set()
edadent.place(x=70, y=95)

# Texto antes de la caja de datos(grado)
labGrado = Label(frameDat,text = "Grado:")
labGrado.config(font=("Arial", 12), bg="white")
labGrado.place(x=20 ,y=130)

# Caja de datos (grado)
gradoent = Entry(frameDat)
gradoent.config(bg="white", font=("Arial",12,) ,width=10)
gradoent.focus_set()
gradoent.place(x=75, y=130)

# Texto antes de la caja de datos(identificación)
labIdent = Label(frameDat,text = "Identificación:")
labIdent.config(font=("Arial", 12), bg="white")
labIdent.place(x=20 ,y=160)

# Caja de datos (identficación)
idenent = Entry(frameDat)
idenent.config(bg="white", font=("Arial",12,) ,width=10)
idenent.focus_set()
idenent.place(x=125, y=160)

# Texto antes de la caja de datos(teléfono)
labIdent = Label(frameDat,text = "Teléfono:")
labIdent.config(font=("Arial", 12), bg="white")
labIdent.place(x=20 ,y=190)

# Caja de datos (teléfono)
idenent = Entry(frameDat)
idenent.config(bg="white", font=("Arial",12,) ,width=10)
idenent.focus_set()
idenent.place(x=95, y=190)

# Texto antes de la caja de datos(sede)
labIdent = Label(frameDat,text = "Sede:")
labIdent.config(font=("Arial", 12), bg="white")
labIdent.place(x=20 ,y=220)

# Caja de datos (sede)
idenent = Entry(frameDat)
idenent.config(bg="white", font=("Arial",12,) ,width=10)
idenent.focus_set()
idenent.place(x=75, y=220)

# --------------------------------------

# Botón correspondiente a los datos de la materia
image_Notas = PhotoImage(file="./img/paulasiatico.png")
bot_Notas = Button(ventana__Principal)
bot_Notas.config(image=image_Notas)
bot_Notas.place(x=80, y =375)

# Texto arriba del botón datos
labIdent = Label(ventana__Principal,text = "Ingresar notas")
labIdent.config(font=("Arial", 12), bg="cyan3")
labIdent.place(x=105 ,y=350)




ventana__Principal.mainloop()