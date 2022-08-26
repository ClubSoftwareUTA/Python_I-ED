#permiten identificar si un valor existe o no en un conjunto de datos
listaUno = [1,2,3,4,5]
listaDos = [6,7,8]

#"in" operador de pertenencia en caso de existir
print(2 in listaUno)
# "not in" contraparte del operador "in"
print(7 not in listaUno)

#diccionario (en los diccionarios buscamos mediante las llaves)
diccionarioUno = {"saludo":["hola","que","tal"]
                , "despedida":"adios"
                , "llave": "valor de la llave"}
#print("hola" not in diccionarioUno)
#diccionarioUno["saludo"] = ["hola","que","tal"]
print("despedida" in diccionarioUno["saludo"])

