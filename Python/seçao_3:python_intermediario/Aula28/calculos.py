from math import pi

PI = pi


def dobra_lista(listas):
    return [x * 2 for x in listas]


def multiplica(listas):
    r = 1
    for i in listas:
        r *= i
    return r


if __name__ == '__main__':
    print(__name__)
    lista = [1, 2, 3, 4, 5, 6]
    print(dobra_lista(lista))
    print(multiplica(lista))
    print(PI)
