#assert condition, mensaje error

def divisor(num):
    divisor = []
    for i in range(1, num +1):
        if num % i == 0:
            divisor.append(i)
    print(divisor)    

def run():
    num = input('Ingrese un numero: ')   
    assert num.isnumeric(), 'Debe ingresar un numero mayor a cero.'
    divisor(int(num))
    print('Termino el programa')

if __name__=='__main__':
    run()