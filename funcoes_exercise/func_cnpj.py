def master(cnpj):
    cnpj = removecaracter(cnpj)
    new_cnpj = removecaracter(cnpj[:-2])

    if eh_sequencia(cnpj):
        print('É uma sequência!')
        return False

    try:
        new_cnpj += digito(descobresoma(new_cnpj))
        new_cnpj += digito(descobresoma(new_cnpj, num=6))
    except Exception:
        return False

    return validacao(new_cnpj, cnpj)


def master_gera(cnpj):
    if eh_sequencia(cnpj):
        print('É uma sequência!')
        return False

    try:
        cnpj += digito(descobresoma(cnpj))
        cnpj += digito(descobresoma(cnpj, num=6))
    except Exception:
        return False

    return formatar(cnpj)


def eh_sequencia(cnpj):
    sequence = cnpj[0] * len(cnpj)
    if cnpj == sequence:
        return True
    else:
        return False


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
    return True if cnpj_gerado == cnpj_original else False


def formatar(cnpj):
    return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
