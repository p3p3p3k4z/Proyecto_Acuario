from Punto import Punto

class Circulo(Punto):

    def __init__(self, x=0, y=0, r=0, color="black", delineado="black", b=1):
        super().__init__(x, y, color,delineado)
        self.setRadio(r)
        self.borde=b

    def setRadio(self, r):
        if r > 0:
            self.__radio = r
        else:
            self.__radio = 0

    def getRadio(self):
        return self.__radio

    def dibuja(self, lienzo):
        lienzo.create_oval(self.getX()-self.__radio//2,
                           self.getY()-self.__radio//2,
                           self.getX()+self.__radio//2,
                           self.getY()+self.__radio//2,
                           outline = self.delineado, fill=self.color,
                           width=self.borde)
    
    def mover(self, dx, dy):
        self.setX(self.getX() + dx)
        self.setY(self.getY() + dy)
    
    def __str__(self):
        return "Centro: " + super().__str__()+\
            "radio: " + str(self.__radio) + " "