import math
import pyperclip


def main():
    criptograma = input('Introduce el criptograma: ')
    clave = int(input('Introduce la clave: '))
    criptograma = formatear_mensaje(criptograma)

    texto_plano = descifrar(criptograma, clave)

    print(texto_plano.lower())
    pyperclip.copy(criptograma)


def formatear_mensaje(criptograma):
    mensaje_nuevo = ''
    for simbolo in criptograma:
        if simbolo != ' ':
            mensaje_nuevo += simbolo
    return mensaje_nuevo


def descifrar(criptograma, clave):
    num_col = math.ceil(len(criptograma)/clave)
    num_filas = clave

    celdas_vacias = (num_col*num_filas)-len(criptograma)

    texto_plano = ['']*num_col
    col = 0
    fila = 0

    for simbolo in criptograma:
        texto_plano[col] += simbolo
        col += 1

        if (col == num_col) or (col == num_col-1 and fila >= num_filas-celdas_vacias):
            col = 0
            fila += 1
    return ''.join(texto_plano)


if __name__ == '__main__':
    main()
