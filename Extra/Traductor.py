from deep_translator import GoogleTranslator

def traducirCadena(cadena):
    traductor=GoogleTranslator(source='auto', target='en')
    resultado=traductor.translate(cadena)
    print(resultado)

def traducirArchivo(archivo):
    traductor=GoogleTranslator(source='auto', target='en')
    resultado=traductor.translate_file(archivo)
    print(resultado)

def traducirLista(lista):
    traductor=GoogleTranslator(source='auto', target='fr')
    resultado=traductor.translate_batch(lista)
    print(resultado)

traducirCadena("Hola Mundo")
traducirArchivo("Python.txt")
traducirLista(["Hola", "Mundo", "Como", "Estas"])
