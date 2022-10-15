from rembg import remove
from PIL import Image
input_path = 'Gato3.jpg'
output_path = 'Gato3_sin_fondo.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)
