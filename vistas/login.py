from tkinter import *
from tkinter import  messagebox
from vistas.registro import *
from procesos.procesosGui import *
from procesos.archivos import *
from vistas.menuPrincipal import *
class LoginD:

    def __init__(self,titulo=None):
        self.ruta = 'C:/Users/josel/OneDrive/Escritorio/PROYECTOS_PYTHON/ProyectoD/usuariosD.csv'
        self.cv = ProcesosGui()
        self.arch = Archivo()
        self.__getWindow()
        self.__getLabels()
        self.__getButtons()
        self.__getInputs()
        self.ven.mainloop()

    def __getWindow(self,titulo=None):
        self.ven = Tk()
        self.ven.title(titulo)
        self.cv.center(self.ven,460,355)
        self.ven.config(bg="#CCCCFF")
        self.ven.resizable(0,0)

    def __getLabels(self):
        lb1 = Label(self.ven,fg="black", text="Usuario",
                    bg="#CCCCFF",font=("Arial",18)).place(x=200,
                                                          y=50)
        lb2 = Label(self.ven,fg="black", text="Password",
                    bg="#CCCCFF",font=("Arial",18)).place(x=190,
                                                          y=150)


    def __getInputs(self):
        self.usuario = Entry(self.ven, fg="blue", font=("Tahoma", 18))
        self.usuario.place(x=100, y=100)
        self.password = Entry(self.ven, fg="blue", font=("Tahoma", 18))
        self.password.place(x=100, y=190)
        self.password.config(show="*")

    def __getButtons(self):
        btn1 = Button(self.ven,relief="flat",text="Aceptar",bg="green",
                      command=self.accion1,
                      font=("Tahoma",16),fg="white",cursor="hand1")\
            .place(x=105,y=255,width="110",height=40)
        btn2 = Button(self.ven,relief="flat",text="Cancelar",bg="green",
                      command=self.ven.destroy,
                      font=("Tahoma",16),fg="white",cursor="hand1")\
            .place(x=245,y=255,width="110",height=40)
        btn3 = Button(self.ven,relief="flat",text="Registrar",bg="green",
                      command=self.accion2,
                      font=("Arial",11),fg="white",cursor="hand1")\
            .place(x=340,y=25,width="110",height=25)

    def accion1(self):
        obj= self.arch.getObject(self.usuario.get(),self.ruta)
        if obj==None:
            messagebox.showinfo("Login","Usuario o password incorrectos!",parent=self.ven)
        else:
           self.ven.destroy()
           men = MenuApp(obj)



    def accion2(self):
        reg = Registro("Registro de Usuarios")






