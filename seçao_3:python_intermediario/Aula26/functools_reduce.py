from dados import *
from functools import reduce

soma_total = reduce(lambda ac, i: i + ac, lista, 0)
soma_precos = round(reduce(lambda ac, it: it['preco'] + ac, produtos, 0), 2)
media_idade = reduce(lambda ac, i: i['idade'] + ac, pessoas, 0)
print(f'A soma de lista é {soma_total}')
print(f'A soma dos preços de produtos é {soma_precos}')
print(f'A média de idade das pessoas é {round(media_idade / len(pessoas), 2)}')
