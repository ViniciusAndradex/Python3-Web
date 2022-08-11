from itertools import combinations, permutations, product

lista = ['Luiz', 'Vinicius', 'Andre', 'Maria', 'Rose', 'Kobe']
print('combinations')
for grupo in combinations(lista, 2):
    print(grupo)
print('permutations')
for grupo in permutations(lista, 2):
    print(grupo)
print('product')
for grupo in product(lista, repeat=2):
    print(grupo)
