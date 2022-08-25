class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.clientes = []
        self.contas = []

    def inserir_clientes(self, cliente):
        self.clientes.append(cliente)

    def inserir_conta(self, contas):
        self.contas.append(contas)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False

        if cliente._conta not in self.contas:
            return False

        if cliente._conta.agencia not in self.agencias:
            return False

        return True
