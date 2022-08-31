#ejemplo bucle for in
frutas = ["manzana", "pera", "cereza"]

#"manzana"  "pera"      "cereza"
#frutas[0]  frutas[1]   frutas[2]
#                             x
#print(frutas[0])
#print(frutas[1])
#print(frutas[2])

#for (la variable) in (listado a recorrer)
for x in frutas:
    if x == "pera":
        print("la fruta es:",x)

#empieza desde el 0 ,y va a terminar en un numero menor al numero que asignemos
#la palabra else nos permite saber (se imprime) unicamente cuando el ciclo finaliza correctamente
#numeroInicio = int(input("agrega el numero desde que iniciamos: "))
for y in range (6,8,2):
    print(y)
else:
    print("termino el ciclo")

# "for _ in"
contador = 0
for _ in range (5):
    contador += 1
print(contador)