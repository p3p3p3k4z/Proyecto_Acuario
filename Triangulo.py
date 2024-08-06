from Punto import Punto

class Triangulo(Punto):
    def __init__(self, x=0, y=0, ancho=10, alto=10, color="black", delineado="black"):
        super().__init__(x, y, color, delineado)
        self.setAncho(ancho)
        self.setAlto(alto)

    def setAncho(self, ancho):
        if ancho>0:
            self.__ancho = ancho
        else:
            self.__ancho = 0

    def setAlto(self, alto):
        if alto>0:
            self.__alto = alto
        else:
            self.__alto = 0

    def getAncho(self):
        return self.__ancho

    def getAltura(self): return self.__alto    

    def dibuja(self, lienzo):
        lienzo.create_polygon(self.getX() + self.__ancho//2, self.getY(),
                                self.getX()+self.__ancho,self.getY()+self.__alto,
                                self.getX(), self.getY()+self.__alto,
                                outline = self.delineado, fill=self.color)

    def mover(self, dx, dy):
        self.setX(self.getX() + dx)
        self.setY(self.getY() + dy)

    def __str__(self):
        return "Referencia: " + super().__str__()+\
            "Ancho: " + str(self.__ancho) + " "+\
            "Largo: " + str(self.__alto) + " "

class TrianguloInvertido(Punto):
    def __init__(self, x=0, y=0, ancho=10, alto=10, color="black", delineado="black"):
        super().__init__(x, y, color, delineado)
        self.setAncho(ancho)
        self.setAlto(alto)

    def setAncho(self, ancho):
        if ancho>0:
            self.__ancho = ancho
        else:
            self.__ancho = 0

    def setAlto(self, alto):
        if alto>0:
            self.__alto = alto
        else:
            self.__alto = 0

    def getAncho(self):
        return self.__ancho

    def getAltura(self): return self.__alto    

    def dibuja(self, lienzo):
        lienzo.create_polygon(self.getX()+ self.__ancho//2, self.getY()+self.getAltura(),
                                self.getX(),self.getY(),
                                self.getX()+self.getAncho(), self.getY(),
                                outline = self.delineado, fill=self.color)

    def mover(self, dx, dy):
        self.setX(self.getX() + dx)
        self.setY(self.getY() + dy)
        
    def __str__(self):
        return "Referencia: " + super().__str__()+\
            "Ancho: " + str(self.__ancho) + " "+\
            "Largo: " + str(self.__alto) + " "

class TrianguloDer(Punto):
    def __init__(self, x=0, y=0, ancho=10, alto=10, color="black", delineado="black"):
        super().__init__(x, y, color, delineado)
        self.setAncho(ancho)
        self.setAlto(alto)

    def setAncho(self, ancho):
        if ancho>0:
            self.__ancho = ancho
        else:
            self.__ancho = 0

    def setAlto(self, alto):
        if alto>0:
            self.__alto = alto
        else:
            self.__alto = 0

    def getAncho(self):
        return self.__ancho

    def getAltura(self): return self.__alto    

    def dibuja(self, lienzo):
        lienzo.create_polygon(self.getX(), self.getY(),
                                self.getX()+self.getAncho(),self.getY()+self.__alto//2,
                                self.getX(), self.getY()+self.getAltura(),
                                outline = self.delineado, fill=self.color)

    def mover(self, dx, dy):
        self.setX(self.getX() + dx)
        self.setY(self.getY() + dy)

    def __str__(self):
        return "Referencia: " + super().__str__()+\
            "Ancho: " + str(self.__ancho) + " "+\
            "Largo: " + str(self.__alto) + " "

class TrianguloIzq(Punto):
    def __init__(self, x=0, y=0, ancho=10, alto=10, color="black", delineado="black"):
        super().__init__(x, y, color, delineado)
        self.setAncho(ancho)
        self.setAlto(alto)

    def setAncho(self, ancho):
        if ancho>0:
            self.__ancho = ancho
        else:
            self.__ancho = 0

    def setAlto(self, alto):
        if alto>0:
            self.__alto = alto
        else:
            self.__alto = 0

    def getAncho(self):
        return self.__ancho

    def getAltura(self): return self.__alto    

    def dibuja(self, lienzo):
        lienzo.create_polygon(self.getX() + self.getAncho(), self.getY(),
                                self.getX()+self.getAncho(),self.getY()+self.getAltura(),
                                self.getX(), self.getY()+self.getAltura()//2,
                                outline = self.delineado, fill=self.color)

    def mover(self, dx, dy):
        self.setX(self.getX() + dx)
        self.setY(self.getY() + dy)

    def __str__(self):
        return "Referencia: " + super().__str__()+\
            "Ancho: " + str(self.__ancho) + " "+\
            "Largo: " + str(self.__alto) + " "
'''
from tkinter import * 
ventana = Tk()
ventana.title("Pecera")
ventana.geometry("850x650")

lienzo = Canvas(ventana,width=850, height=650,bg ="cyan")
lienzo.pack()

tr=Triangulo(150,350,50,40,"red")
tr.dibuja(lienzo)

tr1=TrianguloInvertido(100,350,50,40,"green")
tr1.dibuja(lienzo)

tr2=TrianguloDer(50,350,50,40,"blue")
tr2.dibuja(lienzo)

tr3=TrianguloIzq(250,350,50,40)
tr3.dibuja(lienzo)

ventana.mainloop()
'''