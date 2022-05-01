# ¡Adivina la palabra
# ------
# Ingresa una letra: 
# ¡Ganaste! La palabra es -----
# Incorpora comprehension, manejo de errores y manejo de archivos.
# Utiliza el archivo data.txt y leelo para obtener las palabras.
# Investiga la funcion enumerate. 
# El metodo get de los diccionarios puede servirte.
# La sentencia: os.system('cls') -> windows, os.system('clear') -> UNIX, te servira para limpiar la pantalla.
# Mejora el juego: añade un sistema de puntos, dibuja al 'ahorcado' en cada jugada con codigo ASCII.
# Mejora la interfaz.
import random 
random.seed()


def extractor_de_palabras():
    with open('./files/data.txt', 'r', encoding='utf-8') as f:
        palabras = []
        for line in f:
            palabras.append(line)
        palabra = palabras[random.randint(0, 170)]
        

def run():
    print('¡Adivina la palabra!')
    extractor_de_palabras()
    # letra = input('Ingresa una letra: ')


if __name__=='__main__':
    run()