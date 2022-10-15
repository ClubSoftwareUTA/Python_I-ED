from PIL import Image
from captcha.image import ImageCaptcha
imagen = ImageCaptcha(width=300, height=100)
textoCaptcha = input("Ingrese el texto del captcha: ")
dato = imagen.generate(textoCaptcha)
imagen.write(textoCaptcha, "captcha.png")
Image.open("captcha.png")
