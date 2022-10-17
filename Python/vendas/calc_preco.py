from vendas.formata.preco import real


def aumento(valor, porcentagem, formatar=False):
    r = valor + (valor * (porcentagem / 100))
    if formatar:
        return real(r)
    else:
        return r


def reducao(valor, porcentagem, formatar=False):
    r = valor - (valor * (porcentagem / 100))
    if formatar:
        return real(r)
    else:
        return r
