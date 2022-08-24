from dominio.imagen import *
from tkinter import *
from vistas.login import *
class Prueba:

    def __init__(self):
        self.__getWindow()
        self.__showImages()

    def __getWindow(self):
        self.root = Tk()
        self.root.geometry("1000x600")

    def __showImages(self):
        ruta = "C:/Users/sopor/PycharmProjects/ProyectoC/img/pizza.png"
        ruta1 = 'C:/Users/sopor/PycharmProjects/ProyectoD/java.png'
        ruta2 = 'C:/Users/sopor/PycharmProjects/ProyectoD/carro.png'
        im = PhotoImage(file=ruta2)
        obj = Imagenes(im, 10, 10)
        im = PhotoImage(file=ruta)
        obj1 = Imagenes(im, 200, 300)
        lista = [obj, obj1]
        self.__getImage(lista)


    def __getImage(self,img):
        for i  in range(len(img)):
            im= img[i].imagen
            foto = Label(self.root,image=im).\
                place(x=img[i].posX,y=img[i].posY)
        self.root.mainloop()


    def __setImage(self,ruta,x,y,tam):
        #imgpath = 'C:/Users/sopor/PycharmProjects/ProyectoD/java.png'
        imgpath=ruta
        img = PhotoImage(file=imgpath)
        img = img.zoom(tam) #with 250, I ended up running out of memory
        img = img.subsample(32) #mechanically, here it is adjusted to 32 instead of 320
        panel = Label(self.root, image = img).place(x=x,y=y)
        self.root.mainloop()


if __name__ == '__main__':
    ob = LoginD("SEGUNDO D")
    print("Hola como vamos")