from abc import ABC, abstractmethod


class Figura(ABC):
    def __init__(self,eje_x,eje_y):
        self.eje_x=eje_x
        self.eje_y=eje_y
    
    def __str__(self):
        return "Eje x: {} Eje y {}".format(self.eje_x,self.eje_y)

    @abstractmethod
    def calcular_area():
        pass