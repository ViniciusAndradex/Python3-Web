print(2 == 2)
print(2 == 1)
print(2 == '2')
print('-' * 10)
num = 2
n = 2
exp = num == n
print(exp)
print('-' * 10)
nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))
idade_limite = 18
if idade >= idade_limite:
    print(f'{nome} pode pegar um empréstimos.')
else:
    print(f'{nome} não pode pegar empréstimos.')
print('-' * 10)
nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))
muito_jovem = 20
muito_velho = 30
if muito_jovem <= idade <= muito_velho:
    print(f'{nome} pode pegar um empréstimos.')
else:
    print(f'{nome} não pode pegar empréstimos.')
