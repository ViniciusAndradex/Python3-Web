a = 2
b = 2
c = 3
print(a == b and b < c)
print(a == b and b > c)
print(a == b or b > c)
print(not a == b or b > c)
d = ''
if not d:
    print('Preencha a variavel.')
print('-' * 10)
nome = 'vinicius'
if 'vini' in nome:
    print(f'i existe em {nome}')
else:
    print('Não existe')
print('-' * 10)
user = input('Nome de usuário: ')
senha = input('Senha de usuário: ')

user_bd = 'vini'
senha_bd = '123456'

if user == user_bd and senha == senha_bd:
    print('Você está logado no sistema.')
else:
    print('user ou senha inválidos')
