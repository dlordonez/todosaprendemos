from tkinter import *


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
    B2=Button(frameBotones,text="Estudiantes \n Fonoaudiologia", command=EstudiantesFono).grid(row=0,column=1)
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
    B12=Button(frameBotones2,text="Programas").grid(row=0,column=0)
    B22=Button(frameBotones2,text="Estudiantes \n Fonoaudiologia").grid(row=0,column=1)
    B32=Button(frameBotones2,text="Estudiantes \n Tedesoft").grid(row=0,column=2)
    B42=Button(frameBotones2,text="Reportes").grid(row=0,column=3)
    B52=Button(frameBotones2,text="Mejores \n Estudiantes", command=menu1).grid(row=0,column=4)
    frameBotones2.place(x=60, y=20, width=400, height=25)
    gui.update()

def error():
    labelBorrar=Label(gui,text="")
    labelBorrar.place(x=60, y=80, width=400, height=300)
    errorLabel = Label(text="Error en el ingreso de los datos", bg="red")
    errorLabel.place(x=60, y=80, width=250, height=80)
    gui.update()

#cambioej    
    


    
#labelBorrar, sobreescribe, pone una página nueva sobre el gui hay que crear un campo para ingresar texto
    
def programas():
    labelBorrar=Label(gui,text="")
    labelBorrar.place(x=0, y=0, width=800, height=800)

    
    frameLabels1=Frame(gui)
    labelTdsof=Label(frameLabels1,text="TECNOLOGÍA EN DESARROLLO DE SOFTWARE").grid(row=1,column=1)
    frameLabels1.place(x=70, y=80, width=1300, height=600)

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

def EstudiantesFono():
    labelBorrar=Label(gui,text="")
    labelBorrar.place(x=0, y=0, width=800, height=800)
    frameBotones2=Frame(gui)
    agregar=Button(frameBotones2,text="Agregar").grid(row=0,column=0)
    editar=Button(frameBotones2,text="Editar").grid(row=0,column=1)
    eliminar=Button(frameBotones2,text="Eliminar").grid(row=0,column=2)
    volver=Button(frameBotones2,text="Volver", command=menu1).grid(row=0,column=3)
    frameBotones2.place(x=300, y=600, width=200, height=120)
    gui.update()


    

    
menu1()
gui.mainloop()

