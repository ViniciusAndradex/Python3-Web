from POO.contas.contabanco import Conta


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo Precisa ser númerico!')

        if (self.saldo + self.limite) < valor:
            print('Valor Ultrapassa o maxímo permitido.')
            return

        self.saldo -= valor
