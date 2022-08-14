from vendas import calc_preco
# from vendas.calc_preco import aumento

price = 49.90
preco_com_aumento = calc_preco.aumento(valor=price, porcentagem=15, formata=True)
print(preco_com_aumento)

preco_com_reducao = calc_preco.reducao(valor=price, porcentagem=15)
print(preco_com_reducao)
