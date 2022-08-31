# el "break" nos permite finalizar un bucle (una accion)
# el "continue" nos permite saltar una iteracion del ciclo

#for x in range (6):
#    if x == 3:
#        break
#    print(x)
#else:
#    print("Termino el bucle correctamente")

#una calculadora con funciones basicas, la calculadora siempre va a estar funcionando a menos que el
#usuario quiera apagar la calculadora

#1- sume
#2- reste
#3- multiplique
#4- divida (ojo con la divicion para 0)
#5- finaliza la calculadora
#6- nos de las tablas del numero elegido
#7- serie de fibonacci la cantidad de numeros que el usuario requiera

diccionario = {
    "nombre":"Luis",
    "apellido":"Zerna",
    "edad" : 24
}

for _, y in diccionario.items():
    print(y)