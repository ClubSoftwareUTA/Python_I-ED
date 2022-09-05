import pywhatkit

def convertir(origen, destino):
    pywhatkit.image_to_ascii_art(origen, destino)

# convertir(r'C:\ruta\nombre_foto.jpg', r'C:\ruta\nombre_archivo.txt')
convertir("imagen.jpg", "imagen")