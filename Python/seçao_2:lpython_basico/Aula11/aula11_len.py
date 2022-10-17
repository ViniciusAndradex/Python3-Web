user = input('Digite seu usuário: ')
qtd_caractere = len(user)

print(user, qtd_caractere, type(qtd_caractere))

if qtd_caractere < 6:
    print('Você precisa de pelo menos 6 caracteres.')
else:
    print('Você foi cadastrado no sistema.')
print('-' * 10)
s1 = input('Digite algo: ')
s2 = input('Digite algo: ')

print(f'A quatiade total de caractere digitados foi {len(s1) + len(s2)}')
