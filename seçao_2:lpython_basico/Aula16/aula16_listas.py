lista = ['A', 'B', 'C', 'D', 'E', 10.5]
lista[5] = 'Meu'
# Os indices e métodos funcionam iguais ao fatiamento.
print(lista[0])
print(lista[-1])
print(lista[0:3])
print(lista[::2])
print(lista[::-1])

print('-' * 10)
l1 = [1, 2, 3]
print(l1)
l2 = [4, 5, 6]
l3 = l1 + l2
l1.extend(l2)
print(f'l3 : {l3}')
print(f'l1 : {l1}')
l2.append('b')
print(f'l2: {l2}')
l1.insert(0, 'h')
print(f'l1: {l1}')
l1.pop()
print(f'l1: {l1}')
print('-' * 10)
del l1[:2]
print(f'l1: {l1}')
print(max(l1))
print(min(l1))
l1.clear()
l1 = list(range(0, 9))
print(l1)
for val in l1:
    print(f'l1: {val}')
print(f'Soma = {sum(l1)}')
print('-' * 10)
l2 = ['String', True, 10, -20.5]
for c in l2:
    print(f'O tipo do dado é {type(c)} e tem o valor {c}')
print('-' * 10)
secreto = 'perfume'
digit = []
chance = 3
while True:
    if chance < 1:
        print('Suas chance terminaram.')
        break
    letra = input('Digite um letra [Somente uma letra!!!]: ')[0]
    if letra in secreto:
        print(f'A letra {letra} existe na palavra secrata!')
        digit.append(letra)
    else:
        print(f'A letra {letra}, não pertence a palavra.')
    palavra = ''
    for p in secreto:
        if p in digit:
            palavra += p
        else:
            palavra += '*'
    if palavra == secreto:
        print(f'Parabéns, você ganhou acertou a palavra era {secreto}')
        break
    else:
        print(f'DICA: {palavra}')
    if letra not in secreto:
        chance -= 1
        print(f'número de chances {chance}')
