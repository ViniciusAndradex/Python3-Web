from contextlib import contextmanager


@contextmanager
def abrir(arquivo, modo):
    try:
        arquivo = open(arquivo, modo)
        yield arquivo  # retorne
    finally:
        arquivo.close()


with abrir('abc.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
