from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo


    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo Precisa ser númerico!')

        self._saldo = valor

    def deposito(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo Precisa ser númerico!')

        self.saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass
