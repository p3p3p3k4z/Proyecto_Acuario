from Punto import Punto

class Rectangulo(Punto):
    def __init__(self,x=0,y=0,b=0,h=0,color="black",delineado="black"):
        super().__init__(x,y,color,delineado)
        self.setBase(b)
        self.setAltura(h)
        
    def setBase(self,b):
        if b>0:
            self.__base=b
        else:
            self.__base=0
            
    def setAltura(self,h):
        if h>0:
            self.__altura=h
        else:
            self.__altura=0
            
    def getBase(self):
        return self.__base

    def getAltura(self):
        return self.__altura
    
    def dibuja(self, lienzo):
        lienzo.create_rectangle(self.getX(), self.getY(), 
                                self.getBase()+self.getX(), self.getAltura()+self.getY(),  
                                outline = self.delineado, fill=self.color)
    def mover(self, dx, dy):
        self.setX(self.getX() + dx)
        self.setY(self.getY() + dy)
    
    def __str__(self):
        return "Punto de referencia: " + super().__str__() + \
            "Base: " + str(self.__base) + " Altura: "+ str(self.__altura) + " "
'''   
from tkinter import *
ventana = Tk()
ventana.title("Pecera")
ventana.geometry("850x650")

lienzo = Canvas(ventana,width=850, height=650,bg ="cyan")
lienzo.pack()
p = Rectangulo(50,50,50,50,"blue","red")
p.dibuja(lienzo)
ventana.mainloop()
'''