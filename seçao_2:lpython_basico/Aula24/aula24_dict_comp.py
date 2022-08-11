lista = [('chave', 4), ('chave2', 'valor2')]
dici = {x: y * 2 for x, y in lista}
print(dici)

print()
# d1 = {x: y for x, y in enumerate(range(5))}
d1 = {x for x in range(5)}
print(d1)
d2 = {f'chave_{x}': x**2 for x in range(5)}
print(d2)
