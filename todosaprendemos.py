from tkinter import *

"""gui=Tk()
gui.title("Práctica ")
gui.geometry("400x400")
frameBotones=Frame(gui)
B1=Button(frameBotones,text="Preguntar").grid(row=0,column=0)
B2=Button(frameBotones,text="Reporte").grid(row=0,column=1)
B3=Button(frameBotones,text="Borrar").grid(row=0,column=2)
B4=Button(frameBotones,text="Leer encuesta").grid(row=0,column=3)
frameBotones.place(x=60, y=20, width=300, height=25)

gui.mainloop()"""

#si no se mete en funciones sale sobreescrito, por eso hay que meterlo en funciones, cada menu
gui=Tk()
gui.title(" INSTITUCIÓN EDUCATIVA TODOS APRENDEMOS")
gui.geometry("800x680")
textActividad=Entry(gui)
textTiempo=Entry(gui)
# frame es un espacio dentro del gui para ubicar un elemento
def menu1():
    labelBorrar=Label(gui,text="")
    labelBorrar.place(x=0, y=0, width=1000, height=1000)
    frameBotones=Frame(gui)
    B1=Button(frameBotones,text="Programas",command=programas).grid(row=0,column=0)
    B2=Button(frameBotones,text="Estudiantes \n Fonoaudiologia").grid(row=0,column=1)
    B3=Button(frameBotones,text="Estudiantes\n Tedesoft").grid(row=0,column=2)
    B4=Button(frameBotones,text="Reportes").grid(row=0,column=3)
    B5=Button(frameBotones,text="Mejores \n Estudiantes",command=menu2).grid(row=0,column=4)
    frameBotones.place(x=60, y=20, width=600, height=40)
    gui.update()
#actualiza la interfaz grafica gui.update

def menu2():
    labelBorrar=Label(gui,text="")
    labelBorrar.place(x=60, y=80, width=400, height=300)
    frameBotones2=Frame(gui)
    B12=Button(frameBotones2,text="2Programas").grid(row=0,column=0)
    B22=Button(frameBotones2,text="2Estudiantes \n Fonoaudiologia").grid(row=0,column=1)
    B32=Button(frameBotones2,text="2Estudiantes \n Tedesoft").grid(row=0,column=2)
    B42=Button(frameBotones2,text="2Reportes").grid(row=0,column=3)
    B52=Button(frameBotones2,text="2OMejores \n Estudiantes", command=menu1).grid(row=0,column=4)
    frameBotones2.place(x=60, y=20, width=400, height=25)
    gui.update()

def error():
    labelBorrar=Label(gui,text="")
    labelBorrar.place(x=60, y=80, width=400, height=300)
    errorLabel = Label(text="Error en el ingreso de los datos", bg="red")
    errorLabel.place(x=60, y=80, width=250, height=80)
    gui.update()
    
def updateEncuesta(nuevalinea):
    print("Actualizando encuesta")
    arrayLineas=[]
# enconding manejar caracteres especiales utf-8 es sintaxis
# [:-1:] quita el salto de linea
    with open("ANALISIS.txt", "r", encoding="utf-8") as f:
        for linea in f:
            arrayLineas.append(linea[:-1:])
    f.close()
    f=open("ANALISIS.txt", "w", encoding="utf-8")
    for j in arrayLineas:
        f.write(j+"\n")
    f.write(nuevalinea+"\n")
    f.close()
    
def ingresarEncuesta():
    actividad=int(textActividad.get())
    tiempo=int(textTiempo.get())
    print("Se ingresaran datos")
    print("Tiempo", tiempo)
    print("Actividad", actividad)
    if tiempo > 0 and tiempo <5 and actividad >0 and actividad < 6:
        updateEncuesta(str(tiempo)+","+str(actividad)+",")
    else:
        error()
    
#labelBorrar, sobreescribe, pone una página nueva sobre el gui hay que crear un campo para ingresar texto
    
def programas():
    labelBorrar=Label(gui,text="")
    labelBorrar.place(x=0, y=0, width=800, height=800)

    
    frameLabels1=Frame(gui)
    labelTdsof=Label(frameLabels1,text="TECNOLOGÍA EN DESARROLLO DE SOFTWARE").grid(row=1,column=1)
    frameLabels1.place(x=20, y=80, width=1300, height=600)

    frameLabels2=Frame(gui)
    labelFono=Label(frameLabels2,text="\n FONOAUDIOLOGÍA").grid(row=1,column=50)
    frameLabels2.place(x=500, y=70, width=1300, height=600)

    #labelTdsof2=Label(frameLabels1,text="SEMESTRES: 6 \n ASIGNATURAS: Matemáticas, programación, ingles").grid(row=3,column=1)

    frameImagesFono = Frame(gui)
    #frameImagesFono.pack(side=TOP, fill="x")
    frameImagesFono.picture = PhotoImage(file="pensumfono.png") # colocar imagen
    frameImagesFono.label=Label(frameImagesFono,image=frameImagesFono.picture)
    frameImagesFono.label.pack()
    frameImagesFono.place(x=420, y=120,width=281, height=435)

    frameImagesTede = Frame(gui)
    #frameImagesTede.pack(side=RIGHT, fill="x")
    frameImagesTede.picture = PhotoImage(file="pensumtdsof.gif") # colocar imagen
    frameImagesTede.label=Label(frameImagesTede,image=frameImagesTede.picture)
    frameImagesTede.label.pack()
    frameImagesTede.place(x=50, y=120,width=297, height=435)


    #labelFono2=Label(frameLabels2,text="SEMESTRES: 10 \n ASIGNATURAS: Matematicas, Ingles,Biologia").grid(row=3,column=50)
    #photo2=PhotoImage(file=".gif") #colocar imagen
   
    B6=Button(gui,text="Menú Principal", command=menu1)
    B6.place(x=300, y=600, width=100, height=50,)
    
    
    gui.update()

menu1()
gui.mainloop()

'''def programas():
    global textActividad
    global textTiempo
    labelBorrar=Label(gui,text="")
    labelBorrar.place(x=60, y=80, width=400, height=260)
    labelTiempo=Label(gui,text="Tiempo libre \n <1> Menos de 3 horas \n <2> Entre 3 y 6 horas\n <3> Entre 6 y 9 horas \n <4> Más de 9 horas")
    labelTiempo.place(x=100, y=80, width=150, height=80)
    textTiempo=Entry(gui)
    textTiempo.place(x=280, y=80, width=150, height=80)
    labelActividad=Label(gui,text="Actividad principal \n <1> Leer \n <2> Ver televisión \n <3> Hacer deporte \n <4> Dormir \n <5> Otra")
    labelActividad.place(x=100, y=200, width=150, height=100)
    textActividad=Entry(gui)
    textActividad.place(x=280, y=200, width=150, height=80)
    B6=Button(gui,text="Ingresar", command=ingresarEncuesta)
    B6.place(x=160, y=320, width=70, height=30)'''

