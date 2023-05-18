# Programa que recibe los datos de un estudiante y calcula la nota definitiva de una materia y su IMC

# Se importa tkinter y sus funciones
import tkinter as tk
from tkinter import messagebox, ttk, Tk
from tkinter import *

# Se declara la variable correspondiente a la ventana principal
ventana_Principal = Tk()
ventana_Principal.config(bg="white")
ventana_Principal.geometry("600x700")
ventana_Principal.resizable(False, False)
ventana_Principal.title("Andrés Felipe García Solano")

label1= Label(ventana_Principal, text="Calculadora de nota definitiva e IMC")
label1.config(font=("Arial", 16), bg="white")
label1.place(x=150, y =10)


ing_Salir = Button(ventana_Principal, text="Salir", command=ventana_Principal.destroy)
ing_Salir.config(font=("Arial", 12),height=1, width=25 )
ing_Salir.place(x=200, y=450)

salud = PhotoImage(file="./img/salud.png")
colegio = PhotoImage(file="./img/colegio.png")
sistemas = PhotoImage(file="./img/sistemas.png")
datosss = PhotoImage(file="./img/datosss1.png")
logoSistemas = Label(ventana_Principal)
logoSistemas.config(image=sistemas, bg="white")
logoSistemas.place(x=475, y=500)

def ingDatosdf():
    datosPersonales = Toplevel()
    datosPersonales.geometry("600x300")
    datosPersonales.resizable(False, False)
    datosPersonales.title("Calculadora de nota definitiva e IMC")
    datosPersonales.config(bg="white")
    labelDatos = Label(datosPersonales)
    labelDatos.config(image=datosss, bg="white")
    labelDatos.place(x=350,y=60)
    #--------------- Nombre --------------
    labNombre = Label(datosPersonales, text="Nombre:")
    labNombre.config(font=("Arial", 12), bg="white")
    labNombre.place(x =20, y =60)
    nombre = Entry(datosPersonales)
    nombre.config(bg="white", font=("Arial",12,) ,width=18)
    nombre.focus_set()
    nombre.place(x=125, y=60)
    # ------------- Edad -------------
    labEdad = Label(datosPersonales,text = "Edad:")
    labEdad.config(font=("Arial", 12), bg="white")
    labEdad.place(x=20 ,y=95)
    edadent = Entry(datosPersonales)
    edadent.config(bg="white", font=("Arial",12,) ,width=18)
    edadent.focus_set()
    edadent.place(x=125, y=95)
    # ------------ Grado ------------
    labGrado = Label(datosPersonales,text = "Grado:")
    labGrado.config(font=("Arial", 12), bg="white")
    labGrado.place(x=20 ,y=130)
    gradoent = Entry(datosPersonales)
    gradoent.config(bg="white", font=("Arial",12,) ,width=18)
    gradoent.focus_set()
    gradoent.place(x=125, y=130)
    # --------- Identificación ----------
    labIdent = Label(datosPersonales,text = "Identificación:")
    labIdent.config(font=("Arial", 12), bg="white")
    labIdent.place(x=20 ,y=160)
    idenent = Entry(datosPersonales)
    idenent.config(bg="white", font=("Arial",12,) ,width=18)
    idenent.focus_set()
    idenent.place(x=125, y=160)
    # --------- Teléfono ------------
    labTelef = Label(datosPersonales,text = "Teléfono:")
    labTelef.config(font=("Arial", 12), bg="white")
    labTelef.place(x=20 ,y=190)
    idTelef = Entry(datosPersonales)
    idTelef.config(bg="white", font=("Arial",12,) ,width=18)
    idTelef.focus_set()
    idTelef.place(x=125, y=190)
    # ------------ Sede -----------
    labSede = Label(datosPersonales,text = "Sede:")
    labSede.config(font=("Arial", 12), bg="white")
    labSede.place(x=20 ,y=220)
    combo=ttk.Combobox(datosPersonales,state="reandonly",values =["A", "B", "C", "D", "E"])
    combo.place(x=125, y =220)
    combo.config(width=19)
    labDat = Label(datosPersonales, text="Datos Personales")
    labDat.config(font=("Arial", 16), bg="white")
    labDat.place(x =200, y =20)
    # ------------- Botón Salir ------------
    btnSalir = Button(datosPersonales, text="Salir", font=("Arial", 12), bg="red", fg="white", command=datosPersonales.destroy)
    btnSalir.place(x=280, y=260)



def ingNotas():
    notasPersonales = Toplevel()
    notasPersonales.geometry("600x300")
    notasPersonales.resizable(False, False)
    notasPersonales.title("Calculadora de nota definitiva e IMC")
    notasPersonales.config(bg="white")
    labelColegio = Label(notasPersonales)
    labelColegio.config(image=colegio, bg="white")
    labelColegio.place(x=350,y=60)
    academica = Label(notasPersonales, text="Información académica")
    academica.config(bg="white", font=("Arial", 16))
    academica.place(x =200, y =15)

    # ------------ Materia-----------
    materiaLabel = Label(notasPersonales,text = "Materia:")
    materiaLabel.config(font=("Arial",12), bg ="white")
    materiaLabel.place(x =10, y=80)
    materiaCombo = ttk.Combobox(notasPersonales, state="reandonly", values=["Matemáticas", "Sociales", "Filosofía", "Religión", "Español", "Química", 
                                                                           "Física","Inglés", "Ciencias Políticas", "Artística", "Especialidad", "Estadística"])
    materiaCombo.place(x=165, y=80)
    materiaCombo.config(width=19)
    # ------------ Nota Cognitiva --------------
    notaCognitiva = Label(notasPersonales, text="Nota cognitiva:")
    notaCognitiva.config(font=("Arial", 12), bg ="white")
    notaCognitiva.place(x =10, y=110)
    entry_cog = Entry(notasPersonales)
    entry_cog.place(x=165, y=113)

    # ------------ Nota Procedimental --------------
    notaProcedimental = Label(notasPersonales, text="Nota procedimental:")
    notaProcedimental.config(font=("Arial", 12), bg ="white")
    notaProcedimental.place(x =10, y=140)
    entry_proce = Entry(notasPersonales)
    entry_proce.place(x=165, y=140)
    # ------------ Nota Actitudinal --------------
    notaActitudinal = Label(notasPersonales, text="Nota actitudinal:")
    notaActitudinal.config(font=("Arial", 12), bg ="white")
    notaActitudinal.place(x =10, y=173)
    entry_acti = Entry(notasPersonales)
    entry_acti.place(x=165, y=173)
    # ------------ Nota Autoevaluación --------------
    notaAutoevalu = Label(notasPersonales, text="Nota autoevaluación:")
    notaAutoevalu.config(font=("Arial", 12), bg ="white")
    notaAutoevalu.place(x =10, y=203)
    entry_auto = Entry(notasPersonales)
    entry_auto.place(x=165, y=203)
    # ------------ Nota Bimestral --------------
    notaBimestral = Label(notasPersonales, text="Nota bimestral:")
    notaBimestral.config(font=("Arial", 12), bg ="white")
    notaBimestral.place(x =10, y=233)
    entry_bime = Entry(notasPersonales)
    entry_bime.place(x=165, y=233)
    # ------------- Botón Salir ------------
    btnSalir = Button(notasPersonales, text="Salir", font=("Arial", 12), bg="red", fg="white", command=notasPersonales.destroy)
    btnSalir.place(x=250, y=260)
    # ------ Función calcular-------


# convertir
    def convertir():
        messagebox.showinfo("Nota Definitiva", "Operación realizada")

        # variables notas

        entry_proce_def = float(entry_proce.get())
        entry_cog_def = float(entry_cog.get())
        entry_autoe_def = float(entry_auto.get())
        entry_acti_def = float(entry_acti.get())
        entry_bime_def = float(entry_bime.get())

        entry_not_final = (0.3*entry_proce_def) + (0.3*entry_cog_def) + (0.1*entry_autoe_def) + (0.1*entry_acti_def) + (0.2*entry_bime_def)

        if entry_not_final < 30:
                messagebox.showinfo("Resultado", "El alumno reprobó la asignatura, su nota es: "+ str(entry_not_final))
        else:
                messagebox.showinfo("Resultado", "El alumno aprobó la asignatura, su nota es : "+str(entry_not_final))
    boton1Calcular = Button(notasPersonales, text="Calcular", font=("Arial", 12), bg="green", fg="white", command=convertir)
    boton1Calcular.place(x=350, y=260)
 
    boton1Calcular = Button(notasPersonales, text="Calcular", font=("Arial", 12), bg="green", fg="white", command=convertir)
    boton1Calcular.place(x=350, y=260)

def ingSanidad():
    sanidadDatos = Toplevel()
    sanidadDatos.geometry("600x300")
    sanidadDatos.resizable(False, False)
    sanidadDatos.title("Calculadora de nota definitiva e IMC")
    sanidadDatos.config(bg="white")
    saludLabel = Label(sanidadDatos)
    saludLabel.config(image=salud, bg="white")
    saludLabel.place(x=350, y=60)



    textoSalud = Label(sanidadDatos, text="Datos de Sanidad")
    textoSalud.config(font=("Arial", 16), bg="white")
    textoSalud.place(x=225, y=15)

    epsStr = Label(sanidadDatos, text="EPS:")
    epsStr.config(font=("Arial", 12), bg="white")
    epsStr.place(x=10, y =80)
    epsEntry = Entry(sanidadDatos)
    epsEntry.place(x=90, y=80)

    alturaFloat = Label(sanidadDatos, text="Altura(mt):")
    alturaFloat.config(font=("Arial", 12), bg="white")
    alturaFloat.place(x=10, y =110)

    alturaEntry = Entry(sanidadDatos)
    alturaEntry.place(x=90, y=110)

    pesoFloat = Label(sanidadDatos, text="Peso(kg):")
    pesoFloat.config(font=("Arial", 12), bg="white")
    pesoFloat.place(x=10, y=140)
    
    pesoEntry = Entry(sanidadDatos)
    pesoEntry.place(x=90, y=140 )
    # ------------- Botón Salir ------------
    btnSalir = Button(sanidadDatos, text="Salir", font=("Arial", 12), bg="red", fg="white", command=sanidadDatos.destroy)
    btnSalir.place(x=250, y=260)
    # ------ Función calcular -------
    def convertir_imc ():
        estatura = float(alturaEntry.get())
        peso = float(pesoEntry.get())
        imc = peso / estatura**2
      
        if imc < 16:
            messagebox.showinfo("Resultado","Su imc corresponde a delgadez severa")
        elif imc < 17:
            messagebox.showinfo("Resultado","Su imc corresponde a delgadez moderada")
        elif imc < 18.5:
            messagebox.showinfo("Resultado","Su imc corresponde a delgadez ligera")
        elif imc < 25:
            messagebox.showinfo("Resultado","Su imc corresponde a Saludable")
        elif imc < 30:
            messagebox.showinfo("Resultado","Su imc corresponde a Sobrepeso")
        elif imc < 35:
            messagebox.showinfo("Resultado","Su imc corresponde a Obesidad grado I")
        elif imc < 40:
            messagebox.showinfo("Resultado","Su imc corresponde a Obesidad grado II (grave)")
        else:
            messagebox.showinfo("Resultado","Su imc corresponde a Obesidad grado III (mórbida)")
    boton3Calcular = Button(sanidadDatos, text="Calcular", font=("Arial", 12), bg="green", fg="white", command=convertir_imc)
    boton3Calcular.place(x=350, y=260)




ing_Notas = Button(ventana_Principal, text="Nota definitiva", command=ingNotas)
ing_Notas.config(font=("Arial", 12),height=1, width=25 )
ing_Notas.place(x=200, y=250)

ing_Datos = Button(ventana_Principal, text="Ingresar datos personales", command=ingDatosdf)
ing_Datos.config(font=("Arial", 12), height=1, width=25)
ing_Datos.place(x=200, y =150)

ing_Salud = Button(ventana_Principal, text="IMC", command=ingSanidad)
ing_Salud.config(font=("Arial", 12),height=1, width=25 )
ing_Salud.place(x=200, y=350)

ventana_Principal.mainloop()
#ventana__Principal.mainloop()