from POO.pessoas.cliente import Cliente
from POO.contas.contapoupanca import ContaPoupanca
from POO.contas.contacorrente import ContaCorrente
from POO.banco.banco import Banco

bank = Banco()
c1 = Cliente('Luiz', 30)
c2 = Cliente('Maria', 18)
c3 = Cliente('João', 50)

conta1 = ContaPoupanca(1111, 254136, 0)
conta2 = ContaCorrente(2222, 254137, 0)
conta3 = ContaPoupanca(1212, 2541368, 0)

c1.inserir_conta(conta1)
c2.inserir_conta(conta2)
c3.inserir_conta(conta3)

bank.inserir_clientes(c1)
bank.inserir_conta(conta1)
bank.inserir_clientes(c2)
bank.inserir_conta(conta2)

if bank.autenticar(c2):
    c2._conta.deposito(40)
    c2._conta.sacar(60)
else:
    print('Cliente não autenticado')
