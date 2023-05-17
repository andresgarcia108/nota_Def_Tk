# Programa que recibe los datos de un estudiante y calcula la nota definitiva de una materia y su IMC

# Se importa tkinter y sus funciones
import tkinter as tk
from tkinter import messagebox, ttk, Tk
from tkinter import *

# Se declara la variable correspondiente a la ventana principal

# --------------------------------------
"""
# Botón correspondiente a los datos de la materia
image_Notas = PhotoImage(file="./img/baba.png")
bot_Notas = Button(ventana__Principal)
bot_Notas.config(image=image_Notas)
bot_Notas.place(x=80, y =375)

# Texto arriba del botón datos
labIdent = Label(ventana__Principal,text = "Ingresar notas")
labIdent.config(font=("Arial", 12), bg="bisque")
labIdent.place(x=105 ,y=350)

# Texto arriba del botón datos salud
labSalud = Label(ventana__Principal,text = "Datos sanidad")
labSalud.config(font=("Arial", 12), bg="bisque")
labSalud.place(x=360 ,y=350)

image_Salud = PhotoImage(file="./img/salud.png")
bot_Salud = Button(ventana__Principal)
bot_Salud.config(image=image_Salud)
bot_Salud.place (x=340, y =375)"""

ventana_Principal = Tk()
ventana_Principal.config(bg="white")
ventana_Principal.geometry("600x700")
ventana_Principal.resizable(False, False)
ventana_Principal.title("Calculadora de nota definitiva e IMC")

label1= Label(ventana_Principal, text="Calculadora de nota definitiva e IMC")
label1.config(font=("Arial", 16), bg="white")
label1.place(x=150, y =10)


ing_Salir = Button(ventana_Principal, text="Salir", command=ventana_Principal.destroy)
ing_Salir.config(font=("Arial", 12),height=1, width=25 )
ing_Salir.place(x=200, y=450)

sistemas = PhotoImage(file="./img/sistemas.png")

logoSistemas = Label(ventana_Principal)
logoSistemas.config(image=sistemas)
logoSistemas.place(x=475, y=500)

def ingDatosdf():
    datosPersonales = Toplevel()
    datosPersonales.geometry("600x300")
    datosPersonales.resizable(False, False)
    datosPersonales.title("Calculadora de nota definitiva e IMC")
    datosPersonales.config(bg="bisque")
    #--------------- Nombre --------------
    labNombre = Label(datosPersonales, text="Nombre:")
    labNombre.config(font=("Arial", 12), bg="bisque")
    labNombre.place(x =20, y =60)
    nombre = Entry(datosPersonales)
    nombre.pack()
    nombre.config(bg="white", font=("Arial",12,) ,width=18)
    nombre.focus_set()
    nombre.place(x=90, y=60)
    # ------------- Edad -------------
    labEdad = Label(datosPersonales,text = "Edad:")
    labEdad.config(font=("Arial", 12), bg="bisque")
    labEdad.place(x=20 ,y=95)
    edadent = Entry(datosPersonales)
    edadent.pack()
    edadent.config(bg="white", font=("Arial",12,) ,width=20)
    edadent.focus_set()
    edadent.place(x=70, y=95)
    # ------------ Grado ------------
    labGrado = Label(datosPersonales,text = "Grado:")
    labGrado.config(font=("Arial", 12), bg="bisque")
    labGrado.place(x=20 ,y=130)
    gradoent = Entry(datosPersonales)
    gradoent.pack()
    gradoent.config(bg="white", font=("Arial",12,) ,width=19)
    gradoent.focus_set()
    gradoent.place(x=75, y=130)
    # --------- Identificación ----------
    labIdent = Label(datosPersonales,text = "Identificación:")
    labIdent.config(font=("Arial", 12), bg="bisque")
    labIdent.place(x=20 ,y=160)
    idenent = Entry(datosPersonales)
    idenent.pack()
    idenent.config(bg="white", font=("Arial",12,) ,width=14)
    idenent.focus_set()
    idenent.place(x=125, y=160)
    # --------- Teléfono ------------
    labTelef = Label(datosPersonales,text = "Teléfono:")
    labTelef.config(font=("Arial", 12), bg="bisque")
    labTelef.place(x=20 ,y=190)
    idTelef = Entry(datosPersonales)
    idTelef.pack()
    idTelef.config(bg="white", font=("Arial",12,) ,width=17)
    idTelef.focus_set()
    idTelef.place(x=95, y=190)
    # ------------ Sede -----------
    labSede = Label(datosPersonales,text = "Sede:")
    labSede.config(font=("Arial", 12), bg="bisque")
    labSede.place(x=20 ,y=220)
    combo=ttk.Combobox(datosPersonales,state="reandonly",values =["A", "B", "C", "D", "E"])
    combo.pack()
    combo.place(x=80, y =220)
    combo.config(width=25)
    labDat = Label(datosPersonales, text="Datos Personales")
    labDat.config(font=("Arial", 16), bg="bisque")
    labDat.place(x =200, y =20)
    # ------------- Botón Salir ------------
    btnSalir = Button(datosPersonales, text="Salir", font=("Arial", 12), bg="red", fg="white", command=datosPersonales.destroy)
    btnSalir.place(x=280, y=260)



def ingNotas():
    notasPersonales = Toplevel()
    notasPersonales.geometry("600x300")
    notasPersonales.resizable(False, False)
    notasPersonales.title("Calculadora de nota definitiva e IMC")
    notasPersonales.config(bg="bisque")
    academica = Label(notasPersonales, text="Información académica")
    academica.config(bg="bisque", font=("Arial", 16))
    academica.place(x =200, y =15)

    # ------------ Materia-----------
    materiaLabel = Label(notasPersonales,text = "Materia:")
    materiaLabel.config(font=("Arial",12), bg ="bisque")
    materiaLabel.place(x =10, y=80)
    materiaCombo = ttk.Combobox(notasPersonales, state="reandonly", values=["Matemáticas", "Sociales", "Filosofía", "Religión", "Español", "Química", 
                                                                           "Física","Inglés", "Ciencias Políticas", "Artística", "Especialidad", "Estadística"])
    materiaCombo.place(x=75, y=80)
    materiaCombo.config(width=25)
    # ------------ Nota Cognitiva --------------
    notaCognitiva = Label(notasPersonales, text="Nota cognitiva:")
    notaCognitiva.config(font=("Arial", 12), bg ="bisque")
    notaCognitiva.place(x =10, y=110)
    entry_cog = Entry(notasPersonales)
    entry_cog.place(x=125, y=113)
    # ------------ Nota Procedimental --------------
    notaProcedimental = Label(notasPersonales, text="Nota procedimental:")
    notaProcedimental.config(font=("Arial", 12), bg ="bisque")
    notaProcedimental.place(x =10, y=140)
    entry_proce = Entry(notasPersonales)
    entry_proce.place(x=157, y=140)
    # ------------ Nota Actitudinal --------------
    notaActitudinal = Label(notasPersonales, text="Nota actitudinal:")
    notaActitudinal.config(font=("Arial", 12), bg ="bisque")
    notaActitudinal.place(x =10, y=173)
    entry_acti = Entry(notasPersonales)
    entry_acti.place(x=135, y=173)
    # ------------ Nota Autoevaluación --------------
    notaAutoevalu = Label(notasPersonales, text="Nota autoevaluación:")
    notaAutoevalu.config(font=("Arial", 12), bg ="bisque")
    notaAutoevalu.place(x =10, y=203)
    entry_cog = Entry(notasPersonales)
    entry_cog.place(x=165, y=203)
    # ------------ Nota Bimestral --------------
    notaBimestral = Label(notasPersonales, text="Nota bimestral:")
    notaBimestral.config(font=("Arial", 12), bg ="bisque")
    notaBimestral.place(x =10, y=203)
    entry_bime = Entry(notasPersonales)
    entry_bime.place(x=165, y=203)
    # ------------- Botón Salir ------------
    btnSalir = Button(notasPersonales, text="Salir", font=("Arial", 12), bg="red", fg="white", command=notasPersonales.destroy)
    btnSalir.place(x=250, y=260)
    # ------ Función calcular-------
    def calcular1():
        entry_proce_def = (entry_proce.get())
        entry_cog_def = (entry_cog.get())
        entry_auto_def = (entry_cog.get())
        entry_acti_def = (entry_acti.get())
        entry_bime_def = (entry_bime.get())

        entry_not_final = (0.3*entry_proce_def) + (0.3*entry_cog_def) + (0.1*entry_auto_def) + (0.1*entry_acti_def) + (0.2*entry_bime_def)

        if entry_not_final < 30:
                messagebox.showinfo("Resultado", "El alumno reprobo la asignatura  :")
        else:
                messagebox.showinfo("Resultado", "El alumno aprobo la asignatura :")

 


    boton1Calcular = Button(notasPersonales, text="Calcular", font=("Arial", 12), bg="green", fg="white", command=calcular1)
    boton1Calcular.place(x=350, y=260)

def ingSanidad():
    sanidadDatos = Toplevel()
    sanidadDatos.geometry("600x300")
    sanidadDatos.resizable(False, False)
    sanidadDatos.title("Calculadora de nota definitiva e IMC")
    sanidadDatos.config(bg="bisque")
    saludPaul = PhotoImage(file="./img/salud.png")
    holaLabel = Label(sanidadDatos,image=saludPaul)
    holaLabel.place(x=300, y =100)

    textoSalud = Label(sanidadDatos, text="Datos de Sanidad")
    textoSalud.config(font=("Arial", 16), bg="bisque")
    textoSalud.place(x=225, y=15)

    epsStr = Label(sanidadDatos, text="EPS:")
    epsStr.config(font=("Arial", 12), bg="bisque")
    epsStr.place(x=10, y =80)
    epsEntry = Entry(sanidadDatos)
    epsEntry.place(x=50, y=80)

    alturaFloat = Label(sanidadDatos, text="Altura(mt):")
    alturaFloat.config(font=("Arial", 12), bg="bisque")
    alturaFloat.place(x=10, y =110)

    alturaEntry = Entry(sanidadDatos)
    alturaEntry.place(x=90, y=110)

    pesoFloat = Label(sanidadDatos, text="Peso(kg):")
    pesoFloat.config(font=("Arial", 12), bg="bisque")
    pesoFloat.place(x=10, y=140)
    
    pesoEntry = Entry(sanidadDatos)
    pesoEntry.place(x=85, y=140 )
    # ------------- Botón Salir ------------
    btnSalir = Button(sanidadDatos, text="Salir", font=("Arial", 12), bg="red", fg="white", command=sanidadDatos.destroy)
    btnSalir.place(x=250, y=260)
    # ------ Función calcular -------
    def calcular2():
        eps = str(epsEntry.get())
        peso = int(pesoEntry.get())
        altura = int(alturaEntry.get())
    boton2Calcular = Button(sanidadDatos, text="Calcular", font=("Arial", 12), bg="green", fg="white", command=calcular2)
    boton2Calcular.place(x=350, y=260)


ing_Notas = Button(ventana_Principal, text="Ingresar notas", command=ingNotas)
ing_Notas.config(font=("Arial", 12),height=1, width=25 )
ing_Notas.place(x=200, y=250)

ing_Datos = Button(ventana_Principal, text="Ingresar datos personales", command=ingDatosdf)
ing_Datos.config(font=("Arial", 12), height=1, width=25)
ing_Datos.place(x=200, y =150)

ing_Salud = Button(ventana_Principal, text="Datos de sanidad", command=ingSanidad)
ing_Salud.config(font=("Arial", 12),height=1, width=25 )
ing_Salud.place(x=200, y=350)

ventana_Principal.mainloop()
#ventana__Principal.mainloop()