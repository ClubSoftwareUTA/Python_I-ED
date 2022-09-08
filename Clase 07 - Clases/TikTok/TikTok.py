from time import sleep


class TikTok ():
    siguiendo = 12
    seguidores = 100
    likes = 1000

    def __init__(self, yoSigo, seguidoresNuevos, likesNuevos):
        self.siguiendo = yoSigo+self.siguiendo
        self.seguidores = seguidoresNuevos+self.seguidores
        self.likes = likesNuevos+self.likes
        print("Actualizando datos...")
        sleep(3)
        print("Datos actualizados")

    def actualizarPerfil(self):
        print("Siguiendo: ", self.siguiendo)
        print("Seguidores: ", self.seguidores)
        print("Likes: ", self.likes)
        print("Actualizado")
