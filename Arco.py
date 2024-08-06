from tkinter import *
from Punto import Punto

class Arco(Punto):
    def __init__(self, x=0, y=0, ancho=10, largo=10, gradoIni=0, gradoFin=90, color="black", delineado="black"):
        super().__init__(x,y,color,delineado)
        self.setAncho(ancho)
        self.setLargo(largo)
        self.setIni(gradoIni)
        self.setFin(gradoFin)    

    def setAncho(self, ancho):
        if ancho>0:
            self.__ancho = ancho
        else:
            self.__ancho = 0
    def setLargo(self, largo):
        if largo>0:
            self.__largo = largo
        else:
            self.__largo = 0

    def setIni(self,i):
        self.__ini=i

    def setFin(self,f):
        self.__fin=f                    

    def getAncho(self):
        return self.__ancho

    def getLargo(self):
        return self.__largo
    
    def getIni(self):
        return self.__ini
    
    def getFin(self):
        return self.__fin

    def dibuja(self, lienzo, tipo=0):
        if tipo==0:
            lienzo.create_arc(self.getX(),self.getY(),self.getAncho(),self.getLargo(), 
                              start = self.getIni(), extent = self.getFin(),outline = self.delineado, fill = self.color)
    #Prueba de distintos estilos de dibujar arcos
        elif tipo==1:
                lienzo.create_arc((10, 10), (200, 200), style=PIESLICE, width=2)
                lienzo.create_arc((10, 200), (200, 390), style=CHORD, width=2)
                lienzo.create_arc((10, 400), (200, 590), style=ARC, width=2)
    
    def mover(self, dx, dy):
        self.setX(self.getX() + dx)
        self.setY(self.getY() + dy)

    def __str__(self):
        return "Centro: " + super().__str__()+\
            "Ancho: " + str(self.__ancho) + " " +\
            "Largo: " + str(self.__largo) + " " +\
            "Grado: " +str(self.__ini)+"-"+str(self.__fin) + " "   
