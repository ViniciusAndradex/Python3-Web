def fib(numero=0):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'FizzBuzz'
    if numero % 3 == 0:
        return 'Fizz'
    if numero % 5 == 0:
        return 'Buzz'
    return numero


retorno = fib(numero=int(input('Digite um número: ')))
print(retorno)
