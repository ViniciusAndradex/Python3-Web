num = input('Digite um número: ')
n = input('Digite outro número: ')

# isnumeric isdigit is decimal = Funções para descobrir se pode ser convertido para numeros
# e somente  números e portanto negativos e float retorna false.
if num.isdigit() and n.isdigit():
    num = int(num)
    n = int(n)
    print(n + num)
else:
    print('Não pude converter os números para realizar contas.')
