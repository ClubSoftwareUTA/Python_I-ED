from Producto import Producto

class Libro(Producto):
    isbn=""
    autor=""

    def __str__(self):
        return """\
        Referencia:\t {}
        Nombre:\t\t {}
        PVP:\t\t {}
        Descripcion:\t {}
        Isbn:\t {}
        Autor:\t {}""".format(self.referencia, self.nombre, self.pvp, self.descripcion, self.isbn, self.autor)