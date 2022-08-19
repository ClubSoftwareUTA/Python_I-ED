""" entero = 1 #entero
flotantes = 2.2 #flotante
complejos = 2j
booleanos = True # True o False
lista = []
tuplas = ()
diccionarios = {}

print(type(entero))
print(type(flotantes))
print(type(complejos))
print(type(booleanos))
print(type(tuplas))
print(type(diccionarios)) """

""" nombre = input('Ingrese nombre')
apellido = 'Ortiz'
edad = int(input('Ingrese edad: '))
print(type(edad))
print('Soy ' + nombre + ' ' + apellido + ' tengo' , edad , 'años')
apellido = 12
print(type(apellido)) """

#listas
""" valores = ['frutas', 2, 2, 2, True, 'juegos']

valores.append('nombres')
print(valores)
cadena = valores.pop()
print(valores)
print(cadena) """

#tuplas

""" nombres = ('Juan', 'Pedro', 'Jean')

listaNombres = list(nombres)
listaNombres.append('Andres')

print(listaNombres) """

#dicionarios

""" persona = {
    "id" : 1,
    "nombre" : 'Juan',
    "apellido" : 'Ortiz'
}

#persona["telefono"] = "0983467813"
#print(persona)
#persona.pop('telefono')

persona.popitem()

print(persona) """

""" Empresa = {
    "Cliente": {
        "nombre" : 'Andres',
        "apellidop" : 'Ortiz'
    },

    "Producto": {
        "id" : 34,
        "precio" : 12.1
    }
}

print(Empresa) """
#automovil = dict(marca = 'Toyota', modelo = 'xplore')
#print(automovil)

#tipado estatico
num: int = 5
nombre: str = 'Kevin'
bandera: bool = True


print(num, nombre, bandera)







