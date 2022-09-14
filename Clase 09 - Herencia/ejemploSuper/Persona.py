class Persona:
    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def descripcion(self):
        print("Nombre: ", self.nombre, "Edad: ", self.edad, "Residencia: ", self.residencia)