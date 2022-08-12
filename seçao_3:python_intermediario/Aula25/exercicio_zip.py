from itertools import zip_longest
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_unida = zip(lista_a, lista_b)
lista_unida1 = zip_longest(lista_a, lista_b, fillvalue=0)
sum_list = [x + y for x, y in lista_unida]
sum_list1 = [x + y for x, y in lista_unida1]

print(f'Resultado = {sum_list}')
print(f'Resultado = {sum_list1}')
