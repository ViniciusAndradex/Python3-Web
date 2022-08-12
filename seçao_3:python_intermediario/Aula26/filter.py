from dados import produtos, pessoas, lista

nova_lista = filter(lambda x: x > 5, lista)
new_list = [x for x in lista if x > 5]
print(list(nova_lista))
print(new_list)
print('-' * 10)


def filtra(p):
    # if p['preco'] > 50:
    #     p['e_caro'] = True
    if p['idade'] > 45:
        p['old'] = True
    return True


# dicionario = filter(lambda p: p['preco'] > 50, produtos)
# dicionario_comp = [p for p in produtos if p['preco'] > 50] mesma coisa.
# for prod in dicionario:
#     print(prod)

dictio = filter(filtra, pessoas)

for pessoa in dictio:
    print(pessoa)
