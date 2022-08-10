def master(fun1):
    if fun1 == soma:
        while True:
            n = input('Digite um número: ')
            n1 = input('Digite um número: ')
            if n.isdigit() and n1.isdigit():
                n = int(n)
                n1 = int(n1)
                print('Tudo certo, vamos a função!')
                break
            else:
                print('ERROR')
        return fun1(n=n, n1=n1)
    else:
        return fun1(nome=str(input('Digite uma frase: ')))


def name(nome=None):
    return f'\033[1;33m{nome}\033[m'


def soma(n=None, n1=None):
    return n + n1


# Programa Principal
fsoma = master(soma)
fnome = master(name)
print(fsoma)
print(fnome)
