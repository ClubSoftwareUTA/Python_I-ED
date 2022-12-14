import pyperclip

CLARO = 'abcdefghijklmnopqrstuvwxyz '
CIFRADO = 'zyxwvutsrqponmlkjihgfedcba '

salida = ''

texto = input('Introduce el texto a cifrar: ')

for simbolo in texto.lower():
    if simbolo in CLARO:
        indice=CLARO.index(simbolo)
        salida+=CIFRADO[indice]

print(salida)

pyperclip.copy(salida)
