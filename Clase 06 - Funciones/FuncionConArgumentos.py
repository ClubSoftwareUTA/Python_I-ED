def sumar(numero1, numero2):
    print (numero1)
    print (numero2)
    print (numero1+numero2)

sumar (5, 7)

def restar(numero1=None, numero2=None):
    if(numero1==None or numero2==None):
        print ("Error, debes enviar dos números a la función")
    else:
        print (numero1-numero2)

restar (10, 5)
restar ()
restar (5)
    
