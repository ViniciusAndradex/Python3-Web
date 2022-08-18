
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):  # É uma instancia do tipo str
            valor = float(valor.replace('R$', ''))
        self._preco = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str):
            valor = valor.title()
        self._nome = valor


p1 = Produto('camiseta', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('caNeCa', 'R$15')
p2.desconto(10)
print(p2.nome, p2.preco)

