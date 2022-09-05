import mysql.connector as mc
class Conexion:

    def conectar(self,base):
        conect = None
        credencial = {
                    'host': 'localhost',
                    'port': '3306',
                    'user':'root',
                    'password':'1234',
                    'database':base,
                    'auth_plugin': 'mysql_native_password'
        }
        try:
            conect = mc.connect(**credencial)
        except(mc.errors.ProgrammingError,mc.errors.InterfaceError) as ex:
            print(str(ex))
        return conect


#obC = Conexion()
#print(obC.conectar("segundod2022_1"))
