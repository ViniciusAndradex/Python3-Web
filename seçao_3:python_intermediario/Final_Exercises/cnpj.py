from funcoes_exercise.func_cnpj import removecaracter, digito, descobresoma, validacao

cnpj = '04.252.011/0001-10'
no_digit_cnpj = '04.252.011/0001'
new_cnpj = removecaracter(no_digit_cnpj)

while len(new_cnpj) < 14:
    new_cnpj += digito(descobresoma(new_cnpj)) if len(new_cnpj) < 13 else digito(descobresoma(new_cnpj, num=6))

print(validacao(new_cnpj, removecaracter(cnpj)))
