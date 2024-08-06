import time
from tkinter import *

from Punto import Punto
from Circulo import Circulo
from Triangulo import *
from Rectangulo import Rectangulo
from TrianguloRectangulo import *
from Arco import Arco

from Pixel import Pixel

estrella = [
    [0,0,0,0,0,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,2,1,0,0,0,0,0],
    [0,0,0,0,0,0,1,2,1,0,0,0,0,0],
    [0,0,0,0,0,1,3,3,3,1,0,0,0,0],
    [0,0,0,0,0,1,3,4,3,1,0,0,0,0],
    [0,1,1,1,3,3,3,3,3,3,1,1,1,0],
    [1,2,3,3,4,3,3,4,3,3,4,3,2,1],
    [0,1,2,3,3,3,3,3,3,3,3,2,1,0],
    [0,0,1,1,2,4,3,3,3,4,2,1,0,0],
    [0,0,0,0,1,2,3,4,3,3,1,0,0,0],
    [0,0,0,0,1,3,3,3,3,4,1,0,0,0],
    [0,0,0,1,4,3,2,1,2,3,3,1,0,0],
    [0,0,1,3,2,2,1,0,1,2,2,3,1,0],
    [0,1,2,2,1,1,0,0,0,1,1,3,3,1],
    [0,1,1,1,0,0,0,0,0,0,0,1,1,1],
]

alga = [
    [0,0,0,0,0,1,0],
    [0,0,0,0,1,1,0],
    [0,0,0,1,1,0,0],
    [0,1,1,0,0,0,0],
    [0,0,0,1,1,0,0],
    [0,1,1,0,0,0,0],
    [0,0,1,0,0,0,0],
    [0,1,1,0,0,0,0],
    [0,0,0,1,1,0,0],
    [0,0,0,0,1,1,0],
    
]

coral = [
    [0,0,0,1,1,0,0,0],
    [0,0,1,1,1,1,0,0],
    [0,1,1,1,1,1,1,0],
    [0,0,1,1,1,1,0,0],
    [0,0,0,1,1,0,0,0],
    ]

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
CafeArena= '#907031'

class Arrecife:
    def __init__(self, x=0, y=0,tam=1,color1= AzulOscuro,color2= AzulMarino):
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

        arr=Circulo(100*t+x,100*t+y,100*t,c1,c2)                 
        arr.dibuja(lienzo)
      
    def cambiarTamano(self, tam):
        self.__tamano=tam
                    
    def cambiarColor(self, color1, color2):
        self.__color1 = color1
        self.__color2 = color2
        
    def mover(self, dx, dy):
        self.setCordenada(self.getCordenada().getX() + dx, self.getCordenada().getY() + dy)

class Arena:
    def __init__(self, x=0, y=0,tam=1,color1= CafeArena):
        self.__cordenada=Punto(x,y)
        self.__tamano = tam
        self.__color1 = color1
        
    def setCordenada(self, x, y):
        self.__cordenada.setX(x)
        self.__cordenada.setY(y)
        
    def getCordenada(self):
        return self.__cordenada
    
    def dibuja(self, lienzo):
        x = self.__cordenada.getX()
        y = self.__cordenada.getY()
        c1 = self.__color1
        t = self.__tamano
         
        a=Rectangulo(0*t+x,500*t+y,850*t,650*t,c1)
        a.dibuja(lienzo)
      
    def cambiarTamano(self, tam):
        self.__tamano=tam
                    
    def cambiarColor(self, color1):
        self.__color1 = color1
        
    def mover(self, dx, dy):
        self.setCordenada(self.getCordenada().getX() + dx, self.getCordenada().getY() + dy)

class Alga:
    def __init__(self, x=0, y=0,tam=1,color1= Vino):
        self.__cordenada=Punto(x,y)
        self.__tamano = tam
        self.__color1 = color1
        
    def setCordenada(self, x, y):
        self.__cordenada.setX(x)
        self.__cordenada.setY(y)
        
    def getCordenada(self):
        return self.__cordenada
    
    def dibuja(self, lienzo):
        x = self.__cordenada.getX()
        y = self.__cordenada.getY()
        c1 = self.__color1
        t = self.__tamano
        
        l3=Pixel(100*t+x,100*t+y,5*t) 
        l3.dibuja(lienzo,alga,c1,"","","")
     
    def cambiarTamano(self, tam):
        self.__tamano=tam
                    
    def cambiarColor(self, color1, color2):
        self.__color1 = color1
        self.__color2 = color2
        
    def mover(self, dx, dy):
        self.setCordenada(self.getCordenada().getX() + dx, self.getCordenada().getY() + dy)
        
class Estrella:
    def __init__(self, x=0, y=0,tam=1,color1= "red",color2= "purple", color3="pink", color4="yellow"):
        self.__cordenada=Punto(x,y)
        self.__tamano = tam
        self.__color1 = color1
        self.__color2 = color2
        self.__color3 = color3
        self.__color4 = color4
        
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
        c3 = self.__color3
        c4 = self.__color4
        t = self.__tamano

        e=Pixel(110*t+x,100*t+y,2*t)
        e.dibuja(lienzo,estrella,c1,c2,c3,c4)
      
    def cambiarTamano(self, tam):
        self.__tamano=tam
                    
    def cambiarColor(self, color1, color2, color3, color4):
        self.__color1 = color1
        self.__color2 = color2
        self.__color3 = color3
        self.__color4 = color4
        
    def mover(self, dx, dy):
        self.setCordenada(self.getCordenada().getX() + dx, self.getCordenada().getY() + dy)
        
class Coral:
    def __init__(self, x=0, y=0,tam=1,color1= purpuraOscuro):
        self.__cordenada=Punto(x,y)
        self.__tamano = tam
        self.__color1 = color1
        
    def setCordenada(self, x, y):
        self.__cordenada.setX(x)
        self.__cordenada.setY(y)
        
    def getCordenada(self):
        return self.__cordenada
    
    def dibuja(self, lienzo):
        x = self.__cordenada.getX()
        y = self.__cordenada.getY()
        c1 = self.__color1
        t = self.__tamano
        
        c=Pixel(10*t+x,10*t+y,10*t)
        c.dibuja(lienzo,coral,c1,"","","")
      
    def cambiarTamano(self, tam):
        self.__tamano=tam
                    
    def cambiarColor(self, color1, color2):
        self.__color1 = color1
        self.__color2 = color2
        
    def mover(self, dx, dy):
        self.setCordenada(self.getCordenada().getX() + dx, self.getCordenada().getY() + dy) 

class Burbuja:
    def __init__(self, x=0, y=0,tam=1,grosor=2,color1= "pink"):
        self.__cordenada=Punto(x,y)
        self.__tamano = tam
        self.__color1 = color1
        self.__grosor = grosor
        
    def setCordenada(self, x, y):
        self.__cordenada.setX(x)
        self.__cordenada.setY(y)
        
    def getCordenada(self):
        return self.__cordenada
    
    def dibuja(self, lienzo):
        x = self.__cordenada.getX()
        y = self.__cordenada.getY()
        c1 = self.__color1
        g=self.__grosor
        t = self.__tamano
        
        b=Circulo(100*t+x,100*t+y,20*t,"",c1,g)
        b.dibuja(lienzo)
      
    def cambiarTamano(self, tam):
        self.__tamano=tam
                    
    def cambiarColor(self, color1, color2):
        self.__color1 = color1
        self.__color2 = color2
        
    def mover(self, dx, dy):
        self.setCordenada(self.getCordenada().getX() + dx, self.getCordenada().getY() + dy)

class Esponja:
    def __init__(self, x=0, y=0,tam=1,color1= "yellow",color2= "blue"):
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

        es=Rectangulo(100*t+x,100*t+y,100*t,100*t,c1,c1)
        p1=Rectangulo(120*t+x,125*t+y,5*t,5*t,c2,c2)
        p2=Rectangulo(130*t+x,145*t+y,5*t,5*t,c2,c2)
        p3=Rectangulo(180*t+x,115*t+y,5*t,5*t,c2,c2)
        p4=Rectangulo(170*t+x,165*t+y,5*t,5*t,c2,c2)
        p5=Rectangulo(150*t+x,185*t+y,5*t,5*t,c2,c2)
        es.dibuja(lienzo)
        p1.dibuja(lienzo)
        p2.dibuja(lienzo)
        p3.dibuja(lienzo)
        p4.dibuja(lienzo)
        p5.dibuja(lienzo)
      
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
p = Arrecife()
p.dibuja(lienzo)

d = Arena()
d.dibuja(lienzo)

c= Coral()
c.dibuja(lienzo)

e = Estrella()
e.dibuja(lienzo)

a = Alga()
a.dibuja(lienzo)

b=Burbuja()
b.dibuja(lienzo)

es=Esponja()
es.dibuja(lienzo)

ventana.mainloop()
'''