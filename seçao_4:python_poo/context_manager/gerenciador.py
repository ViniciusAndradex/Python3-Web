class Arquivo:  # Gerenciador
    def __init__(self, arquivo, modo):
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):  # exc_type:Tipo de exceção | exc_val: Valor | exc_tb: Trace Back
        self.arquivo.close()
        # return True Caso a exception tenha sido tratada.


with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa')
