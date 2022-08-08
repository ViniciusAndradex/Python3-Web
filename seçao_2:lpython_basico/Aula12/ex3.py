name = str(input('Digite seu primeiro nome: '))

if len(name) <= 4:
    print('Seu nome é muito curto!')
elif len(name) <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')
