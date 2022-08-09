def master(fun1=None, fun2=None):
    if fun1 and not fun2:
        return name(fun1)
    if fun1 and fun2:
        return soma(fun1, fun2)
    return None


def name(nome):
    return f'\033[1;33m{nome}\033[m'


def soma(n, n1):
    return n + n1


# Programa Principal
fsoma = master(5, 5)
fnome = master('Maria')
fmaster = master()
print(fsoma)
print(fnome)
print(fmaster)
