from tkinter import *
class ProcesosGui:

    def center(self,objV,ancho,alto):
        v_alto = alto
        v_ancho = ancho
        ancho_screen = objV.winfo_screenwidth()
        alto_screen = objV.winfo_screenheight()
        x_coord = int((ancho_screen/2)-(v_ancho/2))
        y_coord = int((alto_screen/2)-(v_alto/2))
        objV.geometry('{}x{}+{}+{}'.format(v_ancho,v_alto,x_coord,y_coord))


class String:

    def getOnlyNumber(self,valor):
        msg = ""
        for i in range(1,len(valor)):
            msg = msg + valor[i]
        return msg

    def getPosCombo(self,valor,lista1):
        pos = -1
        for i in range(len(lista1)):
            if valor==lista1[i]:
                pos = i
                break
        return pos