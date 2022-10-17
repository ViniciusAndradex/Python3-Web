name = str(input('Digite seu primeiro nome: '))
tam = len(name)

if tam <= 4:
    print('Seu nome é muito curto!')
elif tam <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')
