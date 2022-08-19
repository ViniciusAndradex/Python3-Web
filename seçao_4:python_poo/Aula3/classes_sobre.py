class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nome} está falando da classe {self.nomeclasse}...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} Comprando...')

    def falar(self):
        print(f'Estou em cliente...')


class ClienteVIP(Cliente):
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)  # Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        super().falar()
        print(f'{self.nome} {self.sobrenome}')
