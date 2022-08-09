def aumento(valor=0.0, percentual=0):
    perc = valor * percentual / 100
    return perc + valor


dinheiro = aumento(100, 50)
print(f'R${dinheiro:.2f}')
print(f'R${aumento():.2f}')
print(f'R${aumento(valor=200.9):.2f}')
print(f'R${aumento(valor=200.9,percentual=10):.2f}')
