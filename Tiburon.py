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

class Tiburon:
    def __init__(self, x=0, y=0,tam=1,color1= Turquesa,color2= "yellow"):
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
        cuerpo=TrianguloRectanguloDer((200 + x) * t, (100 + y) * t, 130 * t, 100 * t, c1, c1)
        cuerpo.dibuja(lienzo)
        cuerpo1=Rectangulo((200 + x) * t, (200 + y) * t, 130 * t, 60 * t, c1, c1)
        cuerpo1.dibuja(lienzo)
        cabeza= TrianguloDer((325 + x) * t, (198 + y) * t, 30 * t, 40 * t, c1, c1)
        cabeza.dibuja(lienzo)
        aleta=TrianguloIzq((160 + x) * t, (150 + y) * t, 40 * t, 70 * t, c1, c1)
        aleta.dibuja(lienzo)
        aleta1=TrianguloDer((130 + x) * t, (155 + y) * t, 30 * t, 60 * t, c2, c1)
        aleta1.dibuja(lienzo)
        aletap=Arco((200 + x) * t, (180 + y) * t, (280 + x) * t, (250 + y) * t, 270 , 90 , c2)
        aletap.dibuja(lienzo)
        ojo=Circulo((310 + x) * t, (210 + y) * t, 10 * t, "white", "black", 3*t)
        ojo.dibuja(lienzo)
                    
    def cambiarTamano(self, tam):
        self.__tamano=tam
                    
    def cambiarColor(self, color1, color2):
        self.__color1 = color1
        self.__color2 = color2
        
    def mover(self, dx, dy):
        self.setCordenada(self.getCordenada().getX() + dx, self.getCordenada().getY() + dy)

'''
ventana = Tk()
ventana.title("Pecera")
ventana.geometry("850x650")

lienzo = Canvas(ventana,width=850, height=650,bg ="cyan")
lienzo.pack()

p = Tiburon(10,10,1,"red","green")
p.dibujarTiburon(lienzo)

ventana.mainloop()
'''