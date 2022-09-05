from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from procesos.procesosGui import *
from dominio.entidades import *
from procesos.archivos import *
class NewStudent:

    def __init__(self,obj=None):
        titulo = ""
        if obj!=None:
            self.obU = obj
            titulo="Usuario : "+obj.nombres + " "+obj.apellidos+"."
        self.lista=["MATUTINA","VESPERTINA","NOCTURNA"]
        self.fondo="#CCCCFF"
        self.ruta = 'C:/Users/josel/OneDrive/Escritorio/PROYECTOS_PYTHON/ProyectoD/estudiantesD.csv'
        self.arch = Archivo()
        self.cv = ProcesosGui()
        self.__getWindow(titulo)
        self.__getFrame()
        self.__getLabels()
        self.__getInputs()
        self.__getButtons()
        #self.ven.mainloop()

    def __getWindow(self,titulo=None):
        self.ven = Toplevel()
        self.ven.title(titulo)
        self.cv.center(self.ven,700,500)
        self.ven.config(bg=self.fondo)
        self.ven.resizable(0,0)


    def __getLabels(self):
        posX =120
        lb1 = Label(self.marco,fg="black", text="Registro de estudiantes",
                    bg=self.fondo,font=("Arial",18)).place(x=220,
                                                          y=30)
        lb2 = Label(self.marco,fg="black", text="Cedula",
                    bg=self.fondo,font=("Arial",18)).place(x=posX,
                                                          y=100)
        lb3 = Label(self.marco,fg="black", text="Nombres",
                    bg=self.fondo,font=("Arial",18)).place(x=posX,
                                                          y=150)
        lb4 = Label(self.marco,fg="black", text="Apellidos",
                    bg=self.fondo,font=("Arial",18)).place(x=posX,
                                                          y=200)
        lb5 = Label(self.marco,fg="black", text="Correo",
                    bg=self.fondo,font=("Arial",18)).place(x=posX,
                                                          y=250)
        lb6 = Label(self.marco,fg="black", text="Carrera",
                    bg=self.fondo,font=("Arial",18)).place(x=posX,
                                                          y=300)

        lb7 = Label(self.marco,fg="black", text="Jornada",
                    bg=self.fondo,font=("Arial",18)).place(x=posX,
                                                          y=350)



    def __getInputs(self):
        posX=350
        self.cedula = Entry(self.marco,font=("Tahoma",16))
        self.cedula.place(x=posX,y=100,width=180,height=25)
        self.nombres = Entry(self.marco,font=("Tahoma",16))
        self.nombres.place(x=posX,y=150,width=180,height=25)
        self.apellidos= Entry(self.marco,font=("Tahoma",16))
        self.apellidos.place(x=posX,y=200,width=180,height=25)
        self.correo= Entry(self.marco,font=("Tahoma",16))
        self.correo.place(x=posX,y=250,width=180,height=25)
        self.carrera= Entry(self.marco,font=("Tahoma",16))
        self.carrera.place(x=posX,y=300,width=180,height=25)
        self.combo = Combobox(self.marco,state='readonly',values=self.lista)
        self.combo.place(x=posX, y=350,height=30,width=180)



    def __getFrame(self):
        self.marco = Frame(self.ven,bd=5,bg=self.fondo)
        self.marco.pack(fill="both",expand=1)
        self.marco.config(cursor="pirate")
        self.marco.config(bd=5)
        self.marco.config(relief="groove")

    def __getButtons(self):
        btn1 = Button(self.marco,relief="flat",text="Buscar",bg="green",
                      command=self.accion1,
                      font=("Tahoma",16),fg="white",cursor="hand1")\
            .place(x=550,y=95,width=90,height=30)
        btn2 = Button(self.ven,relief="flat",text="Guardar",bg="green",
                      command=self.getData,
                      font=("Tahoma",16),fg="white",cursor="hand1")\
            .place(x=200,y=425,width=110,height=40)
        btn3 = Button(self.marco,relief="flat",text="Cancelar",bg="green",
                      command=self.ven.destroy,
                      font=("Tahoma",16),fg="white",cursor="hand1")\
            .place(x=360,y=420,width=110 ,height=40)


    def vaciar(self):
        self.cedula.delete(0,END)
        self.nombres.delete(0,END)
        self.apellidos.delete(0,END)
        self.correo.delete(0,END)
        self.carrera.delete(0,END)

    def getData(self):
        pos = self.combo.current()
        obj = Estudiante(self.cedula.get(),
                      self.nombres.get(),
                      self.apellidos.get(),
                      self.correo.get(),
                      self.carrera.get(),
                      self.lista[pos])
        reg = obj. cedula+","+obj.nombres+","+obj.apellidos\
              +","+obj.correo+","+obj.carrera+","+ obj.jornada+",\n"
        print(reg)
        self.arch.create(self.ruta,reg,"a")
        self.vaciar()
        messagebox.showinfo("Registro",
        "Su registro ha sido grabado con exito!",
                            parent=self.ven)



    def accion1(self):
        print("ruta",self.ruta)
        obj = self.arch.getStudent(self.cedula.get(),self.ruta)
        if obj!=None:
           messagebox.showinfo("Mensaje!", "Cedula ya existe!.", parent=self.ven)






