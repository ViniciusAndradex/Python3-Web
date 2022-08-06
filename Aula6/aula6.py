nome = 'Vinicius'
idade = 32
altura = 1.85
e_maior = idade >= 18
peso = 80
print('Nome:', nome)  # str
print('Idade:', idade)  # int
print('Altura:', altura)  # float
print('É maior:', e_maior)  # bool
print('/' * 10)
print(idade * altura)
imc = peso / altura ** 2
print('IMC: ', end='')
print(f'{nome} tem {idade} anos de idade e seu imc é de {imc:.2f}')
