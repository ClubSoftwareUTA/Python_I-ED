class Producto:
    def __init__(self, referencia, nombre, pvp, descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion

    def __str__(self):
        return """\
        Referencia:\t {}
        Nombre:\t\t {}
        PVP:\t\t {}
        Descripcion:\t {}""".format(self.referencia, self.nombre, self.pvp, self.descripcion)