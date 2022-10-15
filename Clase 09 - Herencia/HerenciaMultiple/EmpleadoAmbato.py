from Ambato import Ambato
from Empleado import Empleado


class EmpleadoAmbato(Empleado, Ambato):
    def saludar (self):
        print ('Mi nombre es: ' + self.nombre)
        print ('Vivo en: ' + self.domicilio)