var = ['lula', 'bolsonaro', 'maria']
for c in var:
    if c.startswith('l'):
        print(f'Começa com J {c}')
    else:
        print(f'Não começa com J {c}')
    # continue e break funcionam!
print('-' * 10)
comeca_com_l = False
for c in var:
    if c.lower().startswith('l'):
        comeca_com_l = True
        break
else:
    print('Não existe um palavra que começa com l')
