from dados import produtos, pessoas, lista

nova_lista = map(lambda x: x * 2, lista)
comprehension = [x * 2 for x in lista]
print(list(nova_lista))
print(comprehension)
print('*' * 10)


# def aumento_preco(p):
#     p['preco'] = round(p['preco'] * 1.05, 2)
#     return p
#
#
# # precos = map(lambda p: p['preco'], produtos) desta forma não é possível fazer nenhum acrescimo.
# precos = map(aumento_preco, produtos)
# for c in precos:
#     print(c)
print('List Comprehension:')
only_person = [p['nome'] for p in pessoas]
for person in only_person:
    print(person)
print('\033[1;31mMAP[IDADE]:')



def aumento_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)
    return p


idades = map(aumento_idade, pessoas)
for idade in idades:
    print(idade)
