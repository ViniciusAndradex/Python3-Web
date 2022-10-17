cpf = '16899535009'
new_cpf = cpf[:-2]
total = index = 0
c = 10

# Criando a analise e adição dos números do digito 0.
while True:
    total += int(new_cpf[index]) * c
    if c == 2:
        digit = 11 - (total % 11)
        new_cpf += '0' if digit > 9 else str(digit)
        if len(new_cpf) == 11:
            break
        cont = index = 0
        c = 11
    c -= 1
    index += 1

if new_cpf == cpf:
    print(f'O seu cpf é valido: {new_cpf}')
else:
    print('Sinto muito os digitos encontrados não batem, CPF INVALIDO.')
