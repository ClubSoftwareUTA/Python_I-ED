""" valor = True

if (valor):
    print('Este el bloque if')
else :
    print('Bloque else')

print('Fuera del bloque') """

""" num1 = 3
num2 = 1
num3 = 2

if (num1 == num2):
    print('Numero 1 es igual numero 2')
elif(num1 == num3):
    print('Numero 1 es igual numero 3')
elif(num2 == num3):
    print('Numero 2 es igual a numero 3')
else:
    print('Todos los numeros son diferentes')
     """

#LISTAS
#existe elemento str en la lista
""" lista = [2, 3, 7.5]

if(len(lista) != 0):
    #print('La lista esta vacia')
    #print(type(elementoUno))
    if (type(lista[0]) == str or type(lista[1]) == str or type(lista[2]) == str):
        print('Si existe elementos str')
    else:
        print('No existe elementos string')
else:
    elemento = input('Ingrese valor: ')
    #print(elemento.isnumeric())
    if (elemento.isnumeric()):
        lista.append(int(elemento))
    else:
        lista.append(elemento)
    print(type(elemento))
    print(lista) """


#DICCIONARIOS

id = input('Ingrese id: ')

persona = {"id" : '1723',
            "nombre" : 'Jean',
            "apellido" : 'Giron'}

if (persona["id"] != id):
    print('El id ingresado es incorrecto')
else:
    print('Bienvenido ' + persona["nombre"] + ' ' + persona["apellido"])




