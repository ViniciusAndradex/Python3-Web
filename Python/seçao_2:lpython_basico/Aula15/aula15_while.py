
while True:  # Laço infinito
    nome = input('Qual seu nome? ')
    print(f'olá {nome}')
    if nome not in '':
        break

x = 0
while x < 10:
    if x == 3:
        x += 1
        continue
    print(x, end=' - ')
    x += 1

print('-' * 10)
x = 0
y = 0
while x < 5:
    while y < 5:
        print(f'x = {x} e y = {y}')
        y += 1
    x += 1
    y = 0
print('-' * 10)
while True:
    print()
    n = input('Digite um número: ')
    n1 = input('Digite um número ')
    operador = input('Digite um operador [+ | - | * | / ]: ')

    try:
        n = int(n)
        n1 = int(n1)
    except:
        print('ERRO. Digite um número!')
    else:
        if operador == '+':
            print(f'{n + n1}')
        elif operador == '-':
            print(f'{n - n1}')
        elif operador == '/':
            print(f'{n / n1}')
        elif operador == '*':
            print(f'{n * n1}')
    sair = input('Deseja sair? [S/N]\n').upper()
    if sair == 'S':
        break
        