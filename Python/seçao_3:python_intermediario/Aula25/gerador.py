import sys
from time import sleep


# Função geradora.
def gera():
    # for n in range(100):
    #     yield n
    #     sleep(0.2)
    var = 'valor1'
    yield var
    var = 'valor2'
    yield var
    var = 'valor3'
    yield var


g = gera()

for v in g:
    print(v)
# print(next(g))
# print(next(g))
# print(next(g))

print('-' * 10)
lista = [x for x in range(1000)]
print(type(lista))
lista1 = (x for x in range(1000))
print(type(lista1))
print(sys.getsizeof(lista))
print(sys.getsizeof(lista1))
