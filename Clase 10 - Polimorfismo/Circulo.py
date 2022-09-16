import math
from Figura import Figura
class Circulo(Figura):
    def __init__(self, eje_x,eje_y,radio):
        super().__init__(eje_x,eje_y)
        self.radio=radio
    #Sobre escritura de reemplazo
    def __str__(self):
        return "Eje x: {} Eje y: {} Radio: {}".format(self.eje_x,self.eje_y,self.radio)

    def calcular_area(self):
        return "El área del circulo es: {}".format(math.pi*self.radio**2)