cpf = '16899535009'
list_cpf = []
cont = 0
# Criando a analise e adição dos números do digito 0.
for n, c in enumerate(range(10, 1, -1)):
    cont += int(cpf[n]) * c
    list_cpf.append(cpf[n])

formula = 11 - (cont % 11)
digito0 = 0 if formula > 9 else formula
list_cpf.append(str(digito0))

cont = 0
for n, c in enumerate(range(11, 1, -1)):
    cont += int(list_cpf[n]) * c

formula = 11 - (cont % 11)
digito1 = 0 if formula > 9 else formula
list_cpf.append(str(digito1))

new_cpf = ''
for c in list_cpf:
    new_cpf += c
if new_cpf == cpf:
    print(f'O seu cpf é {new_cpf}')
else:
    print('Sinto muito os digitos encontrados não batem.')
