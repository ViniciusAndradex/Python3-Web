
cnpj = '04.252.011/0001'
new_cnpj = ''.join([x if x != '.' and x != '/' and x != '-' else '' for x in cnpj])

while True:
    cont = 0
    num = 5
    if len(cnpj) == 13:
        num = 6

    for value in new_cnpj:
        cont += int(value) * num
        if num == 2:
            num = 9
        num -= 1
    formula = 11 - (cont % 11)
    new_cnpj += str('0') if formula > 9 else str(formula)
    print(new_cnpj)
    break
