import pytube

def DescargarVideo(url):
    # Lugar donde se guardará el video
    path="C:/Users/josel/Downloads/"
    pytube.YouTube(url).streams.get_highest_resolution().download(path)

DescargarVideo(url=input("Introduce la URL del video: "))