from tkinter import *
from procesos.procesosGui import *
from tkinter import messagebox
from vistas.newStudent import *
from vistas.gestionE import *
class MenuApp:

    def __init__(self,obU=None):
        self.imagen = 'C:/Users/josel/OneDrive/Escritorio/PROYECTOS_PYTHON/ProyectoD/img/python-poo.png'
        self.cv = ProcesosGui()
        titulo=''
        if obU!=None:
            self.usu = obU
            titulo="Usuario : "+obU.nombres+" "+obU.apellidos+"."
        self.__getWindow(titulo)
        self.__setImage(self.imagen,0,0,7,9)

    def __getWindow(self,titulo=None):
        self.ven = Tk()
        self.ven.title(titulo)
        self.cv.center(self.ven,1000,560)
        self.ven.config(bg="#CCCCFF")
        self.ven.resizable(0,0)

    def __setImage(self,ruta,x,y,tam,sub):
        img = PhotoImage(file=ruta)
        img = img.zoom(tam)
        img = img.subsample(sub)
        fondo = Label(self.ven,image=img).place(x=x,y=y)
        self.__getMenu()
        self.ven.mainloop()

    def __getMenu(self):
        self.menu = Menu(self.ven)
        self.ven.config(menu=self.menu)
        self.item1 = Menu(self.menu)
        self.menu.add_cascade(label="Archivo",menu=self.item1)
        self.item1.add_command(label="Registro nuevo",command=self.nuevo)
        self.item1.add_command(label="Gestion de estudiantes",command=self.gestion)
        self.item1.add_separator()
        self.item1.add_command(label="Factura")
        self.item1.add_command(label="Salir",command=self.ven.destroy)
        #segunda cascada
        self.item2= Menu(self.menu)
        self.menu.add_cascade(label="Ayuda",menu=self.item2)
        self.item2.add_command(label="About",command=self.about)


    def about(self):
        msg = "\tProyecto de Segundo D de POO\n\n" \
              "Este proyecto fue desarrollado por\n" \
              "estudiantes y docente de la materia de POO.\n" \
              "Carrera : Desarrollo de Software\n" \
              "Instituto: Instituto Superior Tecnologico Guayaquil."
        messagebox.showinfo("About", msg, parent=self.ven)


    def nuevo(self):
        nuev = NewStudent(self.usu)

    def gestion(self):
        gest = GestionEstudiantes(self.usu)
