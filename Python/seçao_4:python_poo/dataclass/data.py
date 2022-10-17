from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    def __post_init__(self):
        nome = f'{self.nome}{self.sobrenome}'

    # @property
    # def nome_completo(self):
    #     return f'{self.nome}{self.sobrenome}'


p = Pessoa('Jorge', ' Antunes')
p1 = Pessoa('Jorge', ' Antunes')
# print(p.nome_completo)
print(p == p1)


