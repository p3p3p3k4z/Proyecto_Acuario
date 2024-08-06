from PuntoPixel import Punto

pezPixel = [
    [0,0,0,1,1,2,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,3,2,2,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,3,3,2,0,0,0,0,0],
    [0,0,0,0,0,1,3,3,2,2,2,0,0,0,0],
    [2,2,2,2,0,2,2,2,3,3,3,2,0,0,0],
    [0,1,3,3,2,3,3,3,3,2,2,3,2,2,0],
    [0,0,1,3,1,2,3,3,2,4,5,2,3,3,2],
    [0,0,1,2,1,3,2,3,2,4,4,2,3,2,1],
    [0,1,2,2,1,2,2,2,3,2,2,3,1,1,0],
    [1,1,1,1,0,1,2,2,2,2,2,1,0,0,0],
    [0,0,0,0,0,0,1,3,1,1,1,0,0,0,0],
    [0,0,0,0,0,0,0,1,2,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
]


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

class Pixel():
    def __init__(self, x, y, tam=5):
        self.__cordenada=Punto(x,y)
        self.tamano = tam
    
    def setCordenada(self, x, y):
        self.__cordenada.setX(x)
        self.__cordenada.setY(y)
        
    def getCordenada(self):
        return self.__cordenada
    
    def dibuja(self, lienzo, matriz, c1, c2, c3, c4):
        for i, fila in enumerate(matriz):
            for j, pixel in enumerate(fila):
                if pixel == 1:
                    self.color = c1
                elif pixel == 2:
                    self.color = c2
                elif pixel == 3:
                    self.color = c3
                elif pixel == 4:
                    self.color = c4
                elif pixel == 5:
                    self.color = "white"
                else:
                    self.color = ""

                lienzo.create_rectangle(j*self.tamano + self.getCordenada().getX(), i*self.tamano + self.getCordenada().getY(),
                                    j*self.tamano+self.tamano + self.getCordenada().getX(),
                                    i*self.tamano+self.tamano + self.getCordenada().getY(),
                                    outline = self.color, fill=self.color)
                
    def mover(self, dx, dy):
        self.setCordenada(self.getCordenada().getX() + dx, self.getCordenada().getY() + dy)
'''
from tkinter import *
ventana = Tk()
ventana.title("Pecera")
ventana.geometry("850x650")

lienzo = Canvas(ventana,width=850, height=650,bg ="cyan")
lienzo.pack()

verdeBajo = "#00D520"
verdeAmarillo = "#C4FF33"

def mover_estrella(event):
    if event.keysym == 'Up':
        p.mover(0, -5)
    elif event.keysym == 'Down':
        p.mover(0, 5)
    elif event.keysym == 'Left':
        p.mover(-5, 0)
    elif event.keysym == 'Right':
        p.mover(5, 0)
    lienzo.delete("all")
    p.dibuja(lienzo, pezPixel, "green", verdeBajo, verdeAmarillo, "black")

p = Pixel(100, 100,10)
p.dibuja(lienzo, pezPixel,"green", verdeBajo, verdeAmarillo, "black")

ventana.bind_all('<KeyPress>', mover_estrella)

ventana.mainloop()
'''