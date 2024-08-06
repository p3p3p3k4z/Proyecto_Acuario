from Triangulo import Triangulo

class TrianguloRectanguloIzq(Triangulo):
    def __init__(self, x=0, y=0, ancho=10, alto=10, color="black",delineado="black"):
        super().__init__(x, y, ancho, alto, color, delineado)

    def dibuja(self, lienzo):
        lienzo.create_polygon(self.getX() + self.getAncho(), self.getY(),
                                self.getX()+self.getAncho(),self.getY()+self.getAltura(),
                                self.getX(), self.getY()+self.getAltura(),
                                outline = self.delineado, fill=self.color)
    def mover(self, dx, dy):
        self.setX(self.getX() + dx)
        self.setY(self.getY() + dy)

    def __str__(self):
        return super().__str__()
        
class TrianguloRectanguloIzqInvertido(Triangulo):
    def __init__(self, x=0, y=0, ancho=10, alto=10, color="black", delineado="black"):
        super().__init__(x, y, ancho, alto, color, delineado)

    def dibuja(self, lienzo):
        lienzo.create_polygon(self.getX(), self.getY(),
                                self.getX()+self.getAncho(),self.getY()+self.getAltura(),
                                self.getX()+self.getAncho(), self.getY(),
                                outline = self.delineado, fill=self.color)

    def mover(self, dx, dy):
        self.setX(self.getX() + dx)
        self.setY(self.getY() + dy)

    def __str__(self):
        return super().__str__()
        
class TrianguloRectanguloDer(Triangulo):
    def __init__(self, x=0, y=0, ancho=10, alto=10, color="black",delineado="black"):
        super().__init__(x, y, ancho, alto, color,delineado)

    def dibuja(self, lienzo):
        lienzo.create_polygon(self.getX(), self.getY(),
                                self.getX()+self.getAncho(),self.getY()+self.getAltura(),
                                self.getX(), self.getY()+self.getAltura(),
                                outline = self.delineado, fill=self.color)

    def mover(self, dx, dy):
        self.setX(self.getX() + dx)
        self.setY(self.getY() + dy)

    def __str__(self):
        return super().__str__()

class TrianguloRectanguloDerInvertido(Triangulo):
    def __init__(self, x=0, y=0, ancho=10, alto=10, color="black",delineado="black"):
        super().__init__(x, y, ancho, alto, color, delineado)

    def dibuja(self, lienzo):
        lienzo.create_polygon(self.getX(), self.getY()+self.getAltura(),
                                self.getX(),self.getY(),
                                self.getX()+self.getAncho(), self.getY(),
                                outline = self.delineado, fill=self.color)

    def mover(self, dx, dy):
        self.setX(self.getX() + dx)
        self.setY(self.getY() + dy)

    def __str__(self):
        return super().__str__()
'''        	
from tkinter import * 
ventana = Tk()
ventana.title("Pecera")
ventana.geometry("850x650")

lienzo = Canvas(ventana,width=850, height=650,bg ="cyan")
lienzo.pack()

tr=TrianguloRectanguloIzq(150,350,50,40,"red")
tr.dibuja(lienzo)

tr1=TrianguloRectanguloIzqInvertido(100,350,50,40,"green")
tr1.dibuja(lienzo)

tr2=TrianguloRectanguloDer(100,350,50,40,"blue")
tr2.dibuja(lienzo)

tr3=TrianguloRectanguloDerInvertido(150,350,50,40)
tr3.dibuja(lienzo)

ventana.mainloop()
'''
