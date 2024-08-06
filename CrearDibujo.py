import time
from tkinter import *

from Pixel import Pixel
from Tiburon import Tiburon
from Buzo import Buzo
from Fondo import *

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
violeta= '#300089'

def DibujaPoly(lienzo):
    dibu = [
            Arrecife(150,100,3,AzulVerdoso),Arrecife(400,300,1.5),
            Esponja(-10,200,1.5,"orange","red"),Esponja(-20,300),
            Arena(),Buzo(),Alga(-105,305,1.5,"blue"),Coral(200,350,3),Coral(0,500,1.5,verdeAmarillo),
            Tiburon(),Tiburon(100,-100,1.5,PurpuraOscuro,"gold"),Tiburon(750,450,0.4,Vino,"gold"),
            Alga(580,430),Alga(600,450,1,"green"),
            Alga(280,400,1,"red"),Alga(30,323,0.5,violeta),Alga(45,323,0.5,"pink"),
            Estrella(-90,400,1.5),Estrella(520,360,2,"green","purple",verdeAmarillo,"yellow"),
            Burbuja(620,290,1,2,verdeBajo),Burbuja(550,280,1.5),Burbuja(600,260,1,0.5,"blue")
            ]
    
    for d in dibu:
        d.dibuja(lienzo)
    

ventana = Tk()
ventana.title("ACUARIO")
ventana.geometry("850x650")

lienzo = Canvas(ventana,width=850, height=650,bg =AzulMarino)
lienzo.pack()

def moverPez(event):
    if event.keysym == 'Up':
        p.mover(0, -5)
    elif event.keysym == 'Down':
        p.mover(0, 5)
    elif event.keysym == 'Left':
        p.mover(-5, 0)
    elif event.keysym == 'Right':
        p.mover(5, 0)
    lienzo.delete("all")
    DibujaPoly(lienzo)
    p.dibuja(lienzo, pezPixel, "green", verdeBajo, verdeAmarillo, "black")

DibujaPoly(lienzo)
p = Pixel(100, 100,7)
p.dibuja(lienzo, pezPixel,"green", verdeBajo, verdeAmarillo, "black")

ventana.bind_all('<KeyPress>', moverPez)

ventana.mainloop()