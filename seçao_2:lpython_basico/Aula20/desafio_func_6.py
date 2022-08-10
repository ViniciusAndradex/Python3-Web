def master(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def name(nome):
    return f'\033[1;33m{nome}\033[m'


def soma(n=None, n1=None):
    if not n or not n1:
        return 'ERROR, esqueceu de passar algum valor!'
    else:
        return n + n1


# Programa Principal
fsoma = master(soma)
fnome = master(name, 'Luiz')
print(fsoma)
print(fnome)
