lista = ['Luiz', 'João', 'Maria', 1, 2, 3]
# Por convenção caso não quisermos mais utilizar os valores que estão na lista criamos ela como *_ para indicar a outros
# devs
n1, n2, n3, *qualquer, ultimo_valor = lista

print(n1, n2, n3, qualquer, ultimo_valor)
