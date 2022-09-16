from Gato import Gato
from Circulo import Circulo
from Cuadrado import Cuadrado
circulo = Circulo(0,0,5)
circulo2 = Circulo(0,0,11)
cuadrado = Cuadrado(0,0,5)
cuadrado2 = Cuadrado(0,0,2)
gato =Gato()
lista = [circulo,circulo2,cuadrado,cuadrado2,gato]


for l in lista:
    print(l.__str__())
    print(l.calcular_area())