clientes = {'cliente1': {'nome': 'Vinicius', 'sobrenome': 'Andrade'},
            'cliente2': {'nome': 'Vinicius', 'sobrenome': 'Andrade'}}
a = clientes.copy()

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo: {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')
a['cliente1']['nome'] = 'Joana'
print(a)

print('-' * 10)
lista = [[4, 9], [6, 9], ('index', 15)]
d = dict(lista)
print(d)
