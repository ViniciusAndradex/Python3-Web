from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Fortaleza', 'Rio de Janeiro', 'Monte Belo']

estados = ['SP', 'CE', 'RJ']

cidades_estado = zip(estados, cidades)
cidades_estado1 = zip(indice, estados, cidades)
# Ao utilizar um count que é um gerador infinito, é melhor usar zip se não ele nunca para!
# cidades_estado1 = zip_longest(indice, estados, cidades, fillvalue='Estado')

for indice, estado, cidade in cidades_estado1:
    print(indice, estado, cidade)

print(list(cidades_estado))
print(list(cidades_estado1))
