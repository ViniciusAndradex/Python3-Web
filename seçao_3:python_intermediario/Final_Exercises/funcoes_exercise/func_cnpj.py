def removecaracter(cnpj):
    var = ''.join([x if x != '.' and x != '/' and x != '-' else '' for x in cnpj])
    return var


def digito(soma):
    formula = 11 - (soma % 11)
    return str('0') if formula > 9 else str(formula)


def descobresoma(digitos, num=5, cont=0):
    for value in digitos:
        cont += int(value) * num
        if num == 2:
            num = 9
            continue
        num -= 1
    return cont


def validacao(cnpj_gerado, cnpj_original):
    return f'CNPJ: {cnpj_gerado}\nVÁLIDO' if cnpj_gerado == cnpj_original else f'CNPJ: {cnpj_gerado}\nINVÁLIDO'
