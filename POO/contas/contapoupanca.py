from POO.contas.contabanco import Conta


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo Precisa ser númerico!')

        if self.saldo < valor:
            print('Saldo Insuficiente.')
            return

        self.saldo -= valor
        self.detalhe()
