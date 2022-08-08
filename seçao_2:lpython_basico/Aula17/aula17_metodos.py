string = 'O Brasil é o país do futebol, O Brasil é penta.'
lista1 = string.split(' ')
print(lista1)
lista2 = string.split(',')
palavra = ''
contagem = 0

for val in lista1:
    # print(f'A palavra {val} apareceu {lista1.count(val)}x vezes ')
    qtd_vezes = lista1.count(val)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = val
print(f'A palavra que mais apareceu foi {palavra} e ela apareceu {contagem} vezes.')
print('-' * 15)
for val in lista2:
    print(val.strip().capitalize())
print('-' * 10, '\n')
string = '-'.join(lista1)
print(string)
print('-' * 10, '\n')
string = 'O Brasil é penta'
lista = string.split(' ')

for num, v1 in enumerate(lista):
    print(f'[{num}][{v1}]: {lista[num]}')
print('-' * 10, '\n')
lista = [[0, 'Luiz'], [1, 'João'], [1, 'Maria']]
# Desempacotamento, consigo acessar todos os elementos que estejam dentro de outras lista ou tuplas.
for indice, nome in lista:
    print(f'{indice}, {nome}')
print('-' * 10, '\n')
lista = [['Ed', 'Mota', 'Magal'], ['Justin', 'Magali', 'Manel']]
for v in enumerate(lista):
    indice, valor = v  # Desempacotar!!!!
    nome1, nome2, nome3 = valor
    print(indice, valor, v)
    print(f'NOMES DESEMPACOTADOS: {nome1} - {nome2} - {nome3}')
