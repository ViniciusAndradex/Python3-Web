from funcoes_exercise.func_cnpj import master
cnpj = '04.252.011/0001-10'

if master(cnpj):
    print(f'CNPJ: {cnpj}\nVÁLIDO')
else:
    print(f'CNPJ: {cnpj}\nINVÁLIDO')
