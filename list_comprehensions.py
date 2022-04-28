def run():
    # lista = []
    # for i in range(1, 101):
    #     if i%3 != 0:
    #         lista.append(i**2)
    # print(lista)
  #[element for element in iterable if condition]  
    # squares = [i**2 for i in range(1,101) if i % 3 != 0]
    # print(squares)

    #Reto: Crear una lista de todos los multiplos de 4, que tambien sean multiplos de 6 y de 9, has 5 digitos

    squares = [i for i in range(1, 100000) if (i % 4 == 0 and i % 6 == 0 and i % 9 == 0)]

    print(squares)
    
if __name__=='__main__':
    run()