import random
import os
random.seed()
palabra = ''
character = []
adivinando = []
errorCero = ''
errorUno ='\n               \n              O'
errorDos ='\n               \n              O\n             /'
errorTres ='\n               \n              O\n             / \\'
errorCuatro ='\n               \n              O\n             /|\\\n              |'
errorCinco ='\n               \n              O\n             /|\\\n              |\n             /'
errorSeis ='\n               \n              O\n             /|\\\n              |\n             / \\'
errorSiete ='\n               \n              O\n             /|\\\n              |\n_____________/_\\___'
errorOcho ='\n   |           \n   |          O\n   |         /|\\\n   |          |\n___|_________/_\\___'
errorNueve ='   ___________\n   |           \n   |          O\n   |         /|\\\n   |          |\n___|_________/_\\___'
errorDiez ='   ___________\n   |          |\n   |          O\n   |         /|\\\n   |          |\n___|_________/_\\___'
errorOnce ='   ___________\n   |          |\n   |          X\n   |         /|\\\n   |          |\n___|________ / \\'

errores = [errorCero, errorUno, errorDos, errorTres, errorCuatro, errorCinco, errorSeis, errorSiete, errorOcho, errorNueve, errorDiez, errorOnce]

def extractor_de_palabras():
    global palabra
    global x
    with open('./files/data.txt', 'r', encoding='utf-8') as f:
        palabras = [line for line in f]
        palabra = palabras[random.randint(0, 170)]
        for ch in range(0, len(palabra)-1):
            character.append(palabra[ch].upper())
        for ch in character:    
            adivinando.append('-')

def adivina(letra = ''): 
    x = 0 
    y = 0 
    fallos = 0

    for i in adivinando:
        x += 1
        print(i, end='')

    while x > y :
        letra = input('\n\nIngresa una letra: ')
        y = 0
        if letra.upper() not in character:
            fallos += 1 
            if fallos == 11:
                break

        for i, ch in enumerate(character):           
            if ch == letra.upper():
                adivinando[i] = ch
        print('')
        os.system('clear')
        for i in adivinando:
            if i != '-':
                y += 1
            print(i, end='')
        print('\n')
        print(errores[fallos])


    if fallos == 11:
        os.system('clear')
        print('Perdiste\n')
        print(errorOnce)
        print()
    else:
        print("\n\n¡GANASTE!, la palabra es ", end='')
        for i in adivinando:
            print(i, end='')
        print()


def run():
    print("""
    ***    ***      ****      ****   ***   **********  ****     ****      ****      ****   ***
    ***    ***     **  **     *****  ***   ****   ***  *****   *****     **  **     *****  ***
    **********    ********    ****** ***   ***         ****** ******    ********    ****** ***
    **********    ********    *** ******   ***  *****  *** ***** ***    ********    *** ******
    ***    ***   ***    ***   ***  *****   ***    ***  ***  ***  ***   ***    ***   ***  *****
    ***    ***  ***      ***  ***   ****   **********  ***       ***  ***      ***  ***   ****
    """)
    print('¡Adivina la palabra!\n')
    extractor_de_palabras()
    adivina()


if __name__=='__main__':
    run()
