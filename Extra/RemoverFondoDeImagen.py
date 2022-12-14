from rembg import remove
from PIL import Image
input_path = 'logo1.jpg'
output_path = 'logo13_sin_fondo.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)
