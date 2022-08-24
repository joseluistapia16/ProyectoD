class Usuario:

    def __init__(self,*param):
        self.usuario= param[0]
        self.password= param[1]
        self.nombres= param[2]
        self.apellidos=param[3]
        self.correo = param[4]
        self.profesion= param[5]

class Estudiante:

    def __init__(self,*param):
        self.cedula= param[0]
        self.nombres= param[1]
        self.apellidos = param[2]
        self.correo = param[3]
        self.carrera = param[4]
        self.jornada = param[5]