#los operedores ternarios permiten realizar una asignacion de un valor segun 
#una condicion pre echa

#if es un condicional
condicion = True

#if(5 != 5):
#    valor = "condicion cierta"
#else:
#    valor = "condicion falsa"

#variable = (resultado verdadero) "if" (condicion) "else" (resultado falso)
valor = "condicion cierta" if (condicion) else "condicion falsa"
print(valor)

#quiero saber si un gato es o no llamativo con un operador ternario
#esBonito = False
#gato = "es bonito" if (esBonito) else "no es bonito"
#print("El gato "+gato)

#estos valores son de tipo String
#esBonito = input("El gato te parece bonito? si/no \n")
#gato = "es bonito" if (esBonito == "si") else "no es bonito"
#print("El gato "+gato)

#numeroUno = input("Ingrese el primer numero : ")
#print(numeroUno)
#print(type(int(numeroUno)))

#vamos a preguntar al usuario sobre un numero (inserte un numero)
#decirle al usuario si el numero es par o impar
#numeroUno = input("Ingrese un numero: ")
#numeroUno = int(numeroUno)
#paridad = numeroUno % 2
#resultado = "Es un numero par" if (paridad == 0) else "Es un numero impar"
#print(resultado)

#forma dos
numeroUno = int(input("Ingrese un numero: "))
resultado = "Es un numero par" if (numeroUno%2 == 0) else "Es un numero impar"
print("El numero",numeroUno,resultado)

