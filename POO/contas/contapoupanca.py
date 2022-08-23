from POO.contas.contabanco import Conta


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo Precisa ser númerico!')

        if self.saldo < valor:
            print('Valor Ultrapassa o maxímo permitido.')
            return

        self.saldo -= valor
