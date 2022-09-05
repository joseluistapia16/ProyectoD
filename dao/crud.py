from dao.conexion import *
import mysql.connector as mc
from dominio.entidades import *
class CrudUsuario:
   def __init__(self):
       self.cone = Conexion()

   def insertUser(self,base,datos):
       msg=""
       try:
           con = self.cone.conectar(base)
           cursor1 = con.cursor()
           sql = "insert into usuario(usuario,pasword,nombres,apellidos,fecha,estado) "+\
                 "values(%s,%s,%s,%s,%s,%s)"
           cursor1.execute(sql,datos)
           con.commit()
           con.close()
           msg =str(cursor1.rowcount)+" registro(s) afectado(s)"
       except(mc.errors.IntegrityError) as ex:
         msg= str(ex)
       return msg

   def updateUser(self,base,datos):
       msg =""
       try:
           con = self.cone.conectar(base)
           cursor1= con.cursor()
           sql = "Update usuario set pasword=%s,nombres=%s, apellidos=%s "+\
               "where usuario=%s"
           cursor1.execute(sql,datos)
           con.commit()
           con.close()
           msg=str(cursor1.rowcount)+" registro(s) afectado(s)"
       except(mc.errors.IntegrityError) as ex:
           msg=str(ex)
       return msg

   def deleteUser(self,base, datos):
       msg = ""
       try:
           con = self.cone.conectar(base)
           cursor1= con.cursor()
           sql= "update usuario set estado=%s where usuario=%s"
           cursor1.execute(sql,datos)
           con.commit()
           con.close()
           msg = str(cursor1.rowcount) + " registro(s) afectado(s)"
       except(mc.errors.IntegrityError) as ex:
           msg=str(ex)
       return msg

   def getUser(self,base,datos):
       obj =None
       try:
           con = self.cone.conectar(base)
           cursor1= con.cursor()
           query="select * from usuario where usuario=%s"
           cursor1.execute(query,datos)
           result = cursor1.fetchall()
           con.close()
           if len(result)>0:
               obj = Usuario(result[0][0],result[0][1],result[0][2],result[0][3],
                             result[0][4],result[0][5])
       except:
           obj=None
       return obj

class CrudEstudiante:
    pass


crud = CrudUsuario()
"""
datos = ('maria2022',"maria123","Maria Belen","Rios Suarez",
         "2022-09-12","A")
print(crud.insertUser("segundod2022_1",datos))

datos=("55555","CARLOS MIGUEL","PERALTA VELEZ","luisa2000")
print(crud.updateUser("segundod2022_1",datos))

datos=("I","luisa2000")
print(crud.deleteUser("segundod2022_1",datos))
 """
datos=("luisa2000",)
obj = crud.getUser("segundod2022_1",datos)
if obj!=None:
    print(obj.nombres,obj.apellidos)
else:
    print("usuario no existe!")




