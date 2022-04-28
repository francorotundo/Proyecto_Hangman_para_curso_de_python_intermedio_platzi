def run():
    # dicts = {}
    # for x in range(1, 101):
    #     dicts[x] = x**3

    #{key:value for value in iterable if condition}
    # dicts = { x: x**3 for x in range(1, 101) if x % 3 != 0}
    # print(dicts)

    #Reto Crear un dictionary comprehension, cuyas llaves sean los 1000 primeros números naturales con sus raíces cuadradas como valores.
    my_dict = {i:round(i**0.5, 2) for i in range(1,1001)}
    print(my_dict)


if __name__=='__main__':
    run()