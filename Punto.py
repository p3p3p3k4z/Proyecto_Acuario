#Punto.py
from Figura import Figura

class Punto(Figura):
    def __init__(self, x=0, y=0, color="black", delineado="black"):
        self.setX(x)
        self.setY(y)
        self.color = color
        self.delineado = delineado

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def dibuja(self, lienzo):
        lienzo.create_oval(self.__x, self.__y,
        self.__x+3 , self.__y+3 , outline = self.delineado,
                           fill=self.color)
    def mover(self, dx, dy):
        self.setX(self.getX() + dx)
        self.setY(self.getY() + dy)

    def __str__(self):
        return "[" + str(self.__x) + \
           ", " + str(self.__y) + "] "
'''
from tkinter import *
ventana = Tk()
ventana.title("Pecera")
ventana.geometry("850x650")

lienzo = Canvas(ventana,width=850, height=650,bg ="cyan")
lienzo.pack()
p = Punto(50,50,"red")
p.dibuja(lienzo)
ventana.mainloop()
'''