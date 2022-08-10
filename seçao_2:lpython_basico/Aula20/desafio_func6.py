def master(fun1=None, fun2=None):
    fun1(), fun2()


def name(nome='Q'):
    return f'\033[1;33m{nome}\033[m'


def soma(n=2, n1=4):
    return n + n1


# Programa Principal
fsoma = master(soma)
fnome = master(name)
fmaster = master()
print(fsoma)
print(fnome)
print(fmaster)
