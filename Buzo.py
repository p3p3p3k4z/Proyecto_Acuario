import time
from tkinter import *

from Punto import Punto
from Circulo import Circulo
from Triangulo import *
from Rectangulo import Rectangulo
from TrianguloRectangulo import *
from Arco import Arco

Turquesa = "#009999"
Cafe = '#775000'
CafeClaro = '#A97B1D'
AzulMarino = '#154360'
AzulOscuro = '#2E4053'
AzulVerdoso = '#148F77'
PurpuraOscuro = '#5B2C6F'
Vino = '#641E16'
verdeBajo = "#00D520"
verdeAmarillo = "#C4FF33"
verdeBajo = "#00D520"
verdeAmarillo = "#C4FF33"
purpuraOscuro = '#300089'

class Buzo:
    def __init__(self, x=0, y=0,tam=1,color1= Cafe,color2= CafeClaro):
        self.__cordenada=Punto(x,y)
        self.__tamano = tam
        self.__color1 = color1
        self.__color2 = color2
        
    def setCordenada(self, x, y):
        self.__cordenada.setX(x)
        self.__cordenada.setY(y)
        
    def getCordenada(self):
        return self.__cordenada
    
    def dibuja(self, lienzo):
        x = self.__cordenada.getX()
        y = self.__cordenada.getY()
        c1 = self.__color1
        c2 = self.__color2
        t = self.__tamano
        
        cabeza=Circulo(670*t+x,460*t+y,200*t,c1)
        cuello=Rectangulo(640*t+x,550*t+y,70*t,30*t,c2)
        orejaIzq=Arco(540*t+x,420*t+y,670*t+x,500*t+y,90,180,c2)
        orejaDer=Arco(800*t+x,420*t+y,670*t+x,500*t+y,270,180,c2)
        a=Circulo(670*t+x,460*t+y,120*t,c2)
        b=Circulo(670*t+x,460*t+y,90*t,'black')
        r1=Rectangulo(645*t+x,410*t+y,5*t,90*t,c2)
        r2=Rectangulo(690*t+x,410*t+y,5*t,90*t,c2)

        orejaIzq.dibuja(lienzo)
        orejaDer.dibuja(lienzo)
        cabeza.dibuja(lienzo)
        cuello.dibuja(lienzo)
        a.dibuja(lienzo)
        b.dibuja(lienzo)
        r1.dibuja(lienzo)
        r2.dibuja(lienzo)
        
    def cambiarTamano(self, tam):
        self.__tamano=tam
                    
    def cambiarColor(self, color1, color2):
        self.__color1 = color1
        self.__color2 = color2
        
    def mover(self, dx, dy):
        self.setCordenada(self.getCordenada().getX() + dx, self.getCordenada().getY() + dy)
        
"""   
ventana = Tk()
ventana.title("Pecera")
ventana.geometry("850x650")

lienzo = Canvas(ventana,width=850, height=650,bg ="cyan")
lienzo.pack()

p = Buzo(-500,-300,1.5,"red","green")
p.dibuja(lienzo)


ventana.mainloop()
"""