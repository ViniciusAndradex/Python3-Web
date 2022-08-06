nome = input('Qual seu nome: ')
idade = input('Qual sua idade: ')

ano_nasc = 2022 - int(idade)

print(f'O usuário digitou {nome} e o tipo do usuário é {type(nome)}')
print(f'{nome} tem {idade} anos, ano de nascimento {ano_nasc}.')