string = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
n = 10
lista = [string[v: v + n] for v in range(0, len(string), n)]  # Pega os indices e passa o fatiamento como retorno.
lista = '.'.join(lista)
print(lista)
