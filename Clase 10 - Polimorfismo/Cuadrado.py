from Figura import Figura


class Cuadrado(Figura):
    def __init__(self, eje_x,eje_y,lado):
        super().__init__(eje_x,eje_y)
        self.lado=lado

    #Sobre escritura de refinamiento
    def __str__(self):
        return super().__str__()+" Lado: {}".format(self.lado)

    def calcular_area(self):
        return "El área del cuadrado es: {}".format(self.lado*self.lado)