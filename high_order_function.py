def run():
    #Uso de Filter(utiliza dos parametros (una function y una lista))
    # my_list = [i for i in range(1, 15)]

    # odd = list(filter(lambda x: x%2 != 0, my_list))

    # print(odd)

    #Uso de map
    # squares = [i**2 for i in range(1,6)]
    # lista = [i for i in range(1, 6)]
    # squares = list(map(lambda x: x**2, lista))
    # print(squares)

    #Uso de reduce
    from functools import reduce
    lista2 = [2, 2, 2, 2, 2]
    # all_multiplied = 1
    # for i in lista2:
    #     all_multiplied*=i

    all_multiplied = reduce(lambda a, b: a*b, lista2)
    print(all_multiplied)


if __name__=='__main__':
    run()