def divisor(num):
    divisor = []
    for i in range(1, num +1):
        if num % i == 0:
            divisor.append(i)
    print(divisor)    

def run():
    try:
        num = int(input('Ingrese un numero: '))
        if num <= 0:
            raise TypeError
                          
        divisor(num)
        print('Termino el programa')

    except ValueError:
        print('Debes ingrese un numero, vuelve a intentarlo.')
        run()

    except TypeError:
                print('Debes ingresar un numero mayor a cero, vuelve a intentarlo.')
                run()


if __name__=='__main__':
    run()