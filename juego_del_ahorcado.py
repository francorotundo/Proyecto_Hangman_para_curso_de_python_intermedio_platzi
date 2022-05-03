import random
import os
random.seed()
palabra = ''
character = []
adivinando = []

def extractor_de_palabras():
    global palabra
    global x
    with open('./files/data.txt', 'r', encoding='utf-8') as f:
        palabras = [line for line in f]
        palabra = palabras[random.randint(0, 170)]
        for ch in range(0, len(palabra)-1):
            character.append(palabra[ch])
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
        if letra is not character:
            fallos += 1 
            if fallos == 11:
                break

        for i, ch in enumerate(character):           
            if ch == letra:
                adivinando[i] = ch
        print('')
        os.system('clear')
        for i in adivinando:
            if i != '-':
                y += 1
            print(i, end='')

    if fallos == 11:
        os.system('clear')
        print('Perdiste\n')
    else: 
        print("\n\n¡GANASTE! la palabra es ", end='')
        for i in adivinando:
            print(i, end='')
        print()


def run():
    print('¡Adivina la palabra!\n')
    extractor_de_palabras()
    adivina()


if __name__=='__main__':
    run()