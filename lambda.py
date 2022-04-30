#lambda argumentos: expresión
def run():
    # def palindromo(string):
    #     return string == string[::-1]
    palindromo = lambda string: string == string[::-1]
    print(palindromo("ana"))

if __name__=='__main__':
    run()