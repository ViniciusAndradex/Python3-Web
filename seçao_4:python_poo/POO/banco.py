from contas.contabanco import Conta
from pessoas.cliente import Cliente


class Banco:
    def __init__(self, cliente, conta):
        self._cliente = cliente
        self._conta = conta
        self._autenticar = False

    @property
    def autenticar(self):
        return self._autenticar

    @classmethod
    def autenticar_banco(cls, agencia, cliente, conta):
        if not isinstance(agencia, Conta):
            print('A agência em questâo não pertence ao banco solicitado.')
            return False

        if not isinstance(cliente, Cliente):
            print('A agência em questâo não pertence ao banco solicitado.')
            return False

        if not isinstance(conta, Conta):
            print('A agência em questâo não pertence ao banco solicitado.')
            return False

        return True
    