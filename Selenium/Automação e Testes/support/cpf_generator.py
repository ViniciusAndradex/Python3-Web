from random import randint

# ADICONANDO MODULO PARA GERAR CPF's
cpf = str(randint(100000000, 999999999))
new_cpf = cpf
total = index = 0
c = 10

# Criando a analise e adição dos números do digito 0.
while True:
    total += int(new_cpf[index]) * c
    if c == 2:
        digit = 11 - (total % 11)
        if digit > 9:
            digit = 0
        new_cpf += str(digit)
        if len(new_cpf) == 11:
            break
        total = index = 0
        c = 11
    c -= 1
    index += 1

def cpf_generator():
    return new_cpf
    