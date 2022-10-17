def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2


divide = divisao(8, 4)
# Esse if é utilizado para verificar se o valor retornado é none ou não!
if divide:
    print(divide)
else:
    print('conta invalida!')

print('-' * 10)


# Retorna qualquer valor!!!
def dumn():
    return f


def f(vari):
    return vari


var = dumn()('Jonas')
print(var, type(var), type(f), id(var), id(f))

print('-' * 10)


def dumb():
    return 'Luiz', 'Otavio'


veri = dumb()
print(veri[1], type(veri))
