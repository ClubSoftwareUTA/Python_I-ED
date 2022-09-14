from math import dist
from Producto import Producto

class Alimento(Producto):
    productor=""
    distribuidor=""

    def __str__(self):
        return """\
        Referencia:\t {}
        Nombre:\t\t {}
        PVP:\t\t {}
        Descripcion:\t {}
        Productor:\t {}
        Distribuidor:\t {}""".format(self.referencia, self.nombre, self.pvp, self.descripcion, self.productor, self.distribuidor)