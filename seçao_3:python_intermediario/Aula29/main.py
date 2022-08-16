from vendas.calc_preco import reducao, aumento

# from vendas.calc_preco import aumento

price = 49.90
preco_com_aumento = aumento(valor=price, porcentagem=15, formatar=True)
print(preco_com_aumento)

preco_com_reducao = reducao(valor=price, porcentagem=15, formatar=True)
print(preco_com_reducao)
