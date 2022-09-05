from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from procesos.procesosGui import *
from dominio.entidades import *
from procesos.archivos import *
class EditStudent:

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
        self.cad = String()
        self.__getWindow(titulo)
        self.__getFrame()
        self.__getLabels()
        self.__getInputs()
        self.__getButtons()
        if obj!=None:
            self.__DataCharge(obj)
            self.cedula['state']='disabled'
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
        self.grabar = Button(self.ven,relief="flat",text="Actualizar",bg="green",
                      command=self.edit,
                      font=("Tahoma",16),fg="white",cursor="hand1")
        self.grabar.place(x=120,y=425,width=110,height=40)
        self.eliminar = Button(self.marco,relief="flat",text="Eliminar",bg="green",
                      command=self.delete,
                      font=("Tahoma",16),fg="white",cursor="hand1")
        self.eliminar.place(x=300,y=420,width=110,height=40)

        btn3 = Button(self.marco,relief="flat",text="Cancelar",bg="green",
                      command=self.ven.destroy,
                      font=("Tahoma",16),fg="white",cursor="hand1")\
            .place(x=460,y=420,width=110 ,height=40)


    def __DataCharge(self,obj):
        self.lista1=[" ","MATUTINA","VESPERTINA","NOCTURNA"]
        self.cedula.insert(0,obj.cedula)
        self.nombres.insert(0,obj.nombres)
        self.apellidos.insert(0,obj.apellidos)
        self.correo.insert(0,obj.correo)
        self.carrera.insert(0,obj.carrera)
        pos = self.cad.getPosCombo(obj.jornada,self.lista1)
        self.combo.set(self.lista1[pos])

    def edit(self):
        self.datos = self.arch.allStudents(self.ruta)
        posi = self.arch.getStudentPosition(self.cedula.get(),self.ruta)
        pos = self.combo.current()
        obj = Estudiante(self.cedula.get(),
                      self.nombres.get(),
                      self.apellidos.get(),
                      self.correo.get(),
                      self.carrera.get(),
                      self.lista[pos])
        self.datos[posi].cedula=obj.cedula
        self.datos[posi].nombres=obj.nombres
        self.datos[posi].apellidos=obj.apellidos
        self.datos[posi].correo=obj.correo
        self.datos[posi].carrera= obj.carrera
        self.datos[posi].jornada=obj.jornada
        msg = ""
        for i in range(len(self.datos)):
            msg=msg+self.datos[i].cedula+","+self.datos[i].nombres+","+self.datos[i].apellidos+","+\
                ","+self.datos[i].correo+","+self.datos[i].jornada+",\n"
        print(msg)
        """ 
        reg = obj. cedula+","+obj.nombres+","+obj.apellidos\
              +","+obj.correo+","+obj.carrera+","+ obj.jornada+",\n"
        print(reg)
        self.arch.create(self.ruta,reg,"a")
        """
        messagebox.showinfo("Actualizacion",
        "Su registro ha sido actualizado con exito!",
                            parent=self.ven)

    def delete(self):
       pass
       #messagebox.showinfo("Mensaje!", "Cedula ya existe!.", parent=self.ven)