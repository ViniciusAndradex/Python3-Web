from itertools import count

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
contador = count(start=0)
lista1 = ['luiz', 'João', 'Maria']
lista1 = zip(contador, lista1)

for valor, val in lista1:
    print(valor, val)

for valor in lista:
    print(round(next(contador), 2), valor)

