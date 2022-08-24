from tkinter import *
from tkinter import  messagebox
from tkinter import ttk
from vistas.registro import *
from procesos.procesosGui import *
from procesos.archivos import *
from vistas.menuPrincipal import *
from vistas.newStudent import *
class GestionEstudiantes:

    def __init__(self,obj=None):
        self.clk= 0
        self.n_fila=[-1,-1]
        self.cad = String()
        titulo = ""
        if obj!=None:
            self.obU = obj
            titulo= "Usuario : "+obj.nombres+" "+obj.apellidos+"."
        self.ruta = 'C:/Users/sopor/PycharmProjects/ProyectoD/estudiantesD.csv'
        self.cv = ProcesosGui()
        self.arch = Archivo()
        self.datos= self.arch.allStudents(self.ruta)
        self.__getWindow()
        self.__getLabels()
        self.__getButtons()
        self.__getInputs()
        self.__showTable(self.datos)
        self.ven.mainloop()

    def __getWindow(self,titulo=None):
        self.ven = Toplevel()
        self.ven.title(titulo)
        self.cv.center(self.ven,1100,400)
        self.ven.config(bg="#CCCCFF")
        self.ven.resizable(0,0)

    def __getLabels(self):
        lb1 = Label(self.ven,fg="black", text="Gestion de estudiantes",
                    bg="#CCCCFF",font=("Tahoma",14)).place(x=480,
                                                          y=20)
        lb2 = Label(self.ven,fg="black", text="Ingrese la cedula:",
                    bg="#CCCCFF",font=("Arial",12)).place(x=280,
                                                          y=77)


    def __getInputs(self):
        validate = self.ven.register(self.validateId)
        self.cedula = Entry(self.ven, fg="blue", font=("Arial", 12),
                            validate="key",validatecommand=(validate,"%d","%S","%s"))
        self.cedula.place(x=450, y=80)


    def __getButtons(self):
        btn1 = Button(self.ven,relief="flat",text="Buscar",bg="green",
                      command=self.filtro,
                      font=("Tahoma",12),fg="white",cursor="hand1")\
            .place(x=680,y=77,width=90, height=25)
        btn2 = Button(self.ven,relief="flat",text="Cancelar",bg="green",
                      command=self.ven.destroy,
                      font=("Tahoma",12),fg="white",cursor="hand1")\
            .place(x=580,y=350,width=90)
        btn3 = Button(self.ven,relief="flat",text="Registrar",bg="green",
                      command=self.accion2,
                      font=("Arial",12),fg="white",cursor="hand1")\
            .place(x=460,y=350,width=90)


    def __showTable(self,lista1=None):
        self.tabla = ttk.Treeview(self.ven,columns=(1,2,3,4,5),
                     show="headings",height=8)
        self.tabla.bind("<1>",self.onClick)
        vsb= ttk.Scrollbar(self.ven,orient="vertical",command=self.tabla.yview)
        vsb.place(x=1058,y=120, height=190)
        self.tabla.configure(yscrollcommand=vsb.set)
        #estilo
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("Treeview.Heading",bg="0051C8")
        #Encabezado
        self.tabla.heading(1,text="CEDULA")
        self.tabla.heading(2,text="NOMBRES")
        self.tabla.heading(3,text="APELLIDOS")
        self.tabla.heading(4,text="CORREO")
        self.tabla.heading(5,text="CARRERA")

        self.tabla.column(1,anchor=CENTER)
        self.tabla.column(2,anchor=CENTER)
        self.tabla.column(3,anchor=CENTER)
        self.tabla.column(4,anchor=CENTER)
        self.tabla.column(5,anchor=CENTER)
        #llenado de datos
        for i in range(len(lista1)):
            self.tabla.insert("","end",values=(lista1[i].cedula,
                                               lista1[i].nombres,
                                               lista1[i].apellidos,
                              lista1[i].correo,lista1[i].carrera))
        self.tabla.place(x=55,y=120)

    def onClick(self,event):
        item = event.widget.identify("item",event.x,event.y)
        num = self.cad.getOnlyNumber(item)
        print(item,"Posicion",num)
        if num!="":
            self.clk +=1
            posi= int(num)
            if self.clk==1:
                self.n_fila[0]=posi
            if self.clk==2:
                self.n_fila[1]=posi
                self.clk=0
            if self.clk==0 and self.n_fila[0]==self.n_fila[1]:
                print("Formulario cargado")
        else:
            self.clk=0


    def filtro(self):
        self.datos= self.arch.getStudentFilter(self.cedula.get(),self.ruta)
        if self.datos!=[]:
            self.__showTable(self.datos)
            self.cedula.delete(0,END)
        else:
            self.datos= self.arch.allStudents(self.ruta)
            self.__showTable(self.datos)

    def accion2(self):
        reg = Registro(self.obU)

    def validateId(self,accion,car,texto):
        if accion!='1':
            return True
        return car in "1234567890" and len(texto)<10


#gest = GestionEstudiantes()



