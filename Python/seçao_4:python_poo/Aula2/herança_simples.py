from classes_herança import Cliente, Aluno, Pessoa

c1 = Cliente('Luiz', 45)
print(c1.nome)
c1.falar()
c1.comprar()

a1 = Aluno('Maria', 54)
print(a1.idade)
a1.falar()
a1.estudar()

p1 = Pessoa('Jorge', 43)
p1.falar()
