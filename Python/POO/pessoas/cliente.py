from POO.pessoas.pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self._conta = None

    def inserir_conta(self, conta):
        self._conta = conta
