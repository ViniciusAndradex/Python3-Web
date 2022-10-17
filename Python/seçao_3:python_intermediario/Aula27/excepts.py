try:
    a = 1 / 0
    # a = {}
    # print(a[15])
except NameError as erro:
    print(f'ERRO do desenvolvedor: {erro}')
except (IndexError, KeyError) as erro:
    print('ERRO de indice ou key não adicionada corretamente!')
except Exception as erro:
    print(f'Erro inesperado: {erro}')
else:
    pass
    # print('Seu codigo deu bom!')
    # print(a)
finally:
    a = None
    # print('Vou imprimir de qualquer forma!')

print('Podemos continuar!')
print(a)
