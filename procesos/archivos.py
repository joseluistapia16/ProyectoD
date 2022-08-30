from dominio.entidades import *
class Archivo:

    def create(self,ruta, registro,modo):
        archivo = open(ruta,modo)
        archivo.write(registro)
        archivo.close()

    def allUsers(self,ruta):
        lista = []
        try:
            archivo = open(ruta,"r")
            for i in archivo.readlines():
                tupla = i.split(",")
                obj = Usuario(tupla[0],tupla[1],tupla[2],
                              tupla[3],tupla[4],tupla[5])
                lista.append(obj)
            archivo.close()
        except:
            print("Error...")
        return lista

    def getObject(self,user, ruta):
        lista= self.allUsers(ruta)
        obj=None
        for i in range(len(lista)):
            if user == lista[i].usuario:
                obj= lista[i]
                break
        return obj

    def allStudents(self,ruta):
        lista = []
        try:
            archivo = open(ruta,"r")
            for i in archivo.readlines():
                tupla = i.split(",")
                obj = Estudiante(tupla[0],tupla[1],tupla[2],
                              tupla[3],tupla[4],tupla[5])
                lista.append(obj)
            archivo.close()
        except:
            print("Error...")
        return lista

    def getStudent(self,id, ruta):
        lista= self.allStudents(ruta)
        obj=None
        for i in range(len(lista)):
            if id == lista[i].cedula:
                obj= lista[i]
                break
        return obj

    def getStudentFilter(self,id, ruta):
        lista= self.allStudents(ruta)
        res=[]
        for i in range(len(lista)):
            if id == lista[i].cedula:
                res.append(lista[i])
        return res

    def getStudentPosition(self,id, ruta):
        lista= self.allStudents(ruta)
        pos=-1
        for i in range(len(lista)):
            if id == lista[i].cedula:
                pos= i
                break
        return pos


