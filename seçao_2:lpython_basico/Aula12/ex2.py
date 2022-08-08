num = input('Digite um horário (0-23): ')
try:
    num = int(num)
    if num <= 23:
        if num <= 11:
            print(f'O horário é {num}:00, Bom dia!')
        elif num <= 17:
            print(f'O horário é {num}:00, Boa tarde!')
        elif num <= 23:
            print(f'O horário é {num}:00, Boa noite!')
    else:
        raise ValueError
except ValueError:
    print('Digite um horário entre 0 | 23')
