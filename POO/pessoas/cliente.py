from POO.pessoas.pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self._conta = {}

    @property
    def conta(self):
        return self._conta

    def detalhar(self):
        self.c