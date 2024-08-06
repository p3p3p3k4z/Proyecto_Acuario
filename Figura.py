#Figura.py
from abc import abstractmethod
from abc import ABC

class Figura(ABC):
    @abstractmethod
    def dibuja(self):
        pass
