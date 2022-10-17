from pessoa import Pessoa

p1 = Pessoa('Jorge', 31)
p2 = Pessoa('Brito', 20)

# p1.comer('Maçã')
# p1.falar('POO')
# p1.parar_comer()
# p1.falar('POO')
# p1.comer('Alimento')
# p1.parar_falar()
# p1.falar('Assunto')

print(p1.ano_atual)
print(p2.ano_atual)
print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())
