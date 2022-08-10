a = lambda x, y: x * y

print(a(5, 2))

print('-' * 10)
lista = [['P1', 13], ['P2', 6], ['P3', 7], ['P4', 50], ['P5', 8]]


# def func(item):
#     return item[1]


# lista.sort(key=func) , reverse=True para fazer descrescente
# lista.sort(key=lambda item: item[1])
print(sorted(lista, key=lambda i: i[1]))
