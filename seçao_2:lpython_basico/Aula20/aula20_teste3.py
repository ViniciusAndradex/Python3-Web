def func(*args, **kwargs):
    # args = list(args)
    # args[0] = 20
    print(args)
    print(args[0])
    print(*args)
    print(kwargs)
    nome = kwargs.get('nome')
    print(nome)
    data = kwargs.get('data')
    if not data:
        print('Não deu.')
    else:
        print(data)


lista = [1, 2, 3, 4, 5]
lista1 = [10, 2, 30, 40, 50]
# func(1, 2, 3, 4, 5)
print('-' * 10)
# func(*lista, *lista1)
# func(*lista, *lista1, nome='Jonas', idade=20)
func(*lista, *lista1, nome='Jonas', idade=20, data=2001)
