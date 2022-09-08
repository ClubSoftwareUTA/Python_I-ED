class Foco:
    def __init__(self, usuario, estado, color):
        self.usuario = usuario
        self.estado = estado
        self.color = color
        print("Estado inicial", self.usuario,"\n")

    def encender(self):
        if self.estado:
            print("El foco ya esta encendido\n")
        else:
            self.estado = True
            print("El foco se ha encendido\n")
    
    def apagar(self):
        if self.estado:
            self.estado = False
            print("El foco se ha apagado\n")
        else:
            print("El foco ya esta apagado\n")

    def cambiarColor(self, color):
        if self.estado:
            self.color = color
            print("El foco cambio de color a", self.color, "\n")
        else:
            self.encender()
            self.color = color
            print("El foco cambio de color a", self.color, "\n")

    def estadoFoco(self):
        if self.estado:
            print("El foco esta encendido y es de color", self.color, "\n")
        else:
            print("El foco esta apagado\n")