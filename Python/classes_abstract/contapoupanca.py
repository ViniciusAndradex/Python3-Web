from classes_abstract.conta import Conta


class ContaPupanca(Conta):
    def saque(self, valor):
        if self.saldo < valor:
            print('Saldo Insuficiente!')
            return
        self.saldo -= valor
        self.detalhes()
