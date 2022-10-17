from classes_abstract.contapoupanca import ContaPupanca
from classes_abstract.contacorrente import ContaCorrente

cp = ContaPupanca(1111, 2222, 0)

cp.depositar(10)
cp.saque(5)
cp.saque(5)
cp.saque(1)
print('-' * 10)

cc = ContaCorrente(agencia=1111, conta=3333, saldo=0, limite=500)
cc.depositar(100)
cc.saque(600)
cc.depositar(1000)
