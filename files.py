def read():
    number = []
    with open('./files/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            number.append(int(line))
        print(number)


def write():
    names = ['Rixy', 'Franco', 'Yajira', 'Emma', 'Mary', 'Francisco']
    with open('./files/family.txt', 'w', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')

def append():
    names = ['Ricardo', 'Ana']
    with open('./files/family.txt', 'a', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')

def run():
    read()

if __name__=='__main__':
    run()