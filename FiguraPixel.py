from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def dibuja(self, lienzo, matriz, c1, c2, c3, c4):
        pass