#Implemtar un sistema con un menu que
#Permita registrar clientes
#Permita ver clientes
#Permita ver clientes mayores de edad
#El sistema se finaliza cuando el usuario lo desee

clientes = []

while (True):
    print('\n--Menu del Sistema--')
    print('1. Registrar Clientes' +
            '\n2. Ver Clientes' +
            '\n3. Ver clientes mayores de edad' + 
            '\n0. Salir')
    opcion = int(input('Ingrese opción: '))
    if (opcion == 1):
        print('Ingresar datos cliente')
        nombre = input('Ingrese nombre: ')
        apellido = input('Ingrese apellido: ')
        edad = int(input('Ingrese edad: '))
        cliente = {"Nombre" : nombre,
                    "Apellido" : apellido,
                    "Edad" : edad}
        
        clientes.append(cliente)
        print('Cliente ingresado satisfactoriamente')
    elif (opcion == 2):
        #print(clientes)
        for i in clientes:
            for x, y in i.items():
                print(x, ':', y)
    elif (opcion == 3):
        print('Clientes mayores de edad')
        for i in clientes:
            edad = i.get("Edad")
            if edad >= 18:
                for x, y in i.items():
                    print(x, ':', y)
    elif (opcion == 0):
        print('Gracias por utilizar el sistema')
        break
    else:
        print('Opción no valida')