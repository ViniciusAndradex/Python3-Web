lista = [0, 1, 2, 3, 4]
f = 1234
lista = iter(lista)
print(next(lista))
print(next(lista))
print(next(lista))
print(hasattr(lista, '__iter__'))
print(hasattr(lista, '__next__'))
print(hasattr(f, '__iter__'))
