num1 = 10
num_2 = 3
div = num1 / num_2

print(f'{div:.2f}')
print(f'{num1:0>10}')
print(f'{num1:0^10}')
print(f'{num1:0>10.2f}')
nome = 'Vinicius Andrade'
print(f'{nome:s}')
print('-' * 10)
nome_formatado = f'{nome:@>50}'
print(nome_formatado)
print(nome.ljust(30, '-'))
