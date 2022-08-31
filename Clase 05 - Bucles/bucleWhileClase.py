#El bucle while funciona de forma similar al bucle for
#la diferencia entre el bucle for, la condicion de parada (nosotros damos cuando termina el ciclo)
#bucle while, la condicion de parada es cuando cumple los requisitos

from tkinter.tix import Tree


#while (condicion de parada) : -> acciones
#while (contador < 5):
#    print(contador)
#    contador += 1

contador = 0
condicion = True
while (condicion):
    print(contador)
    pregunta = input("quieres aumentar una unidad al contador? si/no\n")
    if( pregunta != "si"):
        condicion = False
    contador += 1
