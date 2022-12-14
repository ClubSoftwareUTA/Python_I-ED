# Cifra César
import pyperclip
print("""Este programa cifra o descifra un
mensaje mediante la cifra César \n""")

# Símbolos que pueden cifrarse
#ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALFABETO = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

# Almacena la cadena cifrada/descifrada
salida = ''

# Guarda la opción deseada
modo = input('¿Deseas cifrar o descifrar? (c/d) ')

# Se almacena el texto y la clave
texto = input('Introduce el texto: ')
clave = int(input('Y la clave (1-26): '))

# Ejecuta el proceso letra a letra
for simbolo in texto:
    if simbolo in ALFABETO:
        # Identifica la posición de cada símbolo
        pos = ALFABETO.find(simbolo)
        # ejecuta la operación de cifrado/descifrado
        if modo == 'c':
            pos = (pos + clave) % len(ALFABETO)
        elif modo == 'd':
            pos = (pos - clave) % len(ALFABETO)

        # Añade el nuevo símbolo a la cadena
        salida += ALFABETO[pos]

    # Añade a la cadena el simbolo sin cifrar ni desifrar porque no esta en ALFABETO
    else:
        salida += simbolo

# Muestra la cadena cifrada/descifrada
print(salida)

# Copia la cadena cifrada/descifrada al portapapeles
pyperclip.copy(salida)
