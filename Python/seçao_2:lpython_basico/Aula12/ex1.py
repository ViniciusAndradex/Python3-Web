num = input('Digite um número: ')
try:
    num = int(num)
    if num % 2 == 0:
        print(f'{num} é PAR')
    else:
        print(f'{num} é IMPAR')
except:
    print(f'O valor "{num}" não é um inteiro.')
