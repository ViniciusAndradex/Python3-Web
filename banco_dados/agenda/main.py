import sqlite3

class AgendaDB():
    def __init__(self, arquivo):
        self.conexao = sqlite3.connect(arquivo)
        self.cursor = self.conexao.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (:nome, :telefone)'
        self.cursor.execute(consulta, {'nome': nome, 'telefone': telefone})
        self.conexao.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=:nome, telefone=:telefone WHERE id=:id'
        self.cursor.execute(consulta, {'nome': nome, 'telefone': telefone, 'id': id})
        self.conexao.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=:id'
        self.cursor.execute(consulta, {'id': id})
        self.conexao.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')

        for linha in self.cursor.fetchall():
            print(linha)
    
    def listar_2(self, valor):
        consulta = 'SELECT * FROM agenda WHERE agenda.nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conexao.close()

if __name__ == '__main__':
    agenda = AgendaDB('sql/agenda.db')

    agenda.listar()
    print('------------')
    agenda.listar_2('Vinicius')