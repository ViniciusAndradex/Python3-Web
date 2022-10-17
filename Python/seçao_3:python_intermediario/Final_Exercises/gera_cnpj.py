from funcoes_exercise.func_cnpj import master_gera
from random import randint

for c in range(4):
    cnpj = str(randint(10000000, 99999999)) + '0001'
    print(f'CNPJ: {master_gera(cnpj)}')
