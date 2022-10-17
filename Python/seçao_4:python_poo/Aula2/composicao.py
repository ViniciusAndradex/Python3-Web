from classes_composicao import Endereco, Cliente

cliente1 = Cliente('Luiz', 32)
cliente2 = Cliente('Maria', 55)
cliente3 = Cliente('João', 19)

print(cliente1.nome)
cliente1.insere_endereco('Belo Horizonte', 'MG')
cliente1.lista_enderecos()
print()

print(cliente2.nome)
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
cliente2.insere_endereco('Salvador', 'BA')
cliente2.lista_enderecos()
print()

print(cliente3.nome)
cliente3.insere_endereco('São Paulo', 'SP')
cliente3.lista_enderecos()
print()


