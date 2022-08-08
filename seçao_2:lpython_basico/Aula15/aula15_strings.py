frase = 'O rato roeu a roupa do rei de roma'
tam = len(frase)
cont = 0
new_string= ''

while cont < tam:
    print(frase[cont], end='.')
    if frase[cont] in 'oO':
        new_string += frase[cont]
    cont += 1
print('\n' + new_string)
